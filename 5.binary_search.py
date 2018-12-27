'''
Name : Binary search implementation using python 3.4
Author,
Md Imran Sheikh
Dept. of CSE, JUST
'''

def binary_search(L, x):
    n = len(L)
    left, right = 0, n-1
    if left > right:
        return -1
    else:
        while left <= right:
            mid = (left+right)//2
            if L[mid] == x:
                return x
            elif L[mid] < x:
                left = mid + 1
            elif L[mid] > x:
                right = mid - 1 
    return -1 #if the element is not found in the list then return -1

if __name__=="__main__":
    L=[1,2,3,4]
    x=5
    print(binary_search(L, x)) #this will print the position of x in the list L