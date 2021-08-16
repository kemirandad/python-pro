import random

my_set1 = set(random.sample([ x for x in range(10)],5))
my_set2 = set(random.sample([ x for x in range(10)],5))

for m, n in zip(my_set1, my_set2):
    print(m, ':::', n)

my_set3 = my_set1.intersection(my_set2)
# You can also use the option '&'
print('\nIntersection --->', my_set3)

my_set4 = my_set1.union(my_set2)
# You can also use the option '|'
print('\nUnion --->', my_set4)

my_set5 = my_set1.symmetric_difference(my_set2)
# You can also use the option '^'
print('\nSymmetric difference --->', my_set5)

my_set6 = my_set1.difference(my_set2)
# You can also use the option '-'
print('\nA - B --->', my_set6)

my_set7 = my_set2.difference(my_set1)
# You can also use the option '-'
print('\nB - A -->',my_set7 )