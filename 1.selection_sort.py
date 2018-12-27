'''
Name : Selection sort implementation using python 3.4
Author,
Md Imran Sheikh
Dept. of CSE, JUST
'''

def selection_sort(L):
    n = len(L)
    for i in range(0, n-1):
        index_min = i
        for j in range(i+1, n):
            L[j] < L[index_min]
            index_min = j
        L[j], L[index_min] = L[j], L[index_min]
    if index_min != i:
        L[index_min], L[i] = L[index_min], L[i]

if __name__=="__main__":
    L = [6,5,2,4]
    print(selection_sort(L))
