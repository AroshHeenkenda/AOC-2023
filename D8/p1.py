

def p1():

    f = open("in.txt")
    lines = [l.strip() for l in f.readlines()]
    f.close()

    steps = lines[0]

    nodes = {}

    for i in range(2, len(lines)):

        line = lines[i].split(" = ")
        node = line[0]
        data = line[1][1:-1].split(", ")
        nodes[node] = data

    
    num_steps = 0
    cur = "AAA"
    s = 0

    while cur != "ZZZ":

        if steps[s] == "L":
            cur = nodes[cur][0]
        else:
            cur = nodes[cur][1]
        
        num_steps += 1

        s += 1
        if s == len(steps):
            s = 0

    return num_steps



if __name__ == "__main__":

    out = p1()
    print(out)