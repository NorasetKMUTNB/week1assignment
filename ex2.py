# recursion
def re_ex2(k):      
    if k > 1: return re_ex2(k-1)+k
    elif k == 1: return 2
    elif k == 0: return 1

for i in range(8):
    print('this is {} line {}'.format(i, re_ex2(i)))