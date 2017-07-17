from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt

# lists containing data points
x = [-40, -20, 0, 20, 40, 60, 80]
y = [65.33333333,130, 383.6666667, 642.6666667, 717.6666667, 626, 365.3333333]

# creates the equation using data points above
result = np.polyfit(x, y, 4)
eq = np.poly1d(result)
print (eq)

# creates and saves a graph from the equation
plt.plot(x, y, label = "Rocket Data")
plt.show()
plt.savefig("rocket_graph.png")

# asks for an angle
angle = raw_input("Enter an angle: ")
number = 0

# keeps asking user for an angle
while angle != "":
    # tests if angle is invalid(letters)
    if angle.isalpha():
        print ("Invalid angle")
        angle = raw_input("Enter an angle: ")
    else:
        # plugs angle into equation and prints result
        try:
            number = float(angle)
        except ValueError:
            print ("exception")
        print (eq(number))
        angle = raw_input("Enter an angle: ")