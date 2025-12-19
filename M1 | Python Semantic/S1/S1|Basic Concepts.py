# Basic type declaration
x = 5

print(type(x))
print(id(x))
print(x)
print(dir(x))

# Mutability vs Immutability
lst = [1, 2, 3]
print(id(lst))

lst.append(5)
print(id(lst))


a = 4
print(id(a))

a *= 2
print(id(a))

# Type Annotations
def func(_) -> None:
    ...

age: int = 10
name: str = 12