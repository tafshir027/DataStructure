
# Linear Search in Python
def linearSearch(x, n, s):
    for i in range(0, n):
        if x[i] == s:
            return i
    return -1


# x variable refers to array of number
# n variable refers to total length of Array/list
# s variable refers to Search of the Number

x = [1, 2, 3, 4, 5]
n = len(x)
s = int(input("Enter Number You want to search : "))
result = linearSearch(x, n, s)
if result == -1:
    print("Number is Not found! ")
else:
    print("Number is found ")

    
