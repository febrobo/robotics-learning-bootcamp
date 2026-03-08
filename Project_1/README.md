# The Lying Sensors - State Estimation Project

## 🎯 Project Overview

This project demonstrates the fundamental principle of **sensor fusion** in robotics: how to intelligently combine multiple imperfect sensors to get a better estimate of a system's state than using any single sensor alone.

### The Problem

A robot sits at position **x = 5.0 meters**. Two sensors try to measure its position, but both are flawed:
- **GPS Sensor**: Accurate on average but noisy (±3.0 meters uncertainty)
- **Wheel Encoder**: Precise and consistent but can drift over time (±0.5 meters uncertainty)

**Question**: What's our BEST estimate of the robot's true position?

---

## 📚 Learning Objectives

By completing this project, you'll understand:

1. ✅ Why sensors have noise and uncertainty
2. ✅ How different sensors fail in different ways
3. ✅ Why combining sensors intelligently beats using any single sensor
4. ✅ How **inverse variance weighting** works in sensor fusion
5. ✅ The foundation of **Kalman filters** (used in real robotics)

---

## 🛠️ How to Run

### Requirements
```bash
pip install numpy matplotlib
```

### Execute
```bash
python lying_sensors.py
```

This will:
1. Generate 100 readings from each sensor
2. Display two plots comparing sensor readings and estimation methods
3. Print RMSE (Root Mean Squared Error) for each method

---

## 📊 Results

### Sensor Characteristics

| Metric | GPS Sensor | Encoder Sensor |
|--------|-----------|-----------------|
| Mean Reading | 5.140 m | 4.961 m |
| Standard Deviation | 3.049 m | 0.484 m |
| Variance | 9.296 | 0.234 |
| Type of Error | High noise, unbiased | Low noise, precise |

**Interpretation**: GPS readings scatter widely but average toward the true value. Encoder readings stay tight but can drift over time.

---

### Estimation Methods & Performance

| Method | Estimated Position | RMSE (Error) | Rank |
|--------|-------------------|--------------|------|
| GPS Only | 5.140 m | 0.265 m | ❌ Worst |
| Encoder Only | 4.961 m | 0.044 m | ✅ Good |
| Simple Average | 5.050 m | 0.110 m | ⚠️ Medium |
| **Weighted Average** | **4.964 m** | **0.036 m** | **🏆 BEST** |

**Key Finding**: The **weighted average outperforms all individual sensors**, including the precise encoder alone!

---

## 📈 Visual Results

### Plot 1: Sensor Readings Scatter Plot

![Sensor Readings Plot](Figure_1.png)

**What You're Seeing**:
- 🔵 **Blue dots (GPS)**: Scattered widely across 0-14 meters. Noisy but unbiased.
- 🟠 **Orange dots (Encoder)**: Tightly clustered around 5 meters. Precise and consistent.
- 🔴 **Red dashed line**: True robot position at 5.0 meters.

**Insight**: GPS data is all over the place, while encoder data is reliable but could drift if the robot moves for a long time.

---

### Plot 2: Estimation Methods Comparison (RMSE)

![RMSE Comparison](Figure_2.png)

**What You're Seeing**:
- **GPS bar** (tallest): Highest error due to noise
- **Encoder bar** (short): Low error, very reliable
- **Simple Average bar** (medium): Better than GPS, worse than encoder
- **Weighted Average bar** (shortest): **Lowest error—wins the comparison!**

**Insight**: By intelligently weighting sensors based on their precision (inverse variance), we achieve better results than any single sensor.

---

## 🧠 The Math Behind It

### Weighted Average Formula

```
Weighted Average = (w₁ × μ₁ + w₂ × μ₂) / (w₁ + w₂)
```

Where:
- μ₁, μ₂ = sensor means
- w₁, w₂ = weights based on sensor precision

### Inverse Variance Weighting

```
weight = 1 / variance = 1 / (std)²
```

**Key Insight**: Sensors with lower noise (lower variance) get higher weights, so they influence the estimate more.

**Example from our results**:
- GPS weight = 1 / 9.296 = 0.108
- Encoder weight = 1 / 0.234 = 4.274

Encoder weight is **40x larger!** That's why the weighted estimate stays close to the encoder reading.

---

## 💡 Key Takeaways

### 1. **Sensors Have Different Strengths**
- GPS: Good long-term, bad short-term
- Encoder: Good short-term, drifts over time

### 2. **Fusion Beats Individual Sensors**
Even though the encoder alone is quite good (RMSE 0.044m), combining it intelligently with GPS gives better results (RMSE 0.036m).

### 3. **Trust Is Based on Noise, Not Guess**
We don't arbitrarily decide which sensor to trust. We use **inverse variance weighting**—the mathematical way to combine uncertain information.

### 4. **This Is Real Robotics**
This principle is used in:
- 🚗 Self-driving cars (fusing camera, lidar, radar)
- 🚁 Drones (fusing GPS, IMU, barometer)
- 📱 Phone navigation (fusing GPS, accelerometer, compass)
- 🤖 Industrial robots (fusing encoders, force sensors)
- 🛰️ The **Kalman Filter**—the gold standard for state estimation

---

## 🔧 Code Structure

```
Project_1/
├── lying_sensors.py          # Main code
├── README.md                 # This file
├── Figure_1.png              # Sensor readings scatter plot
├── Figure_2.png              # RMSE comparison bar chart
└── requirements.txt          # Python dependencies
```

---

## 🚀 Next Steps

### Try These Experiments:

1. **Change sensor noise levels**
   - What if GPS had std=0.5 and encoder had std=3.0?
   - Weighted average should now favor GPS!

2. **Add a third sensor**
   - Implement a barometer (altimeter) with different noise
   - Update the weighted average to include 3 sensors

3. **Simulate sensor failure**
   - What if GPS stops working?
   - Your code should gracefully use encoder only

4. **Kalman Filter**
   - This project is the foundation for Kalman filtering
   - Next: Implement a simple Kalman filter for dynamic systems

---

## 📖 References

- **Inverse Variance Weighting**: [Wikipedia - Weighted Average](https://en.wikipedia.org/wiki/Weighted_arithmetic_mean)
- **Kalman Filter**: [Introduction to Kalman Filtering](https://en.wikipedia.org/wiki/Kalman_filter)
- **Sensor Fusion**: [Robotics - State Estimation](https://en.wikipedia.org/wiki/State_observer)

---

## ✍️ Author Notes

**What This Project Teaches**:
- The real world is uncertain and noisy
- Good engineering combines multiple imperfect sources intelligently
- Math (inverse variance weighting) gives us the optimal way to do this
- This foundation scales to complex systems like self-driving cars

**Time Spent**: ~45 minutes  
**Difficulty**: Beginner (but teaches advanced concepts!)

---

## 📝 License

This project is open source. Feel free to modify, extend, and learn from it!

---

**Made with ❤️ for learning robotics**
