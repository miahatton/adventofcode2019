# My solution to the problem posted at https://adventofcode.com/2019/day/2

noun1 = 12
verb1 = 2

def get_output(noun,verb):
    Intcode = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,6,19,23,2,6,23,27,1,5,27,31,2,31,9,35,1,35,5,39,1,39,5,43,1,43,10,47,2,6,47,51,1,51,5,55,2,55,6,59,1,5,59,63,2,63,6,67,1,5,67,71,1,71,6,75,2,75,10,79,1,79,5,83,2,83,6,87,1,87,5,91,2,9,91,95,1,95,6,99,2,9,99,103,2,9,103,107,1,5,107,111,1,111,5,115,1,115,13,119,1,13,119,123,2,6,123,127,1,5,127,131,1,9,131,135,1,135,9,139,2,139,6,143,1,143,5,147,2,147,6,151,1,5,151,155,2,6,155,159,1,159,2,163,1,9,163,0,99,2,0,14,0]
    Intcode[1] = noun
    Intcode[2] = verb
    i = 0
    while i < len(Intcode)-4:
        if Intcode[i] == 99:
            break
        else:
            num1 = Intcode[Intcode[i+1]]
            num2 = Intcode[Intcode[i+2]]
            replaceIndex = Intcode[i+3]
            if Intcode[i] == 1:
                Intcode[replaceIndex] = num1+num2
            elif Intcode[i] == 2:
                Intcode[replaceIndex] = num1 * num2
            i += 4
    return Intcode[0]

part1 = get_output(noun1,verb1)
print(part1)
#n = 0
#v = 0

goal = 19690720

for n in range(1,100):
    for v in range(1,100):
        if get_output(n,v) == goal:
            solution = 100*n+v
            print(solution)
            break



