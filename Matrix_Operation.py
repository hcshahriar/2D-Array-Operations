"""
2D Array/Matrix Operations
A collection of useful matrix operations with examples
"""

import numpy as np  
from typing import List, Tuple
import matplotlib.pyplot as plt

class MatrixOperations:
    """Class containing various 2D array operations"""
    
    @staticmethod
    def create_matrix(rows: int, cols: int, default_value=0) -> List[List[int]]:
        """Create a matrix with given dimensions filled with default value"""
        return [[default_value for _ in range(cols)] for _ in range(rows)]
    
    @staticmethod
    def print_matrix(matrix: List[List]) -> None:
        """Pretty print a matrix"""
        for row in matrix:
            print(" ".join(str(x).rjust(3) for x in row))
        print()
    
    @staticmethod
    def transpose(matrix: List[List]) -> List[List]:
        """Return the transpose of a matrix"""
        return [list(row) for row in zip(*matrix)]
    
    @staticmethod
    def add_matrices(a: List[List], b: List[List]) -> List[List]:
        """Add two matrices element-wise"""
        if len(a) != len(b) or len(a[0]) != len(b[0]):
            raise ValueError("Matrices must have the same dimensions")
        return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
    
    @staticmethod
    def multiply_matrices(a: List[List], b: List[List]) -> List[List]:
        """Multiply two matrices"""
        if len(a[0]) != len(b):
            raise ValueError("Number of columns in A must match rows in B")
        return [[sum(a[i][k] * b[k][j] for k in range(len(b))) 
                for j in range(len(b[0]))] for i in range(len(a))]
    
    @staticmethod
    def rotate_90_clockwise(matrix: List[List]) -> List[List]:
        """Rotate matrix 90 degrees clockwise"""
        return [list(row[::-1]) for row in zip(*matrix)]
    
    @staticmethod
    def save_to_file(matrix: List[List], filename: str) -> None:
        """Save matrix to a text file"""
        with open(filename, 'w') as f:
            for row in matrix:
                f.write(" ".join(map(str, row)) + "\n")
    
    @staticmethod
    def load_from_file(filename: str) -> List[List[int]]:
        """Load matrix from a text file"""
        with open(filename, 'r') as f:
            return [[int(num) for num in line.split()] for line in f]
    
    @staticmethod
    def visualize_matrix(matrix: List[List], title: str = "Matrix Visualization") -> None:
        """Visualize matrix using matplotlib"""
        plt.imshow(matrix, cmap='viridis')
        plt.colorbar()
        plt.title(title)
        plt.show()

def example_usage():
    """Demonstrate usage of the MatrixOperations class"""
    print("=== 2D Array Operations Example ===")
   
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    
    print("Matrix A:")
    MatrixOperations.print_matrix(A)
    
    print("Matrix B:")
    MatrixOperations.print_matrix(B)
    
    print("A + B:")
    MatrixOperations.print_matrix(MatrixOperations.add_matrices(A, B))
    
    print("A * B:")
    MatrixOperations.print_matrix(MatrixOperations.multiply_matrices(A, B))
    
    print("Transpose of A:")
    MatrixOperations.print_matrix(MatrixOperations.transpose(A))
    
    print("Rotate A 90° clockwise:")
    MatrixOperations.print_matrix(MatrixOperations.rotate_90_clockwise(A))
   
    MatrixOperations.save_to_file(A, "matrix.txt")
    loaded = MatrixOperations.load_from_file("matrix.txt")
    print("Loaded from file:")
    MatrixOperations.print_matrix(loaded)
   
    MatrixOperations.visualize_matrix(A, "Matrix A Visualization")

if __name__ == "__main__":
    example_usage()
