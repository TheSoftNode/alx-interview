#!/usr/bin/env python3

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to a given number of rows.

    Args:
    - n: An integer specifying the number of rows of Pascal's triangle to generate.

    Returns:
    - A list of lists representing Pascal's triangle up to the nth row.
    """
    if n <= 0:
        return []

    # Initialize the result list with the first row
    res = [[1]]

    # Generate the subsequent rows
    for i in range(n - 1):
        # Create a temporary list with padding zeros on both sides
        temp = [0] + res[-1] + [0]
        row = []

        # Calculate the values for the current row
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j + 1])

        # Append the current row to the result
        res.append(row)

    return res

