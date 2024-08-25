def selection_sort(nlist):
    num = len(nlist)
    for i in range(num - 1):
        min_index = i
        for j in range(i + 1, num):
            if nlist[j] < nlist[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        nlist[i], nlist[min_index] = nlist[min_index], nlist[i]

nlist = [23, 66, 1, 99, 44]

selection_sort(nlist)
print("The list after selection sort is:")
print(nlist)
