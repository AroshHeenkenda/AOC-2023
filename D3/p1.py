

def p1():

    f = open("in.txt")

    lines = [line.strip() for line in f.readlines()]

    sum = 0

    for i in range(len(lines)):

        j = 0
        while j < len(lines[i]):
            
            if lines[i][j].isnumeric():
                num = lines[i][j]

                k = j + 1
                while (k < len(lines[i])):
                    if (lines[i][k].isnumeric()):
                        num += lines[i][k]
                        k += 1
                    else:
                        break
                        
                start = j
                end = k - 1
                text = ""

                if (start - 1) >= 0:
                    text += lines[i][start-1]
                
                if (end + 1) < len(lines[i]):
                    text += lines[i][end+1]
                
                if (i > 0 and i < len(lines)-1):
                    text += lines[i-1][start:end+1]
                    text += lines[i+1][start:end+1]

                    if (start - 1) >= 0:
                        text += lines[i-1][start-1]
                        text += lines[i+1][start-1]
                
                    if (end + 1) < len(lines[i]):
                        text += lines[i-1][end+1]
                        text += lines[i+1][end+1]
                
                if (i == 0):
                    text += lines[i+1][start:end+1]

                    if (start - 1) >= 0:
                        text += lines[i+1][start-1]
                
                    if (end + 1) < len(lines[i]):
                        text += lines[i+1][end+1]
                
                if (i == len(lines)-1):
                    text += lines[i-1][start:end+1]

                    if (start - 1) >= 0:
                        text += lines[i-1][start-1]
                
                    if (end + 1) < len(lines[i]):
                        text += lines[i-1][end+1]
            
                sym = 0

                for char in text:
                    if (char != ".") and (not char.isnumeric()):
                        sym += 1

                sum += int(num)*sym
                j += len(num)

            else:
                j += 1
    
    return sum



if __name__ == "__main__":

    out = p1()
    print(out)