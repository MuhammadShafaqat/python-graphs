import matplotlib.pyplot as plt

# Generate x values from -10 to 10
x = list(range(-10, 11))

# Compute squares of x values to get y values (x^2)
y = [val ** 2 for val in x]

# Plotting the graph
plt.plot(x, y, marker='o')  # 'marker' is optional; it adds markers at data points for better visibility

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph of x^2')

# Display the graph
plt.grid()  # Add a grid for better visualization (optional)
plt.axhline(0, color='black',linewidth=0.5)  # Add horizontal line at y=0 (optional)
plt.axvline(0, color='black',linewidth=0.5)  # Add vertical line at x=0 (optional)
plt.show()
