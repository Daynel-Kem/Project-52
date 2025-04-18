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
        - getCols()
        - getEntries()

    The Vectors are stored as Row Vectors, Not Column Vectors

*/
class Vector {
    vector<double> entries;
    size_t n;

    public:
        // Constructors
        Vector(size_t n); // Default - Creates a Vector with n slots and asks for n numbers in the terminal
        Vector(const vector<double> vector); // Takes a vector<double> and converts it into a Vector
        Vector(const Vector &rhs); // Copy Constructor

        // Equality Operator
        bool operator==(const Vector & rhs) const;
        // Copy Assignment Operator
        Vector& operator=(const Vector & rhs);

        // Vector Addition
        Vector operator+(const Vector &other);
        Vector& operator+=(const Vector &other);
        // Scalar Multiplication
        friend Vector operator*(const double c, const Vector & m);
        friend Vector operator*(const Vector & m, const double c);

        // Utility Functions
        void print();
        size_t getCols() const;
        vector<double> getEntries() const;
        double operator[](size_t i);

        // Destructor
        ~Vector();
};

// Dot Product
double dotProduct(const Vector & v1, const Vector & v2);

#endif