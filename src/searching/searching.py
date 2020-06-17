
# this is iterative

# def linear_search(arr, target):
#     # Your code here
#     # need to return the index value
#     for i in range(0,len(arr)):
#         if arr[i] == target:
#             return i
        
#     return -1   # not found


def linear_search(arr, target):
    # Your code here
    # need to return the index value
    if arr:
        if target == arr[0]:
            return arr[0]
        else:
            arr = arr.pop(0)
            linear_search(arr,target)

        
    return -1   # not found

x = [8,4,5,2,7,9,1]

linear_search(x,4)
# Write a recursive implementation of Binary Search

# this is iterative?
def binary_search(arr, target):

    # Your code here
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == arr[mid]:
            return mid
        elif target <= arr[mid]:
            #throw out right side
            high = mid - 1
        else:
            # throw out left side
            low = mid + 1

    return -1


def binary_search(arr, target):

    # Your code here
    print(arr)
    # need an array thats already sorted
    low = 0
    high = len(arr) - 1

    mid = (low + high) // 2
    if target == arr[mid]:
        return mid
    elif target > arr[mid]:
        #throw out left side
        high = len(arr) - 1
        new_arr = arr[mid:high]
        binary_search(new_arr,target)
    elif target < arr[mid]:
        # throw out right side
        low = 0
        new_arr = arr[low:(mid+1)]
        binary_search(new_arr,target)
    elif mid == None:
        return -1
    
    return binary_search(arr, target)

x = [1,2,3,4,5,6,7,8]

print(binary_search(x,3))