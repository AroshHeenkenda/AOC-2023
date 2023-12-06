
def p2():
    
    f = open("in.txt")
    lines = [line.strip() for line in f.readlines()]
    f.close()

    times = int(lines[0].replace("Time: ", "").replace(" ", ""))
    dists = int(lines[1].replace("Distance: ", "").replace(" ", ""))

    ways = 0

    for t in range(1, times):

        t_left = times - t
        if t_left * t > dists:
            ways += 1
    
    return ways




if __name__=="__main__":

    out = p2()
    print(out)