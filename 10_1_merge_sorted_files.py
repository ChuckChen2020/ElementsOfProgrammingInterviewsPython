import heapq
from functools import reduce


def merge_sorted_arrays(sorted_arrays):
    result = []
    min_heap = [(array[0], row, 0) for row, array in enumerate(sorted_arrays)]
    heapq.heapify(min_heap)

    while min_heap:
        val, row, col = heapq.heappop(min_heap)
        if col < len(sorted_arrays[row]) - 1:
            heapq.heappush(
                min_heap, (sorted_arrays[row][col + 1], row, col + 1))
        result.append(val)
    return result


def merge_sorted_arrays_ii(sorted_arrays):
    min_heap = []
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]
    for i, it in enumerate(sorted_arrays_iters):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    result = []
    while min_heap:
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        smallest_array_iter = sorted_arrays_iters[smallest_array_i]
        result.append(smallest_entry)
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_i))
    return result


def merge_sorted_arrays_pythonic(sorted_arrays):
    return list(heapq.merge(*sorted_arrays))


if __name__ == '__main__':
    arrays = [[3, 5, 7], [0, 6], [0, 6, 28]]
    print(merge_sorted_arrays(arrays))
