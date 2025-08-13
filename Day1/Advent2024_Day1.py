import math

def p1():
    with open("Day1_Input.txt") as f:
        left = []
        right = []

        for line in f:
            values = line.split()
            left.append(int(values[0]))
            right.append(int(values[1]))

        left.sort()
        right.sort()

        distance = 0
        for i in range(len(left)):
            distance = distance + abs(int(left[i])-int(right[i]))
            
        print(distance)
p1()

def p2():
    with open("Day1_Input.txt") as f:
        left = []
        right = []

        for line in f:
            values = line.split()
            left.append(int(values[0]))
            right.append(int(values[1]))

    seen_locations = {}
    left.sort()
    right.sort()   

    similarity_score = 0
    for left_location in left:
        if left_location in seen_locations: 
            similarity_score += int(left_location) * int(seen_locations[left_location])
        else:
            for right_location in right:
                num_repeated = 0
                if right_location == left_location:
                    num_repeated +=1
                    similarity_score += int(left_location * num_repeated)
                    seen_locations[left_location] = num_repeated
                    
    print (similarity_score)

p2()