#include <iostream>
#include <algorithm>
#include <stdexcept>
#include "Eigen/Dense"
#include "Eigen/LU"
#include "matrix.h"

using namespace std;

// Helpers ====================================================================================
Eigen::MatrixXd MtoEigenM(const Matrix &m) {
    Eigen::MatrixXd a(m.getRows(), m.getCols()); 
    vector<Vector> m1 = m.getEntries();
    for (size_t i = 0; i < m.getRows(); ++i) {
        for (size_t j = 0; j < m.getCols(); ++j) {
            a(i, j) = m1[i][j];
        }
    }
    return a;
}

Matrix eigenMtoM(const Eigen::MatrixXd &m) {
    vector<Vector> m3;
    for (size_t i = 0; i < m.rows(); ++i) {
        vector<double> vRow;
        for (size_t j = 0; j < m.cols(); ++j) {
            vRow.emplace_back(m(i, j));
        }
        m3.emplace_back(vRow);
    }
    Matrix a(m3);
    return a;
}
// ===========================================================================================

Matrix::Matrix(size_t n, size_t m) : entries(), n(n), m(m) {
    vector<Vector> entries;
    for (size_t i = 0; i < n; ++i) {
        cout << "Insert Vector for Row " << i << endl;
        Vector v(m);
        entries.emplace_back(v);
    }
    this->entries = entries;
}

Matrix::Matrix(vector<Vector> entries) : entries(entries), n(entries.size()), m(entries.empty() ? 0 : entries[0].getCols()) {}
Matrix::Matrix(const Matrix &other) : entries(other.entries), n(other.n), m(other.m) {}

bool Matrix::operator==(const Matrix &rhs) const {
    if (this->n != rhs.getRows()) return false;
    if (this->m != rhs.getCols()) return false;
    if (this->entries != rhs.getEntries()) return false;
    return true;
}
Matrix& Matrix::operator=(const Matrix &rhs) {
    if (*this == rhs) return *this;
    this->entries = rhs.getEntries();
    this->n = rhs.getRows();
    this->m = rhs.getCols();
    return *this;
}

Matrix Matrix::operator+(const Matrix & other) {
    if (!sizeEqual(*this, other)) throw std::invalid_argument("Matrices do not match sizes");
    vector<Vector> sum;
    vector<Vector> m1 = this->getEntries();
    vector<Vector> m2 = other.getEntries();
    for (size_t i = 0; i < this->n; ++i) {
        Vector v = m1[i] + m2[i];
        sum.emplace_back(v);
    }
    return sum;
}
Matrix& Matrix::operator+=(const Matrix & other) {
    if (!sizeEqual(*this, other)) throw std::invalid_argument("Matrices do not match sizes");
    vector<Vector> sum;
    vector<Vector> m1 = this->getEntries();
    vector<Vector> m2 = other.getEntries();
    for (size_t i = 0; i < this->n; ++i) {
        Vector v = m1[i] + m2[i];
        sum.emplace_back(v);
    }
    this->entries = sum;
    return *this;
}

// Currently Using Eigen (lib) I GOT SUPER LAZY WITH THIS ONE
// THIS IS ACTUALLY PRETTY EASY, I JUST DIDN'T FEEL LIKE DOING IT
// WHEN I STARTED DOING IT, WILL DO IN FUTURE RELEASE
Matrix Matrix::operator*(const Matrix & other) {
    if (this->getCols() != other.getRows()) throw std::invalid_argument("Matrices do not match sizes");
    // vector<Vector> entries;
    // for (size_t i = 0; i < other.getCols(); ++i) {
    //     vector<double> v;
    //     for (size_t j = 0; j < this->getRows(); ++j) {

    //     }
    //     Vector w(v);
    //     entries.emplace_back(w);
    // }

    Eigen::MatrixXd a = MtoEigenM(*this);
    Eigen::MatrixXd b = MtoEigenM(other);
    Eigen::MatrixXd c = a * b;
    return eigenMtoM(c);
}

Matrix operator*(const double c, const Matrix & m) {
    vector<Vector> product;
    vector<Vector> mEntries = m.getEntries();
    for (size_t i = 0; i < m.getRows(); ++i) {
        Vector v = c * mEntries[i];
        product.emplace_back(v);
    }
    Matrix sProduct(product);
    return sProduct;
}

