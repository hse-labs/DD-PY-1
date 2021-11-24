from enum import Enum


class A(Enum):
    a = 1


class B(Enum):
    b = 2


class C(A, B):
    ...


print(C)
