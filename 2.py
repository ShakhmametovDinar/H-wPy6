min = int(input())
max = int(input())
list1 = [1,2,3,4,5,6,7,8,9,10]

print([a for a, num in enumerate(list1) if min <= num <= max])
