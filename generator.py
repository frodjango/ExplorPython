# coding=utf-8

# A propos du yield: yield is a keyword that is used like return, except the function will return a generator.
# savament positionne

'''
The performance improvement from the use of generators is the result of the lazy (on demand) generation of values,
which translates to lower memory usage. Furthermore, we do not need to wait until all the elements have been generated
before we start to use them. This is similar to the benefits provided by iterators, but the generator makes building
iterators easy.
'''

def fib():
    a, b = 0, 1
    while True:
        (yield b)
        a, b = b, a + b

# version pythonic
it = fib()

print next(it)
print next(it)
print next(it)