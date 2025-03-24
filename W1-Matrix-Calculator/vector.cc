#include <vector>
#include <iostream>
#include "vector.h"

using namespace std;

Vector::Vector(size_t n) : entries(), n(n) {
    vector<double> entries;
    for (int i = 0; i < n; ++i) {
        double entry;
        cout << "Please enter a number: ";
        cin >> entry;
        entries.emplace_back(entry);
    }
    this->entries = entries;
}
Vector::Vector(const vector<double> vector) : entries(vector), n(vector.size()) {}
Vector::Vector(const Vector &rhs) : entries(rhs.entries), n(rhs.n) {}

bool Vector::operator==(const Vector & rhs) {
    if (this->entries != rhs.getEntries()) return false;
    if (this->n != rhs.getRows()) return false;
    return true;
}

Vector& Vector::operator=(const Vector & rhs) {
    if (*this == rhs) return *this;
    this->n = rhs.getRows();
    this->entries = rhs.getEntries();
    return *this;
}

void Vector::print() {
    // Iterates through the entries of the Vector and prints them
    for (vector<double>::iterator it = this->entries.begin(); it != this->entries.end(); ++it) {
        cout << "[ " << *it << " ]" << endl;
    }
    cout << endl;
}

Vector Vector::operator+(const Vector &other) {
    vector<double> sum;
    vector<double> v1 = this->getEntries();
    vector<double> v2 = other.getEntries();
    for (size_t i = 0; i < v1.size(); ++i) {
        sum.emplace_back(v1[i] + v2[i]);
    }
    Vector w(sum);
    return w;
}

Vector& Vector::operator+=(const Vector &other) {
    vector<double> sum;
    vector<double> v1 = this->getEntries();
    vector<double> v2 = other.getEntries();
    for (size_t i = 0; i < v1.size(); ++i) {
        sum.emplace_back(v1[i] + v2[i]);
    }
    this->entries = sum;
    return *this;
}

Vector operator*(const double c, const Vector & m) {
    vector<double> product;
    vector<double> mEntries = m.getEntries();
    for (size_t i = 0; i < m.n; ++i) {
        product.emplace_back(mEntries[i] * c);
    }
    Vector v(product);
    return v;
}

Vector operator*(const Vector & m, const double c) {
    vector<double> product;
    vector<double> mEntries = m.getEntries();
    for (size_t i = 0; i < m.n; ++i) {
        product.emplace_back(mEntries[i] * c);
    }
    Vector v(product);
    return v;
}


size_t Vector::getRows() const {
    return this->n;
}

vector<double> Vector::getEntries() const {
    return this->entries;
}

Vector::~Vector() {}

double dotProduct(const Vector & v1, const Vector & v2) {
    if (v1.getRows() != v2.getRows()) {
        return 0;
    }

    double product = 0;
    vector<double> v1Entries = v1.getEntries();
    vector<double> v2Entries = v2.getEntries();
    for (size_t i = 0; i < v1.getRows(); ++i) {
        product += v1Entries[i] * v2Entries[i];
    }
    return product;
}