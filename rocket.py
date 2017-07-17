from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt


x = [-40, -20, 0, 20, 40, 60, 80]
y = [65.33333333,130, 383.6666667, 642.6666667, 717.6666667, 626, 365.3333333]

result = np.polyfit(x, y, 4)
eq = np.poly1d(result)
print (eq)

plt.plot(x, y, label = "Rocket Data")
plt.show()
plt.savefig("rocket_graph.png")

angle = raw_input("Enter an angle: ")
number = 0

while angle != "":
    if angle.isalpha():
        print ("Invalid angle")
        angle = raw_input("Enter an angle: ")
    else:
        try:
            number = float(angle)
        except ValueError:
            print ("exception")
        print (eq(number))
        angle = raw_input("Enter an angle: ")