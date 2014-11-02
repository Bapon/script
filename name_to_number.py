__author__ = 'bapon'


D = {'a': 1, 'b': 7, 'c':3}
s = input("Your name: ")

def letter_to_num():
    count = 0
    for i in s:
        if i in D:
            count += D[i]
    return count

def tvarsumman(n):
    if  n<10:
        print (n)
    else:
        tvarsumman(int(n/10) + n%10)


tvarsumman(letter_to_num())