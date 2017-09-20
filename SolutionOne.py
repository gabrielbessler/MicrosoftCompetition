def main():
    '''
    Solution One
    '''
    i = input()
    test = i.split(',')
    total = 0
    for num in test:
        total += int(num)

    return int(total / len(test))

