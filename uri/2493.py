import sys
import re


T = int(input())
while T:
    expression = [[] for i in range(T)]

    for i in range(T):
        expression[i] = re.split('[ =]', input())

    valid_people = []

    for i in range(T):
        tried = list(input().split(' '))
        operator = tried[2]
        number = int(tried[1]) - 1

        if operator == '+':
            if int(expression[number][0]) + int(expression[number][1]) != int(expression[number][2]):
                valid_people.append(tried[0])
        elif operator == '*':
            if int(expression[number][0]) * int(expression[number][1]) != int(expression[number][2]):
                valid_people.append(tried[0])
        elif operator == '-':
            if int(expression[number][0]) - int(expression[number][1]) != int(expression[number][2]):
                valid_people.append(tried[0])
        else:
            if int(expression[number][0]) + int(expression[number][1]) == int(expression[number][2]
               ) or int(expression[number][0]) - int(expression[number][1]) == int(expression[number][2]
               ) or int(expression[number][0]) * int(expression[number][1]) == int(expression[number][2]):
                valid_people.append(tried[0])

    if len(valid_people) == T:
        print("None Shall Pass!")
    elif len(valid_people) == 0:
        print("You Shall All Pass!")
    else:
        valid_people.sort()
        for i in range(len(valid_people)):
            if i < len(valid_people) - 1:
                print(valid_people[i], end=' ')
            else:
                print(valid_people[i])
    try:
        T = int(input())
    except EOFError:
        break