Python
def pascal_triangle(n):
  """
  This function generates Pascal's Triangle up to level n.

  Args:
      n: An integer representing the desired level of the triangle.

  Returns:
      A list of lists containing the elements of Pascal's Triangle.
      Returns an empty list if n <= 0.
  """
  if n <= 0:
    return []

  triangle = [[1]]

  # Loop for rows (excluding first row)
  for i in range(1, n):
    prev_row = triangle[i-1]
    new_row = [1]  # Start with 1
    for j in range(1, len(prev_row)):
      new_row.append(prev_row[j-1] + prev_row[j])  # Sum elements
    new_row.append(1)  # End with 1
    triangle.append(new_row)

  return triangle
