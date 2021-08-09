# %%
import numpy as np
import numpy as nump
import matplotlib.pyplot as plt
msg = "hello world "
print(msg)


x = [3, 4, 6, 3, 4, 3, 8, 9, 7, 8, ]    # Create a list of numbers
plt.plot(x)       # Plot the sine of each x point
plt.show()


# %%

# Create a list of evenly-spaced numbers over the range
x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the plot
