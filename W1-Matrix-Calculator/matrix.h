#ifndef MATRIX_H
#define MATRIX_H

#include <vector>
#include "vector.h"

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
};

bool sizeEqual(const Matrix & m1, const Matrix & m2);

#endif