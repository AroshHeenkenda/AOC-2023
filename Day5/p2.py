
def p2():

    f = open("in.txt")
    lines = [line.strip() for line in f.readlines()]
    f.close()

    seeds = [int(seed) for seed in lines[0].replace("seeds: ", "").split()]
    pairs = [(seeds[i], seeds[i]+seeds[i+1]) for i in range(0, len(seeds), 2)]

    conv = [[], [], [], [], [], [], []]

    ref = 0

    for i in range(2, len(lines)):

        line = lines[i]

        if line == "seed-to-soil map:":
            ref = 0
        elif line == "soil-to-fertilizer map:":
            ref = 1
        elif line == "fertilizer-to-water map:":
            ref = 2
        elif line == "water-to-light map:":
            ref = 3
        elif line == "light-to-temperature map:":
            ref = 4
        elif line == "temperature-to-humidity map:":
            ref = 5
        elif line == "humidity-to-location map:":
            ref = 6
        elif line == "":
            continue
        else:
            vals = [int(val) for val in line.split()]
            conv[ref].append(vals)


    loc = 0

    while True:

        print(loc)

        cur = loc

        for j in range(len(conv)-1, -1, -1):

            for k in range(len(conv[j])):

                d, s, r = conv[j][k]
                
                if (cur >= d and cur <= d+r):

                    cur = s + (cur - d)
                    break

        if check_pairs(cur, pairs):
            break
        else:
            loc += 1
    
    

    return loc


def check_pairs(l, s_pairs):

    for pair in s_pairs:

        if (l >= pair[0] and l <= pair[1]):
            return True

    return False


if __name__ == "__main__":

    out = p2()
    print(out)