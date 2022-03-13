def even_odd(A):
    pe, po = 0, len(A) - 1
    while pe < po:
        if A[pe] % 2 == 0:
            pe += 1
        else:
            # if it pe hits an odd, swap with the one at po. if this po bears 1) an even value, next round pe will move right and therefore skip to the next. 2) an odd value, then next round it will be swapped with the entry before current po. In both scenarios, the purpose will be achieved naturally.
            A[pe], A[po] = A[po], A[pe]
            po -= 1


if __name__ == '__main__':
    A = [9, 6, 3, 7, 4, 2, 1, 5, 8, 0]
    even_odd(A)
    print(A)
