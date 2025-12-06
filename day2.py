def sumOfInvalidIds_part1():
    sum = 0
    with open('day2_input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            values = line.split(',')
            
            for value in values:
                numbers = value.split('-')
                num1 = int(numbers[0])
                num2 = int(numbers[1])
                
                for i in range(num1, num2 + 1):
                    if not isValidId_part1(i):
                        sum += i

    return sum

def isValidId_part1(num):
    numStr = str(num)
    if len(numStr) % 2 > 0:
        return True

    left = 0
    mid = len(numStr) // 2
    while(mid < len(numStr)):
        if numStr[left] != numStr[mid]:
            return True
        left += 1
        mid += 1
        
    return False
    
print('Invalid part 1 = ', sumOfInvalidIds_part1())

def sumOfInvalidIds_part2():
    invalids = set()
    with open('day2_input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            values = line.split(',')
            
            for value in values:
                numbers = value.split('-')
                num1 = int(numbers[0])
                num2 = int(numbers[1])
                
                for i in range(num1, num2 + 1):
                    if not isValidId_part2(i):
                        print('invalid = ', i)
                        invalids.add(i);

    return sum(invalids)

def isValidId_part2(num):
    numStr = str(num)
    n = len(numStr)
    substr = ''
    
    mid = n // 2
    for i in range(1, mid+1):
        if n % i == 0:
            substr = numStr[:i]
            iterator = n // i
            if substr * iterator == numStr:
                return False

    return True

print('Invalid part 2 = ', sumOfInvalidIds_part2())