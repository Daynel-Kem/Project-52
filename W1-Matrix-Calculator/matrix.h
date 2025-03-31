#ifndef MATRIX_H
#define MATRIX_H

#include <vector>
#include "vector.h"

/*

    A Matrix Class that can perform simple Linear Algebra Operatrions
    The Functionality of this class is listed below:
        - Matrix Addition
        - Scalar Multiplication
        - Matrix Multiplication
        - Tranpose
        - Determinant
        - Row Reduced Echelon Form (RREF)
        - Inverse
        - Solve Ax = b
        - Eigenvalues & Eigenvectors

    As usual with Matrices, some functions are specific to certain types of Matrices
    Square Matrices:
        - Determinant
        - Inverse (Limited up to 4x4 matrices for now)
        - Eigenvalues & Eigenvectors
    
    Same Size:
        - Matrix Addition

    Matrix a columns = Matrix b rows:
        - Matrix Multiplcation
        - Solve Ax = b

    There are a few utility functions such as
        - print()
        - getRows()
        - getCols()
        - getEntries()
        - isSquare()

*/

class Matrix {
    std::vector<Vector> entries;
    size_t n; // number of Rows
    size_t m; // number of Cols
 
    public:
        // Constructors
        Matrix(size_t n, size_t m);
        Matrix(vector<Vector> entries);
        Matrix(const Matrix &other);

        bool operator==(const Matrix &rhs) const;
        Matrix& operator=(const Matrix &rhs);

        Matrix operator+(const Matrix & other);
        Matrix& operator+=(const Matrix & other);

        Matrix operator*(const Matrix & other);

        friend Matrix operator*(const double c, const Matrix & m);

        void transpose();
        double det();
        Matrix rref();
        Matrix inverse();
        Vector solve(const Vector &b);

        void eigen();

        void print();
        size_t getRows() const;
        size_t getCols() const;
        vector<Vector> getEntries() const;
        bool isSquare() const;

        ~Matrix();
};

#endif