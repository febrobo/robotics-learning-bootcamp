# 🤖 Complete Robotics — Learn by Building Projects in Python

> **Philosophy**: You don't learn robotics by reading. You learn by coding. Every single concept is a project you **BUILD**, **RUN**, and **SEE working**. Each project builds on the previous one like LEGO blocks.

**Status**: 🚀 **Starting the journey** — Project 1 complete, 24 projects to go!

---

## ✅ Completed Projects

### **Project 1: The Lying Sensors** ✨

**What You Built**
- Simulated 2 sensors measuring a robot's position
- GPS: noisy (±3.0m) but unbiased
- Wheel encoder: precise (±0.5m) but can drift
- Compared 4 estimation methods and proved weighted average wins!

**What You Learned**
- Sensors have noise (uncertainty)
- Different sensors fail in different ways
- Combining sensors **intelligently** beats any single sensor
- **Foundation of ALL robotics state estimation**

**Key Files**
- 📄 `Project_1/lying_sensors.py` — The code
- 📊 `Project_1/Figure_1.png` — Sensor readings visualization
- 📊 `Project_1/Figure_2.png` — RMSE comparison (weighted average wins!)
- 📖 `Project_1/README.md` — Detailed writeup with math and results

**Key Results**

| Method | Estimated Position | RMSE Error | Status |
|--------|-------------------|-----------|--------|
| GPS Only | 5.140 m | 0.265 m | ❌ Worst |
| Encoder Only | 4.961 m | 0.044 m | ✅ Good |
| Simple Average | 5.050 m | 0.110 m | ⚠️ Medium |
| **Weighted Average** | **4.964 m** | **0.036 m** | **🏆 BEST** |

**The Magic Moment**
Weighted average (0.0362) beat EVEN the encoder alone (0.0439)! By trusting the more precise sensor more, we got better than both.

**Key Concept: Inverse Variance Weighting**
```
weight = 1 / variance = 1 / (std)²

GPS weight = 1 / (3.0²) = 0.111
Encoder weight = 1 / (0.5²) = 4.0

Encoder weight is 36x higher → trust it more!
```

---

## 🗺️ Upcoming Projects Roadmap

### **LEVEL 1: THE FOUNDATION** (4 projects)

| # | Project | Time | Status | Next Steps |
|---|---------|------|--------|-----------|
| 1 | **The Lying Sensors** ✅ | 45 min | 🟢 DONE | |
| 2 | **Moving Robot with Lying Sensors** | 60 min | ⏳ Tomorrow | Track a moving target over time |
| 3 | **Probability is Just Belief** | 45 min | ⏳ Coming | Represent uncertainty as distributions |
| 4 | **The Predict-Update Dance** | 90 min | ⏳ Coming | THE core robotics loop |

**What This Level Teaches**: Why robots need math, sensor fusion basics, the predict-update pattern

---

### **LEVEL 2: KALMAN FILTER** (3 projects)

| # | Project | Time | Status | What's It About |
|---|---------|------|--------|-----------------|
| 5 | **1D Kalman Filter — Falling Ball** | 90 min | 🔒 Locked | Optimal filtering, estimate hidden states |
| 6 | **2D Kalman Filter — Tracking Drone** | 90 min | 🔒 Locked | Multi-dimensional tracking with uncertainty |
| 7 | **KF Tuning Lab** | 60 min | 🔒 Locked | Practical tuning of Q and R parameters |

**Prerequisites**: Complete Level 1 first

---

### **LEVEL 3: EXTENDED KALMAN FILTER** (4 projects)

| # | Project | Time | Status | What's It About |
|---|---------|------|--------|-----------------|
| 8 | **See KF Fail** | 45 min | 🔒 Locked | Why linear filters fail on circular paths |
| 9 | **Jacobians — Linearizing Nonlinearity** | 60 min | 🔒 Locked | Partial derivatives for nonlinear systems |
| 10 | **EKF — Robot Driving Figure-8** | 90 min | 🔒 Locked | Tracking nonlinear robot motion |
| 11 | **EKF Localization with Landmarks** | 90 min | 🔒 Locked | Using known features to localize |

