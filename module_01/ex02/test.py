from vector import Vector

v1 = Vector(5)
print(v1.values)
print(v1.shape)
# print(v1.T())
# print(v1.T().shape)
# print(v1.T().T().values)
# print(v1.T().T().shape)
v2 = Vector((10, 15))
print(v2.values)
print(v2.shape)
v3 = Vector([[0., 3., 2., 7.]])
print(v3.values)
print(v3.shape)
v4 = Vector([[5.], [4.], [3.], [2.0]]).T()
print(v4.values)
print(v4.shape)

print(v1.dot(v2))

print(v1 + v2)

print(v3.dot(v4))

print(v3 + v4)

print(v3)
print(v3 * 4)
print(4 * v3)

print(v1)
print(v1 * 4)
print(4 * v1)
print('\n')

print(v3)
print(v3 / 4)
# print(v4 / v3)
# print(4 / v3)

print(v1)
print(v1 / 4)
# print(v2 / v1)
# print(4 / v1)
