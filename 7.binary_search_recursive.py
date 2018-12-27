'''
Name : Binary search with recursive function implementation using python 3.4
Author,
Md Imran Sheikh
Dept. of CSE, JUST
'''

def binary_search(L, left, right, x):
    if left > right:
        return None
    mid = (left+right)//2
    if L[mid] == x:
        return mid
    if L[mid] > x:
        return binary_search(L, left, mid - 1, x)
    else:
        return binary_search(L, mid + 1, right, x)

if __name__=="__main__":
    L=[1,2,3,4,5]
    n = len(L)
    left, right = 0, n-1
    print("The data is occured in ",binary_search(L, left, right, 2), "position")

        