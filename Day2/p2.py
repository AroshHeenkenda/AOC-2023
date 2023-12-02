

def p2():
    
    f = open("in2.txt")

    lines = [line.strip().split(": ") for line in f.readlines()]

    for line in lines:
        line[0] = int(line[0].replace("Game ", ""))
        line[1] = line[1].split("; ")

        for i in range(len(line[1])):
            line[1][i] = line[1][i].split(", ")

            for j in range(len(line[1][i])):
                line[1][i][j] = line[1][i][j].split()
    
    total = 0

    for line in lines:
        R, G, B = 0, 0, 0
        
        for i in range(len(line[1])):

            for j in range(len(line[1][i])):
                count, col = int(line[1][i][j][0]), line[1][i][j][1]

                if col == "red":
                    if count > R:
                        R = count
                elif col == "green":
                    if count > G:
                        G = count
                elif col == "blue":
                    if count > B:
                        B = count
        
        total += (R*G*B)

    return total




if __name__ == "__main__":
    out = p2()
    print(out)