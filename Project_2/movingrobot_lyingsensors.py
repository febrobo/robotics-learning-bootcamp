import numpy as np
import matplotlib.pyplot as plt

# Parameters
total_time = 60
dt_speedometer = 0.1
dt_gps = 1.0

# Time Arrays
t_speedometer = np.arange(0, total_time + dt_speedometer, dt_speedometer)
t_gps = np.arange(dt_gps, total_time + dt_gps, dt_gps)

print("Speedometer times:", len(t_speedometer), "readings")
print("GPS times:", len(t_gps), "readings")

# True position
true_position = t_speedometer

print("True position at t=0:", true_position[0])
print("True position at t=1:", true_position[10])
print("True position at t=60:", true_position[-1])

# Speedometer readings

true_velocity = np.ones(len(t_speedometer)) * 1.0

print("True velocity shape:", true_velocity.shape)
print("First 5 velocities", true_velocity[:5])

# Speedometer noise

speedometer_readings = true_velocity + np.random.normal(loc=0, scale=0.3, size=len(t_speedometer))

print("Speedometer readings (first 10):", speedometer_readings[:10])

# True GPS positions

true_position_at_gps = t_gps

print("True position at GPS times:", true_position_at_gps)

# GPS noise

gps_readings = true_position_at_gps + np.random.normal(loc=0, scale=3.0, size=len(t_gps))

print("GPS readings:", gps_readings)
print("GPS noise level:", np.std(gps_readings - true_position_at_gps))

# Method 1: GPS only

gps_only_estimate = np.zeros(len(t_gps))

gps_only_estimate[:] = gps_readings

print("GPS only estimates (first 5):", gps_only_estimate[:5])
print("GPS only estimates (last 5):", gps_only_estimate[-5:])

# Method 2: Dead Reckoning

dead_reckoning = np.zeros(len(t_speedometer))
dead_reckoning[0] = 0

for i in range(1, len(t_speedometer)):
    dead_reckoning[i] = dead_reckoning[i-1] + speedometer_readings[i-1] * dt_speedometer

print("Dead reckoning at t=10:", dead_reckoning[100])
print("Dead reckoning at t=60:", dead_reckoning[-1])
print("True position at t=60:", true_position[-1])

# Method 3: Smart Fusion

fusion_estimate = np.zeros(len(t_speedometer))
fusion_estimate[0] = 0

last_gps_position = 0
gps_idx = 0
for i in range(1, len(t_speedometer)):
    if t_speedometer[i] == t_gps[gps_idx]:
        predicted_pos = fusion_estimate[i-1] + speedometer_readings[i-1] * dt_speedometer

        gps_weight = 1 / (3.0 ** 2)
        pred_weight = 1 / (0.3 ** 2)

        fusion_estimate[i] = (gps_weight * gps_readings[gps_idx] + pred_weight * predicted_pos) / (gps_weight + pred_weight)
        last_gps_position = fusion_estimate[i]
        gps_idx += 1
    else:
        fusion_estimate[i] = fusion_estimate[i-1] + speedometer_readings[i-1] * dt_speedometer


print("Fusion estimate at t=10:", fusion_estimate[100])
print("Fusion estimate at t=60:", fusion_estimate[-1])
print("True position at t=60:", true_position[-1])


print("=== METHOD 1: GPS ONLY ===")
print("GPS only final position:", gps_only_estimate[-1])
print("GPS only error:", abs(gps_only_estimate[-1] - 60.0))

print("\n=== METHOD 2: DEAD RECKONING ===")
print("Dead reckoning final position:", dead_reckoning[-1])
print("Dead reckoning error:", abs(dead_reckoning[-1] - 60.0))

print("\n=== METHOD 3: SMART FUSION ===")
print("Fusion final position:", fusion_estimate[-1])
print("Fusion error:", abs(fusion_estimate[-1] - 60.0))

print("\n=== COMPARISON ===")
print("True final position: 60.0")

fig = plt.figure()
plt.plot(t_speedometer, true_position, "g-", label="True Position", linewidth=2)
plt.scatter(t_gps, gps_only_estimate, color="red", marker=".", label="GPS Only", s=50)
plt.plot(t_speedometer, dead_reckoning, "b--", label="Dead Reckoning", linewidth= 1.5)
plt.plot(t_speedometer, fusion_estimate, "m-", label="Smart Fusion", linewidth=2)

plt.xlabel("Time (seconds)")
plt.ylabel("Position (meters)")
plt.title("Project 2: Moving Robot with Lying Sensors")
plt.legend()
plt.grid()

gps_error = np.sqrt(np.mean((gps_only_estimate - true_position_at_gps) ** 2))
dr_error = np.sqrt(np.mean((dead_reckoning - true_position) ** 2))
fusion_error = np.sqrt(np.mean((fusion_estimate - true_position) ** 2))

fig2 = plt.figure()

methods = ["GPS Only", "Dead Reckoning", "Smart Fusion"]
errors = [gps_error, dr_error, fusion_error]

plt.bar(methods, errors, color=["red", "blue", "magenta"])
plt.ylabel("RMSE Error (meters)")
plt.title("Project2: RMSE Comparison")
plt.grid()

print("\n=== RMSE COMPARISON ===")
print(f"GPS Only RMSE: {gps_error:.4f}m")
print(f"Dead Reckoning RMSE: {dr_error:.4f}m")
print(f"Smart Fusion RMSE: {fusion_error:.4f}m")

plt.show()