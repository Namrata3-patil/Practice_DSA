def countSwaps(a):
    numSwaps = 0
    n = len(a)
    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                # Swap adjacent elements
                a[j], a[j + 1] = a[j + 1], a[j]
                numSwaps += 1

    print(f"Array is sorted in {numSwaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[n - 1]}")
