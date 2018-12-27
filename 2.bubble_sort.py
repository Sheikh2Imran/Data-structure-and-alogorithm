'''
Name : Bubble sort implementation using python 3.4
Author,
Md Imran Sheikh
Dept. of CSE, JUST
'''
def bubble_sort(L):
    n = len(L)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L

if __name__=="__main__":
    L = [3,1,7,6,2]
    print(bubble_sort(L))