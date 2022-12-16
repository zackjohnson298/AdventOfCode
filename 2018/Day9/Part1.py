import json


def main():
    players = 10
    last_marble = 1618
    scores = {player: 0 for player in range(1, players+1)}
    marbles = [0]
    player = 0
    current_index = 0
    for marble in range(1, last_marble+1):
        player = player % players + 1
        if marble % 23 == 0:
            current_index = current_index - 7
            scores[player] += marble + marbles.pop(current_index)
        else:
            current_index = (current_index + 2)
            if current_index > len(marbles):
                current_index -= len(marbles)
            marbles.insert(current_index, marble)
    print(json.dumps(scores, indent=4))
    print(max(scores.values()))
    print(marbles[0])


main()
