# coding=utf-8
#
#  Arguments side effects


def changer(a, b):
    a= 2
    b[0] = 'spam'   # l'appelant sera modifie
    print "Inside: {} of type {}".format(b, type(b))

c = 88
li = [1,2,3]
changer(c, li)
print c, li

# - avoid mutable changes

c = 88
li = [1,2,3]
changer(c, li[:])
print c, li

#-------------------------------------------------------------------------------


def f(a, b, c):
    """ exploration sur print"""
    print(a, b, c)
    print a, b, c
    name = 'marie'
    print(name)
    print name
    print("{} {} {}".format(a,b,c))

f(c=3, b=2, a=1)


#-------------------------------------------------------------------------------

def f(*args):
    print "{} {} {}".format(args, len(args), type(args))

f(1, 2, 3)

# at least one argument

def test_var_args(f_arg, *argv):
    print "first normal arg:", f_arg
    for arg in argv:
        print "another arg through *argv :", arg

test_var_args('yasoob','python','eggs','test')
test_var_args('yasoob')

# ------------------------------------------------------------------------------

def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.iteritems():
            print "%s == %s" %(key,value)

greet_me(name="yasoob", a=1)


def test_order_args(f_arg, *argv, **kwargs):
    print "first normal arg:", f_arg
    for arg in argv:
        print "another arg through *argv :", arg
    if kwargs is not None:
        for key, value in kwargs.iteritems():
            print "%s == %s" %(key,value)

test_order_args(1, (1, 2, 3), a=1, b=2, c=3)

# ------------------------------------------------------------------------------

seq1 = (1, 2, 3)
seq2 = (4, 5, 6)
zip(seq1, seq2)

{x+y for x,y in zip(seq1, seq2)}