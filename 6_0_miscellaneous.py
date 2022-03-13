def is_palindromic(s):
    # -x = ~(x-1), 2's complement
    # e.g., x = 10, then ~(9)= ~(1001) = (111...0110)
    return all(s[i] == s[~i] for i in range(len(s) // 2))


if __name__ == '__main__':
    print(is_palindromic('abcdcba'))
    print('ab' in 'abcdef')
    string = '  xoxo love xoxo   '
    print(string.strip(' xoe'))
    string = "this is string example....wow!!!"
    print(string.startswith('this'))
    print(string.startswith('is', 2, 4))
    print(string.startswith('this', 2, 4))
    print(3*'01')
    print(','.join(('Gauss', 'Prince of Mathematicians', '1777-1855')))
    print('Name {name}, Rank {rank}'.format(name='Chuck', rank=5))
