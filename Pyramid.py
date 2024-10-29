def pyramid_descent(pyramid, target):
    def dfs(row, col, product, path):
        # Base case: if we've reached the last row
        if row == len(pyramid) - 1:
            if product == target:
                return path  # Solution found
            return None  # Dead-end path

        # Calculate new products for left and right descent
        left_path = dfs(row + 1, col, product * pyramid[row + 1][col], path + "L")
        right_path = dfs(row + 1, col + 1, product * pyramid[row + 1][col + 1], path + "R")

        # Return whichever path meets the target
        return left_path if left_path else right_path

    # Start from the top of the pyramid
    return dfs(0, 0, pyramid[0][0], "")

# Example usage
pyramid = [
    [2],
    [4, 3],
    [3, 2, 6],
    [2, 9, 5, 2],
    [10, 5, 2, 15, 5]
]
target = 720

solution = pyramid_descent(pyramid, target)
print(f"Path to target: {solution}")
