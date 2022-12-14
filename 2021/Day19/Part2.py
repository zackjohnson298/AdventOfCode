import numpy as np
import json
from Helpers import *


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    scanners = {}
    points = []
    scanner = 0
    for line in lines[1:] + [lines[0]]:
        if '---' in line:
            scanners[scanner] = {
                'beacons': points,
                'position': None,
                'orientation': None,
                'norms': {
                    tuple(point):
                    tuple([
                        np.linalg.norm(p - point) for p in points #if np.linalg.norm(point_a - point) > 0.1
                    ]) for point in points
                }
            }
            scanner += 1
            points = []
            continue
        if len(line) > 0:
            points.append(np.array([int(value) for value in line.split(',')]).T)
    scanners[0]['position'] = np.array([0, 0, 0], dtype='int').T
    scanners[0]['orientation'] = np.identity(3, dtype='int')
    return scanners


def validate(points_a: [np.array], points_b: [np.array], minimum=12):
    count = 0
    for point_a in points_a:
        for point_b in points_b:
            if np.linalg.norm(point_a - point_b) < 0.01:
                count += 1
                if count >= minimum:
                    return True
    return False


def remove_duplicates(points):
    points = [tuple(point.tolist()) for point in points]
    points = set(points)
    points = [np.array(point).T for point in points]
    return points


def find_overlapping_point(norms_a, norms_b, minimum=12):
    for point_a, norm_a in norms_a.items():
        for point_b, norm_b in norms_b.items():
            intersection = set(norm_a).intersection(set(norm_b))
            if len(intersection) >= minimum:
                return np.array(point_a).T, np.array(point_b).T
    return None, None


def generate_overlaps(scanners):
    overlaps = {scanner_id: {} for scanner_id in scanners}
    for scanner_a_id, scanner_a in scanners.items():
        for scanner_b_id, scanner_b in scanners.items():
            if scanner_a_id == scanner_b_id:
                continue
            point_a, point_b = find_overlapping_point(scanner_a['norms'], scanner_b['norms'])
            if point_a is not None:
                overlaps[scanner_a_id][scanner_b_id] = point_a
                overlaps[scanner_b_id][scanner_a_id] = point_b
    return overlaps


def traverse(overlaps, current_scanner, path):
    next_scanners = [scanner for scanner in overlaps[current_scanner] if scanner not in path]
    if len(next_scanners) == 0:
        if len(set(path)) != len(overlaps):
            if validate_path(path + [path[-2]], overlaps):
                path.append(path[-2])
            else:
                path.pop()
        else:
            path.pop()
        return
    for next_scanner in next_scanners:
        # next_path = path + [next_scanner]
        # if validate_path(next_path, overlaps):
        path.append(next_scanner)
        traverse(overlaps, next_scanner, path)


def traverse2(overlaps, current_scanner, destination, path=[]):
    next_scanners = [scanner for scanner in overlaps[current_scanner] if scanner not in path]

    for next_scanner in next_scanners:
        if next_scanner == destination:
            return path + [destination]
        new_path = traverse2(overlaps, next_scanner, destination, path=path+[next_scanner])
        if new_path is not None:
            return new_path


def get_transforms(scanners, overlaps, path):
    transform = {scanner_id: {} for scanner_id in scanners}
    for index in range(1, len(path)):
        scanner_a_id = path[index-1]
        scanner_b_id = path[index]
        scanner_a = scanners[scanner_a_id]
        scanner_b = scanners[scanner_b_id]
        transform[scanner_a_id][scanner_b_id] = {'rotation': None, 'translation': None}
        # print(index, scanner_a_id, scanner_b_id)
        aa_r_k_fixed = overlaps[scanner_a_id][scanner_b_id]
        bb_r_k_fixed = overlaps[scanner_b_id][scanner_a_id]
        for r_index, a_T_b in enumerate(rotations):
            aa_r_b = aa_r_k_fixed - a_T_b @ bb_r_k_fixed
            rotated_points = [aa_r_b + a_T_b @ bb_r_p for bb_r_p in scanner_b['beacons']]
            if validate(scanner_a['beacons'], rotated_points):
                # base_scanner['beacons'] = remove_duplicates(base_scanner['beacons'] + rotated_points)
                transform[scanner_a_id][scanner_b_id]['rotation'] = a_T_b
                transform[scanner_a_id][scanner_b_id]['translation'] = aa_r_b
                break
        else:
            print(f'No Mapping found from {scanner_a_id} to {scanner_b_id}')
    return transform


def validate_path(path, overlaps):
    for index in range(1, len(path)):
        a = path[index-1]
        b = path[index]
        if b not in overlaps[a]:
            return False
    return True


def find_manhattan(a, b):
    return sum([abs(a[ii] - b[ii]) for ii in range(len(a))])


def main():
    scanners = get_input('input.txt')
    overlaps = generate_overlaps(scanners)
    for key, value in overlaps.items():
        print(key, value)
    starting_scanner = 0
    paths = {}
    for scanner_id in scanners:
        if scanner_id != starting_scanner:
            destination = scanner_id
            path = traverse2(overlaps, starting_scanner, destination, path=[starting_scanner])
            paths[destination] = path
            print(scanner_id, path)
    transforms = {}
    print('FINDING TRANSFORMS')
    for ii, path in enumerate(paths.values()):
        print(f'{ii}/{len(paths)}')
        t = get_transforms(scanners, overlaps, path)
        transforms[tuple(path)] = t

    print('Finding positions')
    positions = {}
    for ii, (path, transform_dict) in enumerate(transforms.items()):
        print(f'{ii}/{len(paths)}')
        T = np.identity(3, dtype='int')
        p = np.array((0, 0, 0), dtype='int').T
        for index in range(1, len(path)):
            a = path[index - 1]
            b = path[index]
            t = transform_dict[a][b]
            a_T_b = t['rotation']
            aa_r_b = t['translation']
            p += T @ aa_r_b
            T = T @ a_T_b
        positions[path[-1]] = p
    print()
    max_distance = 0
    keys = list(positions.keys())
    for a in keys[:-1]:
        for b in keys[keys.index(a)+1:]:
            distance = find_manhattan(positions[a], positions[b])
            if distance > max_distance:
                max_distance = distance
    print(max_distance)

main()
