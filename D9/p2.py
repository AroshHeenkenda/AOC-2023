

def p2():

    f = open("in.txt")
    history = [[int(num) for num in line.strip().split()] for line in f.readlines()]

    ex_sum = 0

    for his in history:

        cur = his
        extra = []
        extra.append(cur)

        while True:

            if len(set(cur)) == 1:
                if cur[0] == 0:
                    break

            new_list = []

            for i in range(1, len(cur)):
                new_list.append(cur[i] - cur[i-1])
            
            extra.append(new_list)
            cur = new_list
        
        data = 0

        for i in range(len(extra) - 2, -1, -1):

            data = extra[i][0] - data
        
        ex_sum += data
    
    return ex_sum


if __name__ == "__main__":

    out = p2()
    print(out)