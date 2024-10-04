Python
from your_file import pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__   
 == "__main__":
    n = 5
    triangle = pascal_triangle(n)
    print_triangle(triangle)
