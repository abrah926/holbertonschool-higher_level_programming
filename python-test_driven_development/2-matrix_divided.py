def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given divisor.
    
    Args:
        matrix (list of lists): A matrix of integers or floats.
        div (int or float): The divisor.
    
    Returns:
        list: A new matrix with each element divided by div, rounded to 2 decimal places.
    
    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(ele, (int, float)) for ele in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(ele / div, 2) for ele in row] for row in matrix]
