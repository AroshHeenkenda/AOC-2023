
def p2():
    f = open("in.txt")

    lines = [line.strip() for line in f.readlines()]

    chars = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    total = 0

    for line in lines:
        
        num = ""
        i = 0

        print(f"Line: {line}")

        while i < len(line):

            incr = False
            
            if line[i].isnumeric():
                num += line[i]
                i += 1
                incr = True
            
            else:
                for j in range(len(chars)):
                    if (len(line[i:]) >= len((chars[j]))) and (chars[j] == line[i:i+len(chars[j])]):
                        num += str(j+1)
                        incr = True
                        i += len(chars[j])-1
                        break
            
            if not incr:
                i += 1
        print(f"Number: {num}")
        print(f"2 Digit: {num[0]+num[-1]}")

        total += int(num[0]+num[-1])

        print(f"Total: {total}\n")
        
    f.close()
    return total

if __name__ == "__main__":

    out = p2()
    print(out)