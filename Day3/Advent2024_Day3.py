import re

def p1():
    with open("Day3/Day3_Input.txt") as f:
        data = f.read()
        sum = 0
        valid_instructions = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)
        for instruction in valid_instructions:
            value1 = int(instruction[0])
            value2 = int(instruction[1])
            sum += value1 * value2
    print(sum)

# p1()

def p2():
    with open("Day3/Day3_Input.txt") as f:
        data = f.read()
        sum = 0
        valid_instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", data)
        enabled = True
        for instruction in valid_instructions:
            if instruction == "don't()":
                enabled = False
            elif instruction == "do()":
                enabled = True
            elif "m" in instruction and enabled == False:
                continue
            else:
                value1 = int(instruction[instruction.find("(") + 1: instruction.find(",")])
                value2 = int(instruction[instruction.find(",") + 1: instruction.find(")")])
                sum += value1 * value2
        print(sum)
p2()