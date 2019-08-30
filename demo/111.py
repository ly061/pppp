class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    @staticmethod
    def fizzBuzz(s,t):
        li = []
        kk = 1
        for i in s:
            if i not in li:
                li.append(i)
        for j in li:
            if (s.count(j) - t.count(j)) > 1:
                kk *= (s.count(j) - t.count(j))
        return kk
print(Solution.fizzBuzz("rabbbit","rabbit"))