**Prerequisites**: Complete Level 2 first

---

### **LEVEL 4: SENSOR FUSION** (3 projects)

| # | Project | Time | Status | What's It About |
|---|---------|------|--------|-----------------|
| 12 | **Complementary Filter — IMU Fusion** | 60 min | 🔒 Locked | Fuse gyro + accelerometer |
| 13 | **GPS + IMU Kalman Fusion** | 90 min | 🔒 Locked | Multi-rate sensor fusion |
| 14 | **Multi-Sensor EKF Fusion** | 120 min | 🔒 Locked | Industry-grade: 4 sensors in one EKF |

**Prerequisites**: Complete Level 3 first

---

### **LEVEL 5: PERCEPTION** (3 projects)

| # | Project | Time | Status | What's It About |
|---|---------|------|--------|-----------------|
| 15 | **LiDAR Simulator** | 60 min | 🔒 Locked | How robots "see" with lasers |
| 16 | **Occupancy Grid** | 90 min | 🔒 Locked | Build maps from sensor data |
| 17 | **Point Cloud Processing** | 90 min | 🔒 Locked | Filter and cluster 3D data |

**Prerequisites**: Complete Level 4 first

---

### **LEVEL 6: LOCALIZATION** (2 projects)

| # | Project | Time | Status | What's It About |
|---|---------|------|--------|-----------------|
| 18 | **Particle Filter Localization** | 120 min | 🔒 Locked | "Where am I?" using particles |
| 19 | **ICP — Scan Matching** | 60 min | 🔒 Locked | Align point clouds |

**Prerequisites**: Complete Level 5 first

---

### **LEVEL 7: SLAM** (2 projects)

| # | Project | Time | Status | What's It About |
|---|---------|------|--------|-----------------|
| 20 | **EKF-SLAM** | 120 min | 🔒 Locked | Map + localize simultaneously |
| 21 | **Graph-SLAM** | 90 min | 🔒 Locked | Modern optimization-based SLAM |

**Prerequisites**: Complete Level 6 first

---

### **LEVEL 8: PATH PLANNING** (3 projects)

| # | Project | Time | Status | What's It About |
|---|---------|------|--------|-----------------|
| 22 | **A* Search** | 90 min | 🔒 Locked | Optimal pathfinding |
| 23 | **RRT and RRT*** | 90 min | 🔒 Locked | Sampling-based planning |
| 24 | **DWA — Local Planning** | 90 min | 🔒 Locked | Real-time obstacle avoidance |

**Prerequisites**: Complete Level 7 first

---

### **LEVEL 9: INTEGRATION** (1 project)

| # | Project | Time | Status | What's It About |
|---|---------|------|--------|-----------------|
| 25 | **MEGA CAPSTONE: Full Autonomous Navigation** | 240 min | 🔒 Locked | Everything together! |

**Prerequisites**: Complete Level 8 first

---

## 📊 Overall Progress

```
█████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 4% Complete (1 of 25 projects)

Time Spent: 0.75 hours / 32 hours
Total Time Remaining: ~31.25 hours
```

---

## 🚀 How to Use This Repository

### **Daily Workflow**
1. **Morning**: Read the new project's README
2. **Code**: Build the project step by step
3. **Visualize**: Run it, see the plots
4. **Understand**: Explain the concepts in your own words
5. **Commit**: `git commit -m "Complete Project X"`
6. **Update**: Add results to this README

### **Running Project 1**
```bash
cd Project_1
python lying_sensors.py
```

You should see:
- A scatter plot of GPS vs encoder readings
- A bar chart comparing RMSE for all 4 methods
- Console output showing the results table

---

## 📚 Learning Path

```
START HERE
    ↓
Project 1 ✅ (sensors lie)
    ↓
Project 2 (tracking moving targets)
    ↓
Project 3 (probability distributions)
    ↓
Project 4 (predict-update loop)
    ↓
Projects 5-7 (Kalman Filters)
    ↓
Projects 8-11 (Extended Kalman Filters)
    ↓
Projects 12-14 (Sensor Fusion)
    ↓
Projects 15-17 (Perception)
    ↓
Projects 18-19 (Localization)
    ↓
Projects 20-21 (SLAM)
    ↓
Projects 22-24 (Path Planning)
    ↓
Project 25 (EVERYTHING TOGETHER!)
    ↓
YOU ARE NOW A ROBOTICIST 🤖
```

