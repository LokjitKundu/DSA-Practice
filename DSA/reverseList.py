def reverse(size,li):
    for i in range(size//2):
        li[i],li[size-i-1]=li[size-i-1],li[i]
    return li
size=int(input("Enter size of the list:"))
li=[None]*size
for i in range(size):
    li[i]=input(f"Enter element at index {i}:")
new_li=reverse(size,li)
print("Reversed list:",new_li)