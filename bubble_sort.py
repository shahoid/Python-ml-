def bubble_sort(nlist):
    num = len(nlist)
    for i in range(num):
        for j in range(0, num - i - 1):
            if nlist[j] > nlist[j + 1]:
                # Swap the elements
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]

nlist = [23, 66, 44, 1, 99]
bubble_sort(nlist)
print("The sorted list is:")
print(nlist)
