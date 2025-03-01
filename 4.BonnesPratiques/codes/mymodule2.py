# -*- coding: utf-8 -*-
"""
This is a super module called mymodule.py
@author: arrivault
"""


def create_complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
        real -- the real part (default 0.0)
        imag -- the imaginary part (default 0.0)

    Returns:
        complex - real + imag*j

    Example:

    >>> a = create_complex(1,2)
    >>> print(a)
    (1+3j)
    """
    if imag == 0.0 and real == 0.0:
        return complex(0, 0)
    return complex(real, imag)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
