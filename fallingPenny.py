# find the velocity of a falling penny given a certain height above the ground

from modsim import sqrt

a = 9.8

h = 381
t = sqrt(2 * h / a)
v = a * t
print(v)