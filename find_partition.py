
def find_partition(numbers):
    """Separate given numbers into two series of equal sum.

    Args:
        numbers: an collection of numbers, for an example a list of integers.

    Returns:
        Two lists of numbers.
    """
    A = []
    B = []
    sum_A = 0
    sum_B = 0
    for n in sorted(numbers, reverse=True):
        if sum_A < sum_B:
           A.append(n)
           sum_A = sum_A + n
        else:
           B.append(n)
           sum_B = sum_B + n
    return (A, B)
