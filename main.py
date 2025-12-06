#1-misol
matn = input('Biror-bir mant kiriting: ')

for i in range(len(matn)):
    print(f'{i+1}-{matn[i]}')

#2-misol
ism = input('Ism kiriting: ')

if len(ism) <= 2:
    print(ism)
else:
    birinchi = ism[0]
    oradagi = 'x' * (len(ism)-2)
    oxirgisi = ism[-1]

    print(birinchi + oradagi + oxirgisi)

#3-misol
my_tuple = ('a', 'b', 'c', 'd')
new = []

for i in range(len(my_tuple)):
    new += ((i, my_tuple[i]),)

print(tuple(new))

#4-misol
my_tuple = ('apple', 'banana', 'ok')
new = list(my_tuple)
new_tuple = ()

for i in new:
    new2 = i[::-1]
    new_tuple += (new2,)

print(new_tuple)
