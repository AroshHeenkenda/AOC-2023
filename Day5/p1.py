

def p1():


    f = open("in.txt")

    lines = [line.strip() for line in f.readlines()]

    seeds = [int(seed) for seed in lines[0].replace("seeds: ", "").split()]
    locations = [0]*len(seeds)

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


    for i in range(len(seeds)):

        cur = seeds[i]

        for j in range(len(conv)):

            for k in range(len(conv[j])):

                d, s, r = conv[j][k]
                
                if (cur >= s and cur <= s+r):

                    cur = d + (cur - s)
                    break

        locations[i] = cur


    return min(locations)


if __name__ == "__main__":

    out = p1()
    print(out)