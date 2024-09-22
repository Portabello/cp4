#1

#2
import math
formatstr = "%."+n+"f"
print(formatstr % math.pi)

#3
def day_of_week_and_elapsed_days(date):
    pass

#4
def distinct_sorted(input):
    unique = set()
    for x in input:
        if input not in unique:
            unique.add(x)
    list(unique).sort()
    return unique

#5
def sort_birthdays(n,birthdays):
    sorted_birthdates = sorted(birthdays, key=lambda x: (x[1],x[0],-x[2]))

#6
binary_search(v,arr):
    pass

#7
def permute(data, i, length):
    if i==length:
        print(''.join(data) )
    else:
        for j in range(i,length):
            #swap
            data[i], data[j] = data[j], data[i] 
            permute(data, i+1, length)
            data[i], data[j] = data[j], data[i]


string = "ABC"
n = len(string)
data = list(string)
permute(data, 0, n)
