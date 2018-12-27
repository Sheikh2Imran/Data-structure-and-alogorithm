'''
Name : Linear search implementation using python 3.4
Author,
Md Imran Sheikh
Dept. of CSE, JUST
'''

def linear_search(L, x):
    n = len(L)
    for i in range(0, n):
        if L[i]==x:
            return i
    return -1

if __name__=="__main__":
    L=[1,2,3,4,5]
    x=5
    print(linear_search(L, x)) #this will print the position of x in the list L