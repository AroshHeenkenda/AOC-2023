
def p2():

    f = open("in.txt")
    lines = [line.strip().split(": ")[1] for line in f.readlines()]
    f.close()

    cards = []

    for i in range(len(lines)):
        lines[i] = lines[i].split(" | ")

        lines[i][0] = [int(num) for num in lines[i][0].split()]
        lines[i][1] = [int(num) for num in lines[i][1].split()]
        
        win = lines[i][0]
        nums = lines[i][1]

        match_c = 0
        for num in nums:
            if num in win:
                match_c += 1
        
        cards.append({"in": 1, "match": match_c})
    
    for i in range(len(cards)):

        m = cards[i]["match"]
        ins = cards[i]["in"]

        if m != 0:

            for j in range(i+1, i+1+m):
                cards[j]["in"] += ins

    total = 0
    for i in range(len(cards)):
        total += cards[i]["in"]

    return total


if __name__ == "__main__":

    out = p2()
    print(out)