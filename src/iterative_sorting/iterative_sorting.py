# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # cur_value = arr[i]
        # smallest_value = arr[smallest_index]
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here


        # i should always be the smallest value that has been found so far

        # here you need to go through the array, find the next smallest value, then swap the index of the two
        for j in range(0+i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        #swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]





        # TO-DO: swap
        # Your code here

    return arr

x = [8,4,5,2,7,9,1]
selection_sort(x)

''' UPER

U - UNDERSTAND: What is the problem asking me to do?
P - PLAN: What steps will I take to solve the problem? (Don't code much, just write out your plan)
E - EXECUTE: How do I implement those steps? (Now start coding)
R - REFLECT: Is this implementation as good as I can make it? (Optimize)

'''

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here

    # This problem is asking me to compare each value to the one next to it, swap them into ascending order,
    # and go through the loop until the entire array is sorted in ascending order

    # bubble sort is the same as insertion sort but instead of continuing to compare the same value you are
    # going down the list

    # how to continue the loop until everything is ordered? 

    # loop over each value in the array
    for i in range(0, len(arr)-1):
        # set a loop within the loop - the first loop will push the highest value to the end, so
        # the second instance of the inner loop doesnt need to include the last value in the array
        for j in range(0, len(arr)-i-1):
            cur_index = j
            
            if arr[cur_index] > arr[cur_index + 1]:
                #swap
                arr[cur_index], arr[cur_index + 1] = arr[cur_index + 1], arr[cur_index]

    return arr




x = [8,4,5,2,7,9,1]

bubble_sort(x)

def insertion_sort(arr):
    # Your code here

    for i in range(0, len(arr)):
        cur_index = i

        while cur_index > 0 and arr[cur_index] < arr[cur_index - 1]:
            #swap
            arr[cur_index], arr[cur_index - 1] = arr[cur_index - 1], arr[cur_index]
            cur_index -= 1

    return arr



'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
