A = [1,2,3,4,5]
B = [6,7,8,9,10]
print('A ->',A)
print('B ->',B)
A.extend(B) # igual a A += B
print('A ->',A)
A.insert(0,23)
print('A ->',A)
