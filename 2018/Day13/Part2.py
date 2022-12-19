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
    crashed_cart_ids = []
    for cart_id in sorted_cart_ids(carts):
        if cart_id not in crashed_cart_ids:
            cart = carts[cart_id]
            track = tracks[cart.next_pos]
            cart.update(track.type)
            crash_pos = detect_crash({cart_id: cart for cart_id, cart in carts.items() if cart_id not in crashed_cart_ids})
            if crash_pos:
                crash_ids = [cart.id for cart in carts.values() if cart.pos == crash_pos]
                crashed_cart_ids.extend(crash_ids)
    return crashed_cart_ids


def main():
    carts, tracks, size = get_input('input.txt')
    # draw(carts, tracks, size)
    # _ = input('next: ')
    done = False
    while not done:
        crashed_cart_ids = update(carts, tracks, size)
        # draw(carts, tracks, size)
        for cart_id in crashed_cart_ids:
            carts.pop(cart_id)
        if len(carts) == 1:
            print('Done!')
            done = True
            for cart in carts.values():
                print(f'{cart.pos[1]},{cart.pos[0]}')


main()
