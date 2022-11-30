

def get_input():
    with open('input.txt') as file:
        data = file.read().splitlines()
    return [int(value) for value in data]


def main():
    data = get_input()
    count = 0
    for ii in range(len(data)-1):
        if data[ii] < data[ii + 1]:
            count += 1
    print(count)
    

main()
