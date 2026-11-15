import numpy
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    n = len(a)
    m = len(a[0])
    ans = numpy.zeros((m,n))

    for i in range(n):
        for j in range(m):
            ans[j][i] = a[i][j]
    return ans
    # Your code here
    pass