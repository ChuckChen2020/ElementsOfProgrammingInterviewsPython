import random
from time import perf_counter


def parity(x):
    result = 0
    while x:
        result ^= (x & 1)
        x >>= 1
    return result

# x & (x-1) removes the lowest set bit (bit with 1 to the rightmost) of x.
# e.g., (00101100)2 % (00101011)2 = (00101000)2,
# This avoids going through 0-valued bits thus reduces number of iterations.


def parityRemoveLowestSetBit(x):
    result = 0
    while x:
        result ^= 1
        x &= (x-1)
    return result


PRECOMPUTED_PARITY = [parityRemoveLowestSetBit(
    x) for x in range(0, 0xFFFF + 1)]


def parityCaching(x):
    # x is 64 bits. Precompute parity for all possible 16 bits, cahche the result.
    MASK_SIZE = 16
    # 16 bits of one to take only the last 16 bits.
    BIT_MASK = 0xFFFF
    # O(4) for this, and less than O(16) for precomputation.
    return (PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)] ^
            PRECOMPUTED_PARITY[x >> (2 * MASK_SIZE) & BIT_MASK] ^ PRECOMPUTED_PARITY[x >> MASK_SIZE & BIT_MASK] ^
            PRECOMPUTED_PARITY[x & BIT_MASK])

# The parity (奇偶性) of a "word" is the same as the first half XOR the second half,
# because: (a1,a2,..., a32) ^ (b1, b2, ..., b32) on each bit i the value would be 1 only when {ai, bi} = {0, 1}. In other words, ai ^ bi has the same parity as (ai, b1). The same applies for all bits.
# So to compute the parity of 64 bit, we can xor the first 32 bits with the last 32 bits, whatever the result, we xor its first 16 with the last 16, ....


def parityWordXor(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    # Note the x in the last will have all the 64 digits. But the rightmost one is the only one that matters and should be extracted.
    return x & 0x1


if __name__ == "__main__":
    TIME = 64
    randIntArray = [random.getrandbits(64) for _ in range(TIME)]

    t1 = perf_counter()
    res1 = list(map(parity, randIntArray))
    t2 = perf_counter()
    res2 = list(map(parityRemoveLowestSetBit, randIntArray))
    t3 = perf_counter()
    res3 = list(map(parityCaching, randIntArray))
    t4 = perf_counter()
    res4 = list(map(parityWordXor, randIntArray))
    t5 = perf_counter()
    assert(res1 == res2 == res3 == res4)
    print(t2 - t1, t3 - t2, t4 - t3, t5 - t4)
