nlist1 = []

num = int(input("enter the number of Elements for first List :\n"))

for i in range(0, num):
    element = int(input())
    nlist1.append(element)

print("FIRST LIST IS: \n")
nlist1.sort()
print(nlist1)

nlist2 = []

num2 = int(input("enter the number of Elements of second List :\n"))

for i in range(0,num2):
    element = int(input())
    nlist2.append(element)

print("SECOND LIST IS: \n")

nlist2.sort()
print(nlist2)

i=0

j=0

k=0

merge = []

size1 = len(nlist1)

size2 = len(nlist2)
while i<size1 and j<size2:
    if(nlist1[i]==nlist2[j]):
        merge.append(nlist1[i])
        merge.append(nlist2[j])
        i+=1
        j+1

    if(nlist1[i]<nlist2[j]):
        merge.append(nlist1[i])
        i+=1

    elif nlist2[j] <nlist1[i]:
        merge.append(nlist2[j])
        j+=1

for k in range(i,len(nlist1)):
    merge.append(nlist1[k])

for k in range(j,len(nlist2)):
    merge.append(nlist2[k])

print("\nlist after the merge sort : \n")

print(merge)
