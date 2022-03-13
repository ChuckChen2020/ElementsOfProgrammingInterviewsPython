import random


def dutch_flag_partition(pivot_index, A):
    l, r = 0, len(A) - 1
    pivot = A[pivot_index]
    p = 0
    while p < r:
        if A[p] < pivot:
            A[p], A[l] = A[l], A[p]
            l += 1
            # in this logic, we should move the pointers for small group after the swaps. But there's no gurantee that after the swapping, what the current pointer points to would be less than pivot. This means we shouldn't increment p yet. However, this leds to a possibility that p falls behind l, and we certainly won't wanna swap inside the small group. Thus, we take the max of two as the next p. This way p >= l is guranteed.
            p = max(p, l)
        elif A[p] > pivot:
            # This branch does not need a treatment like the above, since the condition p < r gurantees no swapping inside the large group.
            A[p], A[r] = A[r], A[p]
            r -= 1
        else:
            # if it's just equal to pivot, its place needs no adjustment. Simply move p forward.
            p += 1


def dfp_two_pass(pivot_index, A):
    pivot = A[pivot_index]
    l = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[l] = A[l], A[i]
            l += 1
    r = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] > pivot:
            A[i], A[r] = A[r], A[i]
            r -= 1
        # On the second pass, the smaller ones have been placed right already. If A[i] hits a value less than pivot, we can skip the rest.
        elif A[i] < pivot:
            break


if __name__ == '__main__':
    # random sample is a convenient tool to generate a random int list.
    randList1 = random.sample(range(10), 10)
    print(randList1)
    randList2 = list(randList1)
    dutch_flag_partition(5, randList1)
    dfp_two_pass(5, randList2)
    print(randList1)
    print(randList2)