void Matrix::transpose() {
    vector<Vector> m;
    vector<Vector> thisEntries = this->getEntries();
    for (size_t i = 0; i < this->getCols(); ++i) {
        vector<double> v;
        for (size_t j = 0; j < this->getRows(); ++j) {
            v.emplace_back(thisEntries[j][i]);
        }
        Vector vEntry(v);
        m.emplace_back(vEntry);
    }
    Matrix m1(m);
    this->n = this->getCols();
    this->m = this->getRows();
    this->entries = m;
}

// Currently Using Eigen (lib)
double Matrix::det() {
    if (!this->isSquare()) throw std::invalid_argument("Not Square Matrix");
    Eigen::MatrixXd a(this->getRows(), this->getCols()); 
    vector<Vector> v = this->getEntries();
    size_t n = this->getRows();
    for (size_t i = 0; i < n; ++i) {
        for (size_t j = 0; j < n; ++j) {
            a(i, j) = v[i][j];
        }
    }
    return a.determinant();
}

// Unfinished (This is Copilot Copied, I will implement this on my own once I start working on it again)
Matrix Matrix::rref() {
    Eigen::MatrixXd matrix = MtoEigenM(*this);
    int rows = matrix.rows();
    int cols = matrix.cols();
    int lead = 0;

    for (int r = 0; r < rows; ++r) {
        if (lead >= cols) {
            return eigenMtoM(matrix);
        }
        int i = r;
        while (matrix(i, lead) == 0) {
            ++i;
            if (i == rows) {
                i = r;
                ++lead;
                if (lead == cols) {
                    return eigenMtoM(matrix);
                }
            }
        }
        matrix.row(i).swap(matrix.row(r));
        if (matrix(r, lead) != 0) {
            matrix.row(r) /= matrix(r, lead);
        }
        for (int j = 0; j < rows; ++j) {
            if (j != r) {
                matrix.row(j) -= matrix.row(r) * matrix(j, lead);
            }
        }
        ++lead;
    }
    return eigenMtoM(matrix);
}

// Currently Using Eigen (lib)
Matrix Matrix::inverse() {
    if (!this->isSquare()) throw std::invalid_argument("Not Square Matrix");

    Eigen::MatrixXd a = MtoEigenM(*this);

    Eigen::FullPivLU<Eigen::MatrixXd> lu(a);
    bool invertible = lu.isInvertible();

    if (invertible) {
        Eigen::MatrixXd b = a.inverse();
        Matrix m = eigenMtoM(b);
        return m;
    } else {
        throw std::invalid_argument("Not Invertible");
    }
}

// Currently Using Eigen (lib)
void Matrix::eigen() {
    if (!this->isSquare()) throw std::invalid_argument("Not Square Matrix");

    Eigen::MatrixXd a = MtoEigenM(*this);
    Eigen::SelfAdjointEigenSolver<Eigen::MatrixXd> eigensolver(a);
    if (eigensolver.info() != Eigen::Success) abort();
    cout << "Eigenvalues are:\n" << eigensolver.eigenvalues() << endl;
    cout << "Column Eigenvectors are:\n" << eigensolver.eigenvectors() << endl;
}

// Currently Using Eigen (lib)
Vector Matrix::solve(const Vector &b) {
    if (this->getCols() != b.getCols()) throw std::invalid_argument("Matrix and Vector do not match sizes");
    Eigen::MatrixXd a = MtoEigenM(*this);

    vector<double> v1 = b.getEntries();
    Eigen::VectorXd v2(b.getCols());
    for (size_t i = 0; i < b.getCols(); ++i) {
        v2(i) = v1[i];
    }

    Eigen::VectorXd x = a.colPivHouseholderQr().solve(v2);

    vector<double> v3;
    for (size_t i = 0; i < b.getCols(); ++i) {
        v3.emplace_back(x(i));
    }
    Vector v(v3);
    return v;
}

void Matrix::print() {
    for (size_t i = 0; i < n; ++i) {
        this->entries[i].print();
    }
    cout << endl;
}
size_t Matrix::getRows() const {
    return this->n;
}
size_t Matrix::getCols() const {
    return this->m;
}
vector<Vector> Matrix::getEntries() const {
    return this->entries;
}
bool Matrix::isSquare() const {
    return (this->getCols() == this->getRows());
}

bool sizeEqual(const Matrix & m1, const Matrix & m2) {
    if (m1.getCols() != m2.getCols()) return false;
    if (m1.getRows() != m2.getRows()) return false;
    return true;
}

