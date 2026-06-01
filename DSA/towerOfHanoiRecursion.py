def towerOfHanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    towerOfHanoi(n-1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    towerOfHanoi(n-1, auxiliary, source, destination)
towerOfHanoi(4, "A", "B", "C")