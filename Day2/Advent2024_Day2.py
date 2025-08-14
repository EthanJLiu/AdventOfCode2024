class p1():

    def is_safe(levels):
        should_increase = None
        
        for i in range(1, len(levels)):

            current = int(levels[i])
            prev = int(levels[i-1])
            difference = prev-current

            if difference == 0:
                return False
            elif abs(difference) > 3: 
                return False
            
            if should_increase == None:
                should_increase = difference > 0
            
            if difference < 0 and should_increase != None and should_increase:
                return False
            elif difference > 0 and should_increase != None and not should_increase:
                return False
        return True

    with open("Day2/Day2_Input.txt") as f:
        safe_reports = 0
        for line in f:
            levels = line.split()
            if is_safe(levels):
                safe_reports += 1
        print (safe_reports)
p1()


class p2():

    def is_safe(levels):
        should_increase = None
        
        for i in range(1, len(levels)):
            current = int(levels[i])
            prev = int(levels[i-1])
            difference = prev-current

            if difference == 0:
                return False
            elif abs(difference) > 3: 
                return False
            
            if should_increase == None:
                should_increase = difference > 0
            
            if difference < 0 and should_increase != None and should_increase:
                return False
            elif difference > 0 and should_increase != None and not should_increase:
                return False
        return True

    with open("Day2/Day2_Input.txt") as f:
        safe_reports = 0
        for line in f:

            levels = line.split()
            if is_safe(levels):
                safe_reports += 1
            else:
                for i in range(len(levels)):
                    copy = levels.copy()
                    copy.pop(i)
                    if is_safe(copy):
                        safe_reports += 1
                        break

        print(safe_reports)

p2()