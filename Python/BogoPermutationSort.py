# Python program for implementation of Bogo Sort
import random


# Sorts array a[0..n-1] using Bogo sort
def bogo_sort(a):
    while (not is_sorted(a)):
        random.shuffle(a)


# To check if array is sorted or not
def is_sorted(a):
    for i in range(0, len(a) - 1):
        if (a[i] > a[i + 1]):
            return False
    return True


# To generate permuatation of the array
def shuffle(a):
    n = len(a)
    for i in range(0, n):
        r = random.randint(0, n - 1)
        a[i], a[r] = a[r], a[i]


# Driver code to test above
a = [3, 2, 4, 1, 0, 5]
bogo_sort(a)
print(f'Sorted array : {a}')
