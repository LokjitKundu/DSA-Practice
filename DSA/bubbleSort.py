import time
def bubbleSort(size,li1):
    counter1=0
    for i in range(size-1):
        for j in range(size-i-1):
            counter1+=1
            if li1[j]>li1[j+1]:
                li1[j],li1[j+1]=li1[j+1],li1[j]
        print(li1)
    return li1,counter1
def modifiedBubbleSort(size,li2):
    counter2=0
    for i in range(size-1):
        flag=0
        for j in range(size-i-1):
            counter2+=1
            if li2[j]>li2[j+1]:
                flag=1
                li2[j],li2[j+1]=li2[j+1],li2[j]
        print(li2)
        if flag==0:
            break
    return li2,counter2
size=int(input("Enter the size of the list:"))
li=[None]*size
for i in range(size):
    li[i]=int(input(f"Enter element at index {i}:"))
li1=li.copy()
li2=li.copy()
start1=time.time()
sorted_li1,c1=bubbleSort(size,li1)
print(sorted_li1,"Comparisons:",c1)
end1=time.time()
total_time1=end1-start1
print("bubble sort:",total_time1," seconds")
start2=time.time()
sorted_li2,c2=modifiedBubbleSort(size,li2)
print(sorted_li2,"Comparisons:",c2)
end2=time.time()
total_time2=end2-start2
print("Modified bubble sort:",total_time2," seconds")