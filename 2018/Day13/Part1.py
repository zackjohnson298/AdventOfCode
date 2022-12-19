from Objects import Cart, Track
import numpy as np


def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    carts = {}
    tracks = {}
    cart_id = 0
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char in '<>v^':
                cart = Cart(char, (r, c), cart_id)
                carts[cart_id] = cart
                cart_id += 1
                track_char = '-' if char in '><' else '|'
            else:
                track_char = char
            if track_char == ' ':
                continue
            track = Track(track_char, (r, c))
            tracks[track.pos] = track
    return carts, tracks, (len(lines), len(lines[0]))


def draw(carts: {int: Cart}, tracks: {(int, int): Track}, size):
    for r in range(size[0]):
        for c in range(size[1]):
            cart = get_cart_at_pos((r, c), carts.values())
            if cart:
                dir = cart.dir
                char = '<' if dir == (0, -1) else '>' if dir == (0, 1) else '^' if dir == (-1, 0) else 'v'
                print(char, end='')
                continue
            track = tracks.get((r, c))
            if track:
                print(track.type, end='')
            else:
                print(' ', end='')
        print()
    print()


def get_cart_at_pos(pos, carts: [Cart]):
    for cart in carts:
        if cart.pos == pos:
            return cart
    return None


def sorted_cart_ids(carts: {int: Cart}):
    sorted_ids = []
    positions = sorted([cart.pos for cart in carts.values()])
    for pos in positions:
        for cart_id, cart in carts.items():
            if cart.pos == pos:
                sorted_ids.append(cart_id)
    return sorted_ids


def detect_crash(carts: {int: Cart}):
    positions = []
    for cart_id, cart in carts.items():
        if cart.pos not in positions:
            positions.append(cart.pos)
        else:
            return cart.pos
    return None


def update(carts: {int: Cart}, tracks: {(int, int): Track}, size):
    for cart_id in sorted_cart_ids(carts):
        cart = carts[cart_id]
        track = tracks[cart.next_pos]
        cart.update(track.type)
        crash_pos = detect_crash(carts)
        if crash_pos:
            return crash_pos
    return None


def main():
    carts, tracks, size = get_input('input.txt')
    print(0)
    # draw(carts, tracks, size)
    # _ = input('next: ')
    done = False
    tick = 0
    while not done:
        tick += 1
        crash_pos = update(carts, tracks, size)
        print(tick)
        # draw(carts, tracks, size)
        if crash_pos is not None:
            print()
            print(f'Crash detected! Position: {crash_pos[1]},{crash_pos[0]}')
            _ = input('Continue: ')


main()
