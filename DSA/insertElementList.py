def insertElement(size,element,pos,arr,count):
    if count==size:
        print("Overflow")
        return
    i=count-1
    while i>=pos:
        arr[i+1]=arr[i]
        i-=1
    arr[pos]=element
    count+=1
    return count
size=int(input("Enter the size of the list:"))
arr=[None]*size
for i in range(size):
    arr[i]=int(input(f"Enter element at index {i}:"))
    if i!=size-1:
        ans=input("Do you want to add another element? (y/n)")
        if ans=='n' or ans=='N':
            break
count=0
for item in arr:
    if item is not None:
        count+=1
element=int(input("Enter the element to insert:"))
pos=int(input("Enter the index to insert:"))
result=insertElement(size,element,pos,arr,count)
print("Updated list:")
for i in range(result):
    print(arr[i],end=" ")
print("")