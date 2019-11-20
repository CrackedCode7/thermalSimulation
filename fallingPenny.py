# find the velocity of a falling penny given a certain height above the ground

# import functions from the modsim library

from modsim import *

''' Simple calculations with accelation, velocity, and position, and intro to units '''

meter = UNITS.meter # define meter units
second = UNITS.second # define second units

a = 9.8 * meter / second ** 2 # define accleration
t = 4 * second # set time

print(a * t**2 / 2, 'is the distance fallen after {}'.format(t)) # distance fallen calculation with constant acceleration

vel = a * t # velocity after 4 seconds
print(vel)

''' Solving the falling penny problem '''

h = 381 * meter # define height
t = sqrt(2 * h / a) #c alcualte time to fall to the ground
v = a * t # calculate velocity
print(v)

mile = UNITS.mile # define mile units
hour= UNITS.hour # define hour units

v.to(mile/hour) # convert the units of velocity to mile per hour

''' Exercise: In reality, air resistance limits the velocity of the penny. At about 18 m/s, the force of air resistance equals the force of gravity and the penny stops accelerating.

As a simplification, let's assume that the acceleration of the penny is a until the penny reaches 18 m/s, and then 0 afterwards. What is the total time for the penny to fall 381 m?

You can break this question into three parts:

    How long until the penny reaches 18 m/s with constant acceleration a.
    How far would the penny fall during that time?
    How long to fall the remaining distance with constant velocity 18 m/s?

Suggestion: Assign each intermediate result to a variable with a meaningful name. And assign units to all quantities! '''

t_terminal = (18 * meter / second) / a # find time to reach terminal velocity
print(t_terminal)

dist_fallen = (a * t_terminal**2 / 2) # distance travled up until terminal velocity reached
print(dist_fallen)

rem_dist = h-dist_fallen # calculate the remaining distance to fall once terminal velocity is reached
print(rem_dist)

time_rem = rem_dist / (18 * meter / second) # calcualte remaining time to fall after terminal velocity is reached
print(time_rem)

total_time_to_fall = t_terminal + time_rem
print(total_time_to_fall,'is the final answer')