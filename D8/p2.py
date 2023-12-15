import math


def p2():

    f = open("in.txt")
    lines = [l.strip() for l in f.readlines()]
    f.close()

    steps = lines[0]
    end_in_a = []
    steps_a = []
    nodes = {}

    for i in range(2, len(lines)):

        line = lines[i].split(" = ")
        node = line[0]
        if node[-1] == "A":
            end_in_a.append(node)
        data = line[1][1:-1].split(", ")
        nodes[node] = data

    for a in end_in_a:

        num_steps = 0
        cur = a
        s = 0

        while cur[-1] != "Z":

            if steps[s] == "L":
                cur = nodes[cur][0]
            else:
                cur = nodes[cur][1]
            
            num_steps += 1

            s += 1
            if s == len(steps):
                s = 0

        steps_a.append(num_steps)
    
    return math.lcm(steps_a)



if __name__ == "__main__":

    out = p2()
    print(out)