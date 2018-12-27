'''
Name : Insertion sort implementation using python 3.4
Author,
Md Imran Sheikh
Dept. of CSE, JUST
'''

def insertion_sort(L):
    n = len(L)
    for i in range(1, n):
        item = L[i]
        j = i-1
        while j >= 0 and L[j] > item:
            L[j+1] = L[j]
            j = j-1
            L[j+1] = item
    return L

if __name__=="__main__":
    L = [6,5,2,4]
    print(insertion_sort(L))