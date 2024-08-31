
import matplotlib.pyplot as plt

# Given data
years = list(range(2011, 2021))
cars = ['Tata', 'Kia', 'MG', 'Hyundai', 'Maruti', 'Honda', 'Skoda', 'Mahindra', 'Renault', 'Toyota']
production = [2.2, 2.5, 3.6, 5.5, 4.5, 1.2, 3.3, 8.9, 6.5, 7.6]

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(years, production, marker='o', color='b')

# Labeling
plt.title('Production of Cars')
plt.xlabel('Years')
plt.ylabel('Production in thousands')

# Adding labels to the points
for i, car in enumerate(cars):
    plt.text(years[i], production[i], car)

plt.grid(True)
plt.show()