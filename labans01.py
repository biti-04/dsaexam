def array():
    arr = []
    n = int(input("Enter the number of elements: "))
    for i in range(n):
        arr.append(int(input(f"Enter element {i+1}: ")))

    search_num = int(input("number to be searched: "))

    if search_num in arr:
        occurrences = count(arr, search_num)
        print(f"The number {search_num} appears {occurrences} times.")
    else:
        print(f"The number {search_num} is not present in the array.")

if __name__ == "__main__":
    array()


