# coding=utf-8

celsius = {39.2, 36.5, 37.3, 37.8}  # a set
a = [ ((float(9)/5)*x + 32) for x in celsius ]
print a

celsius = (39.2, 36.5, 37.3, 37.8) # a tuple
a = [ ((float(9)/5)*x + 32) for x in celsius ]
print a


celsius = [39.2, 36.5, 37.3, 37.8] # a list
a = [ ((float(9)/5)*x + 32) for x in celsius ]  # a list
print a

a = { ((float(9)/5)*x + 32) for x in celsius }  # a set
print a

a = ( ((float(9)/5)*x + 32) for x in celsius )  # a generator
print a.next()
print a.next()


# ------------------------------------------------------------------------------------------------------------------
a_list = [1, 4, 9, 0, 4]

squared_ints = [ e**2 for e in a_list ]

print(squared_ints)

a_list = [1, '4', 9, '0', 4]

# Dans cet exemple on retrouve le 3e morceau i.e. le predicat optionel, ici "isinstance(e, (int, float))"

squared_ints = [ e**2 for e in a_list if isinstance(e, (int, float)) ]

print(squared_ints)

# -------------------------------------------------------------------------------------------------------------------

#  it possible de "construire" une collection de collection autre que simple vecteur en exploitant les '[' ou '{'
# Dans l'exemple suivant une liste de listes

words = 'The quick brown fox jumps over the lazy dog'.split()

stuff_list_of_list = [[w.upper(), w.lower(), len(w)] for w in words]
print stuff_list_of_list

stuff_list_of_tuple = [(w.upper(), w.lower(), len(w)) for w in words]
print stuff_list_of_tuple

# -------------------------------------------------------------------------------------------------------------------

mcase = {'a':10, 'b': 34, 'A': 7, 'Z':3}
mcase_frequency = { k : mcase.get(k) * 2 for k in mcase.keys() }
print mcase_frequency

# {'b': 68, 'a': 20, 'A': 14, 'Z': 6}

# ou a partir d'un tuple - noter la presence de deux arguments dans la boucle

tup = [('a', 10), ('b', 34)]
dtup = { k : p for k,p in tup }
print dtup
# {'a': 10, 'b': 34}


# 2 ou 3 arguments dans l'iteration

paires = [(1,2), (2,3), (3,4)]
res = [(x,y,x*y) for x,y in paires]
print res

# Note une zip peut merger en paire deux listes

# 3 boucles for

liste1 = [1,2,3,4,5,6,7,8,9]
liste2 = [3,4,5,6,7]
liste3 = [4,5]

[x for x in liste1 for y in liste2 for z in liste3 if x == y and y == z]