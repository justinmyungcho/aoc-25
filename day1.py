def find_password_part1():
    currPos = 50; # dial starts pointing at 50
    password = 0;
    with open('day1_input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            direction = line[0]  # first character, e.g., 'R'
            ticks = int(line[1:])  # everything after the first character, e.g., '11'
    
            if direction == 'R':
                newPos = currPos + ticks;
                currPos = newPos % 100;
            elif direction == 'L':
                newPos = currPos - ticks;
                currPos = newPos % 100;

            password += currPos == 0;

    return password;

print(find_password_part1());

def find_password_part2():
    currPos = 50; # dial starts pointing at 50
    hit_zero = 0;
    with open('day1_input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            direction = line[0]  # first character, e.g., 'R'
            ticks = int(line[1:])  # everything after the first character, e.g., '11'
    
            if direction == 'R':
                newPos = currPos + ticks;
                if newPos >= 100:
                    hit_zero += newPos // 100;
                currPos = newPos % 100;
            elif direction == 'L':
                newPos = currPos - ticks;
                if newPos < 0:
                    if currPos != 0:
                        hit_zero += 1 + abs(newPos) // 100;
                    elif currPos == 0:
                        hit_zero += abs(newPos) // 100;
                elif newPos == 0:
                    hit_zero += 1;
                currPos = newPos % 100;

    return hit_zero;

print(find_password_part2());