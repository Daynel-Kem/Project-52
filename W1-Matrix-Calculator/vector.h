#ifndef VECTOR_H
#define VECTOR_H
#include <vector>

using namespace std;

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
};

double dotProduct(const Vector & v1, const Vector & v2);

#endif