from itertools import repeat
from operator import add, sub
from typing import NamedTuple


Infinity = float('inf')


class Point(NamedTuple):
    x: int
    y: int

    def _operation(self, other, op):
        def do_op(the_other):
            # Do you know what this is doing?
            return Point(*tuple(map(op, self, the_other)))

        if isinstance(other, Point):
            return do_op(other)
        elif isinstance(other, int):
            other = tuple(repeat(other, 2))
            return do_op(other)
        else:
            raise TypeError

    def __add__(self, other):
        return self._operation(other, add)

    def __sub__(self, other):
        return self._operation(other, sub)

    def __str__(self):
        return ""

    @property
    def real(self):
        """"Proxy due to silly use of complex type by svg.path"""
        return self.x

    @property
    def imag(self):
        """"Proxy due to silly use of complex type by svg.path"""
        return self.y

