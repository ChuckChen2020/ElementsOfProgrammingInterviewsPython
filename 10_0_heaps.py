import itertools
import heapq
from io import StringIO


def top_k(k, stream):
    min_heap = [(len(s), s) for s in itertools.islice(stream, k)]
    print(min_heap)
    heapq.heapify(min_heap)
    for next_string in stream:
        heapq.heappushpop(min_heap, (len(next_string), next_string))
    return [p[1] for p in heapq.nsmallest(k, min_heap)]


if __name__ == '__main__':
    Stream = StringIO("abc\ndefg\nhijklm\nno\np\nqrstuv\nwxy\nz")
    print(top_k(3, Stream))
