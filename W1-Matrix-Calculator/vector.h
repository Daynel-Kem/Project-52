#ifndef VECTOR_H
#define VECTOR_H
#include <vector>

using namespace std;

/*

    A Vector Class that holds up to n entries
    The Functionality of this class is listed below:
        - Vector Addition
        - Scalar Multiplication
        - Dot Product

    There are a few utility functions such as
        - print()
        - getRows()
        - getEntries()
    These can be used for 

*/
class Vector {
    vector<double> entries;
    size_t n;

    public:
        Vector(size_t n);
        Vector(const vector<double> vector);
        Vector(const Vector &rhs);

        void print();
        Vector operator+(const Vector &other);
        Vector& operator+=(const Vector &other);

        friend Vector operator*(const double c, const Vector & m);
        friend Vector operator*(const Vector & m, const double c);

        size_t getRows() const;
        vector<double> getEntries() const;

        ~Vector();
};

double dotProduct(const Vector & v1, const Vector & v2);

#endif