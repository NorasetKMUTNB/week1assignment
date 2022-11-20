arr = [0, -1, 2, -3, 1, -2, 1, 2, 5]

def ex5(arr):       # sum to 0 : big o(n^2) 
    check = 0       # check for "have 3 numbers sum equal 0 ?"
    l = len(arr)  
    numset = set()
    checkset = set()
    ans = []

    for i in range(l-1):            # big o(n)
        for j in range(i+1, l):     # big o(n)
            x = -(arr[i] + arr[j])

            if (x in numset) and (x != arr[i]) and (x != arr[j]):
                temp = [arr[i], arr[j], x]
                temp.sort()         # sort
                temp=tuple(temp)    # list => tuple
                
                if temp in checkset: break # it's duplicate

                ans.append(temp)
                checkset.add(temp)
                check+=1

            else: numset.add(arr[j])

    if check == 0: return print('no found')
    return ans

# output                
ans = ex5(arr)
l = len(ans) 
for i in range(l):
    if i == l-1: 
        print(ans[i])
        break
    print(ans[i], end=',') 
