import random


def rightPropagate(x):
    # (01010000)2 - 1 = (01001111)2
    return (x & (x-1)) + (x ^ (x-1))


def modPowerOfTwo(x, y):
    # set bit in all y digits up.
    mask = (1 << y) - 1
    return x & mask


def isPowerOfTwo(x):
    # Only one set bit if it's a power of 2.
    return x & (x - 1) == 0


if __name__ == "__main__":
    integer = 4382986508964
    res = rightPropagate(integer)
    print(bin(integer), bin(res))

    integer1 = 43829865089640765900
    res1 = rightPropagate(integer1)
    print(bin(integer1), bin(res1))

    x = random.getrandbits(64)
    y = random.getrandbits(10)
    assert(modPowerOfTwo(x, y) == x % (2**y))

    print(isPowerOfTwo(128), isPowerOfTwo(65536),
          isPowerOfTwo(65535), isPowerOfTwo(36))
