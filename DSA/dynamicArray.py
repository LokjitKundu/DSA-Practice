class DynamicArray:

    def __init__(self, capacity=16):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.length = 0

    # Size of array
    def size(self):
        return self.length

    # Check if empty
    def is_empty(self):
        return self.length == 0

    # Get element
    def get(self, index):
        return self.arr[index]

    # Set element
    def set(self, index, elem):
        self.arr[index] = elem

    # Clear array
    def clear(self):
        for i in range(self.capacity):
            self.arr[i] = None
        self.length = 0

    # Add element
    def add(self, elem):

        # Resize if full
        if self.length >= self.capacity:

            # Double capacity
            self.capacity *= 2

            # Create new array
            new_arr = [None] * self.capacity

            # Copy elements
            for i in range(self.length):
                new_arr[i] = self.arr[i]

            self.arr = new_arr

        # Insert element
        self.arr[self.length] = elem
        self.length += 1

    # Remove at index
    def remove_at(self, rm_index):

        if rm_index < 0 or rm_index >= self.length:
            raise IndexError("Invalid index")

        data = self.arr[rm_index]

        new_arr = [None] * (self.length - 1)

        j = 0

        for i in range(self.length):

            if i == rm_index:
                continue

            new_arr[j] = self.arr[i]
            j += 1

        self.arr = new_arr

        self.length -= 1
        self.capacity = self.length

        return data

    # Remove element by value
    def remove(self, obj):

        for i in range(self.length):

            if self.arr[i] == obj:
                self.remove_at(i)
                return True

        return False

    # Find index
    def index_of(self, obj):

        for i in range(self.length):

            if self.arr[i] == obj:
                return i

        return -1

    # Contains element
    def contains(self, obj):
        return self.index_of(obj) != -1

    # Print array
    def __str__(self):

        if self.length == 0:
            return "[]"

        result = "["

        for i in range(self.length - 1):
            result += str(self.arr[i]) + ", "

        result += str(self.arr[self.length - 1]) + "]"

        return result
arr = DynamicArray()

n = int(input("How many elements to add: "))

for i in range(n):
    value = int(input("Enter element: "))
    arr.add(value)

print("\nArray =", arr)

remove_value = int(input("\nEnter value to remove: "))

if arr.remove(remove_value):
    print("Element removed successfully")
else:
    print("Element not found")

print("\nUpdated Array =", arr)

search_value = int(input("\nEnter value to search: "))

print("Contains =", arr.contains(search_value))
print("Index =", arr.index_of(search_value))