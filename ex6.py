import numpy as np      # use numpy library for matrix

def checknum10(arr,sq):     # array follow column/row sq elements
    count = 0

    for i in range(sq-1):
        temp = arr[i]
        for j in range(i+1, sq):
            temp += arr[j]
            if temp > 10: break
            elif temp == 10: 
                count += 1 
                break

    return count

def ex6():
    step = 0      
    r = int(input('Enter round'))   # round 
    while step != r:
        sq = input('Enter your square in round {} : '.format(step+1))  
        i, count = 0, 0   
        try:    # str(sq) can convert to int(sq)
            sq = int(sq)
            tempmatrix = []

            while i != sq: # row in matrix
                x = input('Enter {} integers in row {} : '.format(sq, i+1)).split()     # x := array
                try:    # str(arr) can convert to int(arr)
                    temp = []
                    for j  in range(len(x)): 
                        temp.append(int(x[j]))
                    if len(temp) != sq: 
                        print("it's not {} numbers!! try again!! : ".format(sq)) 
                        break
                    tempmatrix.append(temp) 
                    i+=1
                        
                except ValueError:  # str(arr) can't convert to int(arr)
                    x = input('Please!! enter {} integers in row {} : '.format(sq, i+1)).split()

            # creating matrix
            matrix = np.array(tempmatrix)
            #print('matrix : \n', matrix)

            # find number sum equal 10
            for k in range(sq):
                count+=checknum10(matrix[k,:],sq)
                count+=checknum10(matrix[:,k],sq)
            
            if count == 0: print('no found')
            print(count)

        except ValueError:  # str(sq) can't convert to int(sq)
            sq = input('Please enter an integer again : ')
        
        step+=1

ex6()