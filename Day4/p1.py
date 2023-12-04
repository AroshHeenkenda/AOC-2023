


def p1():

    f = open("in.txt")
    lines = [line.strip().split(": ") for line in f.readlines()]
    f.close()

    for i in range(len(lines)):
        lines[i][1] = lines[i][1].split(" | ")
        for j in range(len(lines[i][1])):
            lines[i][1][j] = [int(num) for num in lines[i][1][j].split()]

    total = 0

    for line in lines:

        win = line[1][0]
        mine = line[1][1]
        f_win = False
        val = 0

        for num in mine:
            if num in win:
                if not f_win:
                    f_win = True
                    val = 1
                else:
                    val *= 2
        
        total += val
    
    return total


if __name__ == "__main__":

    out = p1()
    print(out)


