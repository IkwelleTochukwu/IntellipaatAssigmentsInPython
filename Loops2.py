def EvenNumbers(list):
    index = 0
    while index < len(list):
        if list[index] % 2 == 0:
            print(list[index], end=' ')
        index += 1
   
RandomNumbers = [10, 23, 4, 26, 4, 75, 24, 54, 176, 233, 10, 24]
EvenNumbers(RandomNumbers)


