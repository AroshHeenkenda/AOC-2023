from functools import reduce

def p1():
    
    f = open("in.txt")
    lines = [line.strip() for line in f.readlines()]
    f.close()

    times = [int(time) for time in lines[0].replace("Time: ", "").split()]
    dists = [int(dist) for dist in lines[1].replace("Distance: ", "").split()]
    ways = [0]*len(times)

    for i in range(len(times)):

        time = times[i]

        for t in range(1, time):

            t_left = time - t
            if t_left * t > dists[i]:
                ways[i] += 1
    
    return reduce((lambda x, y: x * y), ways)




if __name__=="__main__":

    out = p1()
    print(out)