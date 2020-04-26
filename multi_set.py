
import numpy as np
from random import randint


class MultiSet:
    """Generate multiset of random integers in given range.

    Args:
        s_num: number of elements in output set
        s_max: maximal value of multiset element
        s_min: minimal value of multiset element 

    Returns:
        Multiset of random numbers.
    """

    def __init__(self, s_num, s_max, s_min=1):
        self.set = [randint(s_min, s_max) for _ in range(s_num)]

    def __str__(self):
        return ", ".join(str(i) for i in self.set)

    def find_greedy_partition(self):
        """Separate given numbers into two series of equal sum.

        Args:
            self.set: an collection of numbers based on MultiSet object definition.

        Returns:
            Two lists of partitioned set and difference in both partitions in single tuple.
        """
        A = []
        B = []
        sum_A = 0
        sum_B = 0

        for n in sorted(self.set, reverse=True):
            if sum_A < sum_B:
                A.append(n)
                sum_A = sum_A + n
            else:
                B.append(n)
                sum_B = sum_B + n

        return (A, B, abs(sum_A - sum_B))

    def find_partition(self):

        n = len(self.set)
        K = sum(self.set)

        row = int(K/2 + 1)
        col = n + 1

        P = np.zeros((row, col))
        P[0] = 1

        for (i, j), _ in np.ndenumerate(P):

            if i != 0 and j != 0:

                if i+1 - self.set[j-1] >= 0:
                    P[i][j] = P[i][j-1] or P[i-self.set[j-1]][j-1]
                else:
                    P[i][j] = P[i][j-1]

        return P


def unit_test():

    test = MultiSet(5, 5)

    # print("Generated set: [{}]".format(test))

    # a, b, diff = test.find_greedy_partition()

    # print("a = {}\nsum(a) = {}\n|a| = {}".format(a, sum(a), len(a)))
    # print("b = {}\nsum(b) = {}\n|b| = {}".format(b, sum(b), len(b)))
    # print("diff = {}".format(diff))

    test.set = [3, 1, 1, 2, 2, 1]
    print("Generated set: [{}]".format(test))

    print(test.find_partition())


if __name__ == "__main__":
    unit_test()
