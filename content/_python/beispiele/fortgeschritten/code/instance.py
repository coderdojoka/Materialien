import random

__author__ = 'Mark Weinreuter'

test = [1, 2]
if random.randint(0, 10) > 5:
    test = 42

test.append(3)  # funktioniert 50% der Zeit!


if isinstance(test, list):
    test.append(3)
else:
    print("Die Variable 'test' ist keine Liste!")


class A:
    def tu_was(self):
        print("Ich bin ein A")


class B(A):
    def tu_was(self):
        print("Ich bin ein B")


test = B()
print("test hat den typ: ", type(test))


if isinstance(test, A):
    test.tu_was()
else:
    print("Falscher Typ")
