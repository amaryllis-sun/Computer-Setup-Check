from math import pow as power
from math import sqrt as square_root
from random import randint as probability 
from random import shuffle as shfl
from random import choice as pick


result_1 = power(2,4)
print("result_1 is", result_1)

result_2 = square_root(16)
print("result_2 is", result_2)


result_3 = probability(0,100)
print("result_3 is", result_3)

names = ["Amaryllis", "Godson", "Emily","Reina", "Derin", "Elena", "Inacio"]
print("Original names: ", names)

shfl(names)
print("Names after shuffling: ", names)

result_4 = pick(names)
print("Chosen name is: ", result_4)