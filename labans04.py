def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swapping occurred in this pass, the array is already sorted
        if not swapped:
            break
    return arr

def main():
    alphabet_arr = ['A','S','C', 'I','I']  # Example array of alphabets


def main():
    alphabet_arr = ['A','S','C', 'I','I']  # Example array of alphabets
    print("Original Array:", alphabet_arr)

    sorted_arr = bubble_sort(alphabet_arr)
    print("Sorted Array:", sorted_arr)

if __name__ == "__main__":
    main()
