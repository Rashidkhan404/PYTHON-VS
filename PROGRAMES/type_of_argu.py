def add(*numbers):  # tupple(1, 2, 3)
#  orbitrary arguments
#  it except only orbitrary positional arguments
#  NOt keyword arguments
    c = 0
    for i in numbers:
        c = c + i
    print(f"SUM IS {c}")


add(1, 2, 3)
add(2, 3, 4)
