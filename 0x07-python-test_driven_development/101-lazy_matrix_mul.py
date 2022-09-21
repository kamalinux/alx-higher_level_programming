#!/usr/bin/python3
"""
Module composed by a function that multiplies 2 matrices
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        result of the multiplication
    """

    return (np.matmul(m_a, m_b))
