def deleteElement(arr,n):

    if n < 0 or n >= len(arr):
        print("Invalid index.")
        return arr
    del arr[n]
    return arr
arr = [3,7,1,9,4]
n = 3
newarray = deleteElement(arr,n)
print("New array:",newarray)
