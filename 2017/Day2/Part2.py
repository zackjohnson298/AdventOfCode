
def get_input(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return [[int(value) for value in line.split()] for line in lines]


def main():
    lines = get_input('input.txt')
    total = 0
    for line in lines:
        done = False
        for ii in range(len(line)-1):
            for jj in range(ii+1, len(line)):
                a = line[ii]
                b = line[jj]
                if a % b == 0:
                    total += int(a / b)
                    done = True
                    break
                elif b % a == 0:
                    total += int(b / a)
                    done = True
                    break
            if done:
                break
    print(total)


main()
