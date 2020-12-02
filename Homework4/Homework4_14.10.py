#Rhahan Sarwar
#1818962


# TODO: Write a selection_sort_descend_trace() function that
#       sorts the numbers list into descending order

def selection_sort_descend_trace(numbers):
    for r in range(len(numbers) - 1):
        largest = r
        for s in range(r + 1, len(numbers)):
            if numbers[s] > numbers[largest]:
                largest = s

        list1 = numbers[r]
        numbers[r] = numbers[largest]
        numbers[largest] = list1

        for a in numbers:
            print(str(a), end=' ')
        print()


if __name__ == "__main__":
    # TODO: Read in a list of integers into numbers, then call
    #       selection_sort_descend_trace() to sort the numbers
    numbers = [int(x) for x in input("").split()]
    selection_sort_descend_trace(numbers)
