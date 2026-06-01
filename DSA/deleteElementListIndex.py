def deleteElement(count,arr,pos):
    if count==-1:
         print("Underflow")
         return
    i=pos
    x=arr[pos]
    while i<count:
         arr[i]=arr[i+1]
         i+=1
    count-=1
    return x,count
size=int(input("Enter the size of the list:"))
arr=[None]*size
for i in range(size):
    arr[i]=int(input(f"Enter number at index {i}:"))
    if i!=size-1:
         ans=input("Do you want to add another element? (y/n):")
         if ans=='n' or ans=="N":
              break
count=-1
for item in arr:
        if item is not None:
            count+=1
pos=int(input("Enter index to delete element:"))
deletedElement,newCount=deleteElement(count,arr,pos)
print("Deleted element:",deletedElement)
print("Updated list:")
for i in range(newCount+1):
     print(arr[i],end=" ")
print("")