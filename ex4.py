arrtest = [0,1,3,5,6,8,9,1]

def ex4(arr):   # arr := list(int)
    tempset = set()
    for num in arr:     # O(n)
        if num in tempset: return True     # work when have duplicate
        tempset.add(num)
    return False                        # work when haven't duplicate

print(ex4(arrtest))