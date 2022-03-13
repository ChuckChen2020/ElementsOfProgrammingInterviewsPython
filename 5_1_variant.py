import random


def variant1_three_colors(A):
    # A comes in with three colors as its elements: 'r', 'w', 'b'.
    l, r = 0, len(A) - 1
    for i in range(len(A)):
        if A[i] == 'w':
            A[i], A[l] = A[l], A[i]
            l += 1
    for i in reversed(range(len(A))):
        if A[i] == 'r':
            A[i], A[r] = A[r], A[i]
            r -= 1
        elif A[i] == 'w':
            break


if __name__ == "__main__":
    A = random.choices(['r', 'w', 'b'], k=20)
    variant1_three_colors(A)
    print(A)
