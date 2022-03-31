# Python3 program to find
# maximum height of arranged
# coin triangle

# Returns the square root of n.
# Note that the function
def squareRoot(n):
    # We are using n itself as
    # initial approximation
    # This can definitely be improved
    x = n
    y = 1

    e = 0.000001  # e decides the accuracy level
    while (x - y > e):
        x = (x + y) / 2
        y = n / x

    return x


# Method to find maximum height
# of arrangement of coins
def findMaximumHeight(N):
    # calculating portion inside the square root
    n = 1 + 8 * N
    maxH = (-1 + squareRoot(n)) / 2
    return int(maxH)


# Driver code to test above method
N = 12
print(findMaximumHeight(N))

# This code is contributed by
# Smitha Dinesh Semwal
