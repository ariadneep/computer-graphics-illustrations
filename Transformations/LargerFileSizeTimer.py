import math

import matplotlib.pyplot as plt
import numpy as np

x = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 150000, 160000, 170000, 180000, 190000, 200000]
y = [4565636.24, 7806000.0, 1.142588625E7, 1.450057167E7, 1.832150543E7, 2.403941375E7, 2.748847042E7, 3.139755292E7, 3.518564333E7, 3.955514875E7, 4.540423792E7, 7.023783541E7, 7.540846458E7, 8.011087042E7, 8.689370957E7, 9.265142876E7, 9.988656E7, 1.01706475E8, 1.0890125751E8, 1.1582897E8]

y2 = [4327099.17, 8106997.92, 1.123385833E7, 1.504114834E7, 1.892216875E7, 2.440132082E7, 2.813146626E7, 3.236273833E7, 3.747277958E7, 4.146403625E7, 4.627595334E7, 7.219487666E7, 7.596293375E7, 7.963023084E7, 8.515466125E7, 9.143971208E7, 9.667392041E7, 1.0436254834E8, 1.1201983875E8, 1.1948998709E8]
check_2 = [4327099.17/x[0], 8106997.92/x[1], 1.123385833E7/x[2], 1.504114834E7/x[3], 1.892216875E7/x[4], 2.440132082E7/x[5], 2.813146626E7/x[6], 3.236273833E7/x[7], 3.747277958E7/x[8], 4.146403625E7/x[9], 4.627595334E7/x[10], 7.219487666E7/x[11], 7.596293375E7/x[12], 7.963023084E7/x[13], 8.515466125E7/x[14], 9.143971208E7/x[15], 9.667392041E7/x[16], 1.0436254834E8/x[17], 1.1201983875E8/x[18], 1.1948998709E8/x[19]]

# Plot the results
plt.plot(x, y, label='large distinct - all', marker='o', linestyle='-')
plt.plot(x, y2, label='large distinct - one', marker='o', linestyle='-')
plt.plot(x, check_2, label='check analysis - linear - one', marker='o', linestyle='-')



# Add labels and title
plt.xlabel('Problem size (k)')
plt.ylabel('Time (nanoseconds)')
plt.title("Large File of Relatively Distinct Words: All vs One Runtime")

plt.legend()

desktop_path = "/Users/ariadnepetroulakis/Desktop/U of U/1. Freshman/Spring/CS 2420/Graphs/a11/"
filename = "a11_Q3_large-distinct.png"
plt.savefig(desktop_path + "/" + filename)

# Show the plot
plt.show()