---

## 💾 Folder Structure

```
Robotics/
├── README.md                          ← You are here (main overview)
├── CURRICULUM.md                      ← Detailed learning guide
├── requirements.txt                   ← Dependencies
├── .gitignore
│
├── Project_1/                         ✅ COMPLETED
│   ├── lying_sensors.py               (code)
│   ├── Figure_1.png                   (scatter plot)
│   ├── Figure_2.png                   (RMSE bar chart)
│   └── README.md                      (results & explanation)
│
├── Project_2/                         ⏳ Tomorrow
│   ├── moving_robot_sensors.py        (empty)
│   └── README.md                      (coming)
│
├── Project_3/ through Project_25/     🔒 Locked
│   └── README.md
```

---

## 🎯 Skills You'll Have After Each Level

### **After Level 1** (Today + 3 more days)
✅ Understand sensor fusion  
✅ Know why multiple sensors beat one sensor  
✅ Understand the predict-update loop  

### **After Level 2** (2 weeks)
✅ Implement Kalman filters  
✅ Understand covariance and Kalman gain  
✅ Track objects in 2D  

### **After Level 3** (3 weeks)
✅ Handle nonlinear robot motion  
✅ Use Jacobians to linearize  
✅ Localize using landmarks  

### **After Level 4** (4 weeks)
✅ Fuse multiple sensors at different rates  
✅ Build robust systems  
✅ Handle sensor failures  

### **After Level 5-9** (8 weeks)
✅ **FULL ROBOTICS STACK**  
✅ Build autonomous navigation systems  
✅ Solve the entire robotics problem!

---

## 📝 Dependencies

```bash
pip install -r requirements.txt
```

Installs:
- numpy (numerical computing)
- matplotlib (visualization)
- scipy (scientific computing)
- sympy (symbolic math, for Project 9)
- open3d (point clouds, for Project 17)
- scikit-learn (clustering, for Project 17)

---

## 🎓 After You Finish All 25 Projects

You'll be able to:
- Explain Kalman filters in an interview
- Build SLAM systems from scratch
- Implement sensor fusion in real systems
- Design path planning algorithms
- Understand every autonomous robot

**You won't just know robotics. You'll have BUILT robotics.**

---

## 📖 References for Project 1

- [Kalman Filter Explained](https://www.kalmanfilter.net/)
- [Inverse Variance Weighting](https://en.wikipedia.org/wiki/Weighted_arithmetic_mean)
- [Why Sensor Fusion Works](https://en.wikipedia.org/wiki/Sensor_fusion)

---

## 🤝 How to Update This README

Each day after completing a project:

1. Move the project from "Upcoming" to "Completed"
2. Add your results and key findings
3. Update the progress bar
4. Commit: `git commit -m "Complete Project X + update README"`

Example for Project 2:
```markdown
### **Project 2: Moving Robot with Lying Sensors** ✨

**Status**: 🟢 COMPLETED (Day 2)

**What You Learned**
- Prediction: using motion model to forecast position
- Dead reckoning drifts over time
- Sensor fusion: combining prediction + measurement
- Key insight: Different sensors excel at different time scales
```

---

## ✨ Next Project Preview

**Project 2: Moving Robot with Lying Sensors**  
Coming tomorrow!

- Robot moves at 1 m/s for 60 seconds
- GPS gives position every 1 second (noisy)
- Speedometer gives velocity (noisy, 10 Hz)
- You'll implement predict-update fusion
- Watch dead reckoning drift, then see fusion fix it!

**Time**: 60 minutes  
**Difficulty**: Medium (builds on Project 1 concepts)

---

## 🚀 You're Ready!

You've completed Project 1. You understand the foundation.

Tomorrow: Project 2 awaits. The journey continues. 🤖

---

**Made with ❤️ for aspiring roboticists**  
*Started: [Date you began]*  
*Last Updated: [Today's date]*

