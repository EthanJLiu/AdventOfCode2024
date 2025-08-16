def p1():
    match = "XMAS"
    lines = []
    with open("Day4/Day4_Input.txt") as f:
        for line in f:
            split_line = [c for c in line]
            lines.append(split_line)
            print(split_line)
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
   
    def search_routes(letters, row, col, dir):
        #ensure direction stays the same
        dr = dir[0]
        dc = dir[1]
        if letters == match:
            return 1
        elif letters != match[0 : len(letters)]:
            return 0
        elif row+dr < 0 or col+dc < 0 or row+dr >= len(lines) or col+dc >= len(lines[0]):
            #print(f"letters: {letters} row : {row}, col: {col}")
            return 0
        
        elif lines[row+dr][col+dc] == match[len(letters)]:
            return search_routes(letters + lines[row+dr][col+dc], row+dr, col+dc, dir)
        
        return 0
    num_matches = 0

    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if lines[r][c] == "X":
                for direction in directions:
                    num_matches += search_routes("X", r, c, direction)

    print(num_matches)
# p1()    

def p2():
    lines = []
    with open("Day4/Day4_Input.txt") as f:
        for line in f:
            split_line = [c for c in line]
            lines.append(split_line)
            print(split_line)
   
    def search_corners(row, col):
        if row == 0 or col == 0 or row == len(lines)-1 or col == len(lines[0])-1:
            return 0
        top_left_to_bottom_right = (lines[row-1][col-1] == "M" and lines[row+1][col+1] == "S") or (lines[row-1][col-1] == "S" and lines[row+1][col+1] == "M")
        bottom_left_to_top_right = (lines[row+1][col-1] == "M" and lines[row-1][col+1] == "S") or (lines[row+1][col-1] == "S" and lines[row-1][col+1] == "M")

        if top_left_to_bottom_right and bottom_left_to_top_right:
            return 1
        return 0

    num_matches = 0

    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if lines[r][c] == "A":
                num_matches += search_corners(r, c)
    print(num_matches)

p2()    

