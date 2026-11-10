def selectionSort(lst):
    for i in range(len(lst)):
        min_index = i

        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j

        lst[i], lst[min_index] = lst[min_index], lst[i]

        # min_value = lst.pop(min_index)
        # lst.insert(i, min_value)

    print(lst)

arr = [10,22,112,3,3,2,1,3,556]
selectionSort(arr)
