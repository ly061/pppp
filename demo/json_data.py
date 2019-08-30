from assertpy import assert_that
a = [1,2,3,["a","b","c"]]
b = a.copy()
b.append(4)
# assert a == b, "a is not equal to b"
assert_that(a).is_equal_to(b)