# Lying Sensors

# Import
import numpy as np
import matplotlib.pyplot as plt

# Parameters
gps_readings = np.random.normal(loc = 5, scale = 3.0, size = 100)
encoder_readings = np.random.normal(loc = 5, scale = 0.5, size = 100)

print("GPS Readings:", gps_readings.mean())
print("Encoder Readings:", encoder_readings.mean())

print("GPS std:", gps_readings.std())
print("Encoder std:", encoder_readings.std())

# Plotting
fig = plt.figure()
plt.scatter(x = range(100), y = gps_readings, label = "GPS Sensor", alpha = 0.6)
plt.scatter(x = range(100), y = encoder_readings, label = "Encoder Sensors", alpha = 0.6)

plt.axhline(y = 5.0, color = "red", linestyle = "--", label = "True Position")
plt.xlabel("Reading Number")
plt.ylabel("Position (meters)")

plt.title("Sensor Readings vs True Position")
plt.legend()
plt.show()

# Average
simple_average = (np.mean(gps_readings) + np.mean(encoder_readings)) / 2

print("Simple Average:", simple_average)

# Variance and Weighting:
# GPS Variance and weights

gps_var = gps_readings.std()**2
gps_weight = 1 / gps_var

# Encoder Variance and weights
encoder_var = encoder_readings.std()**2
encoder_weight = 1 / encoder_var

# Weighted Average
weighted_average = (gps_weight * np.mean(gps_readings) + encoder_weight * np.mean(encoder_readings)) / (gps_weight + encoder_weight)

print("Weighted Average:", weighted_average)

# RMSE Calculation
gps_error = np.sqrt((np.mean(gps_readings) - 5.0)**2)
encoder_error = np.sqrt((np.mean(encoder_readings) - 5.0)**2)

simple_error = np.sqrt((simple_average - 5.0)**2)
weighted_error = np.sqrt((weighted_average - 5.0)**2)

# Print Errors
print("GPS RMSE:", gps_error)
print("Encoder RMSE:", encoder_error)
print("Simple Average RMSE:", simple_error)
print("Weighted Average RMSE:", weighted_error)

# Plotting

fig2 = plt.figure()

plt.bar(["GPS", "Encoder", "Simple Avg", "Weighted Avg"], [gps_error, encoder_error, simple_error, weighted_error])
plt.ylabel("RMSE Error (meters)")
plt.title("Comparison of Estimation Methods")
plt.show()