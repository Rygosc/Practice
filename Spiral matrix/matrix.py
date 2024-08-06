def create_spiral_matrix(n, m):
    """
    Create an n x m matrix filled with numbers from 1 to n*m in a spiral pattern.

    Args:
    n (int): Number of rows.
    m (int): Number of columns.

    Returns:
    list: A 2D list representing the spiral matrix.
    """
    if n <= 0 or m <= 0:
        raise ValueError("Number of rows and columns must be positive integers.")

    matrix = [[0] * m for _ in range(n)]
    numbers = list(range(1, n * m + 1))

    top, bottom = 0, n - 1
    left, right = 0, m - 1

    while numbers:
        # Move right
        for i in range(left, right + 1):
            if not numbers:
                break
            matrix[top][i] = numbers.pop(0)
        top += 1

        # Move down
        for i in range(top, bottom + 1):
            if not numbers:
                break
            matrix[i][right] = numbers.pop(0)
        right -= 1

        # Move left
        for i in range(right, left - 1, -1):
            if not numbers:
                break
            matrix[bottom][i] = numbers.pop(0)
        bottom -= 1

        # Move up
        for i in range(bottom, top - 1, -1):
            if not numbers:
                break
            matrix[i][left] = numbers.pop(0)
        left += 1

    return matrix

def print_matrix(matrix):
    """
    Print the matrix in a readable format.

    Args:
    matrix (list): The 2D list representing the matrix.
    """
    for row in matrix:
        print(" ".join(str(cell).ljust(3) for cell in row))

if __name__ == "__main__":
    try:
        n, m = map(int, input("Enter the number of rows and columns (separated by space): ").split())
        spiral_matrix = create_spiral_matrix(n, m)
        print_matrix(spiral_matrix)
    except ValueError as e:
        print(f"Error: {e}")
