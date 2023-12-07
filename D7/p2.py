

def p1():

    f = open("in.txt")
    hands = []

    for line in f.readlines():
        line = line.strip().split()
        hands.append([line[0], int(line[1]), ""])
    
    f.close()

    poker = "J23456789TQKA"

    for h in range(len(hands)):

        cards = {}

        for card in hands[h][0]:
            if card not in cards:
                cards[card] = 1
            else:
                cards[card] += 1
        
        if "J" in cards.keys() and len(cards.keys()) != 1:
            
            num_js = cards["J"]
            del cards["J"]
            com = ["", 0]
            for key in cards.keys():
                if cards[key] > com[1]:
                    com[0] = key
                    com[1] = cards[key]
            
            cards[com[0]] += num_js
        
        uni = len(cards.keys())

        # 5 of Kind - G
        if uni == 1:
            hands[h][2] = "G"
        
        elif uni == 2:
            c_occ = []
            for key in cards.keys():
                c_occ.append(cards[key])

            # 4 of Kind - F
            if max(c_occ) == 4:
                hands[h][2] = "F"

            # Full House - E
            elif max(c_occ) == 3:
                hands[h][2] = "E"

        elif uni == 3:
            c_occ = []
            for key in cards.keys():
                c_occ.append(cards[key])

            # 3 of Kind - D
            if max(c_occ) == 3:
                hands[h][2] = "D"

            # 2 Pair - C
            elif max(c_occ) == 2:
                hands[h][2] = "C"
        
        # One Pair - B
        elif uni == 4:
            hands[h][2] = "B"

        # High Card - A
        elif uni == 5:
            hands[h][2] = "A"
    
    #Custom sort
    #   First sort by hand type
    #   Then sort on our custom alphabet
    hands.sort(key=lambda x: (x[-1], [poker.index(c) for c in x[0]]))

    win = 0

    for i in range(len(hands)):

        win += (i+1)*hands[i][1]

    return win


if __name__ == "__main__":

    out = p1()
    print(out)