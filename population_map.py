import tifffile as tiff
import numpy as np
import matplotlib.pyplot as plt

tif_file = 'population_0_lon_80_general.tif'
population_density = tiff.imread(tif_file)

print(np.unique(population_density))

valid_min = np.nanpercentile(population_density, 1)  # Set lower threshold
valid_max = np.nanpercentile(population_density, 99)  # Set upper threshold

# Mask out values outside the valid range
population_density_clipped = np.clip(population_density, valid_min, valid_max)

# Step 4: Normalize the data to a range [0, 1] for better visualization
population_density_normalized = (population_density_clipped - np.min(population_density_clipped)) / (np.max(population_density_clipped) - np.min(population_density_clipped))

# Step 5: Plot the population density map
plt.imshow(population_density_normalized, cmap='hot')
plt.colorbar(label='Population Density (Normalized)')
plt.title('Population Density Map (Normalized)')
plt.show()
