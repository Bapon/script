__author__ = 'bapon'
L = [ 1, 7, 3, 5, 8, 9 ]

def selsort(L):
    for i in range (len(L) -1):

        minIndx = i
        print(minIndx)
        minVal = L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j +=1
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] =temp

selsort(L)