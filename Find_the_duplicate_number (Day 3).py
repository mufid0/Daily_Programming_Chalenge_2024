def find_duplicate():
    arr = list(map(int, input("Enter the array elements separated by space: ").split()))
    tortoise = arr[0]
    hare = arr[0]
    while True:
        tortoise = arr[tortoise]
        hare = arr[arr[hare] % len(arr)]
        if tortoise == hare:
            break

    tortoise = arr[0]
    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[hare]
    print("The duplicate element is:", hare)

find_duplicate()
