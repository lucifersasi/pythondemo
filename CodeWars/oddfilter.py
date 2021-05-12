def find_it(seq):
    flag = 0

    for pivot in seq:
        for iter in seq:
            if pivot == iter:
                flag += 1
        if flag % 2 != 0:
            return pivot


def find_odd(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


print(find_odd([20, 1, -1, 2, -2, 3, 3, 3, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
# test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
