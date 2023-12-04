
def p2():

    f = open("in.txt")
    lines = [line.strip().split(": ") for line in f.readlines()]
    f.close()

    cards = [{"occ": 1, "nums": 1}]*len(lines)

    for i in range(len(lines)):
        lines[i][1] = lines[i][1].split(" | ")
        lines[i][0] = int(lines[i][0].replace("Card ", ""))

        for j in range(len(lines[i][1])):
            lines[i][1][j] = [int(num) for num in lines[i][1][j].split()]

    new = True
    while new:

        new = False

        for i in range(len(cards)):

            if cards[i]["nums"] > 0:
                cards[i]["nums"] -= 1

                win, mine = lines[i][1]
                count = 0
                for m in mine:
                    if m in win:
                        count += 1
                
                if count > 0:
                    new = True
                
                if (i + 1 +count) > len(lines):
                    count = len(lines) - 1

                for inc in range(i+1, i+1+count):
                    cards[inc]["nums"] += 1
                    cards[inc]["occ"] += 1

    for card in cards:
        total += card["occ"]

    return total


if __name__ == "__main__":

    out = p2()
    print(out)