
def p1():
    f = open("in.txt")

    lines = [line.strip() for line in f.readlines()]

    total = 0

    for line in lines:
        
        num = ""

        for let in line:
            if let.isnumeric():
                num += let
        
        total += int(num[0]+num[-1])
        

    f.close()
    return total

if __name__ == "__main__":

    out = p1()
    print(out)