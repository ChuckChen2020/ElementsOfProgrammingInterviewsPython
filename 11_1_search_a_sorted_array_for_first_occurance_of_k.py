import bisect


def search_first_of_k(A, k):
    l, r = 0, len(A) - 1
    while l < r:
        m = l + (r - l) // 2
        if k > A[m]:
            l = m + 1
        elif k < A[m]:
            r = m - 1
        else:
            n = m - 1
            while A[n] == k:
                n -= 1
            n += 1
            return n
    return -1


def search_first_of_k_ii(A, k):
    left, right, result = 0, len(A) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result


def search_first_of_k_iii(A, k):
    ind = bisect.bisect_left(A, k)
    return ind if A[ind] == k else -1


if __name__ == '__main__':
    A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    print(search_first_of_k(A, 108))
    print(search_first_of_k(A, 285))
    print(search_first_of_k_ii(A, 108))
    print(search_first_of_k_ii(A, 285))
    print(search_first_of_k_iii(A, 108))
    print(search_first_of_k_iii(A, 285))
