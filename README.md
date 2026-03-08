# 🤖 Complete Robotics Learning Bootcamp

**By Febin** — Learning robotics from scratch, one project at a time.

> I don't learn by reading. I learn by building things and seeing them work.

**Current Status**: 🚀 **Project 1 Complete** — 24 more projects to go!

---

## 📖 The Story Behind This Repository

I started with a simple question: **How do robots know where they are when all their sensors lie?**

That one question led me down the robotics rabbit hole. And I realized that robotics isn't some impossible thing—it's just layers of smart engineering, each building on the last.

So I decided to build all 25 projects and document the entire journey. No skipping the hard parts, no reading-only theories. Just code, visualizations, and understanding.

This is my learning path. Maybe it'll be yours too.

---

## ✅ What I've Built So Far

### **Project 1: The Lying Sensors** ✨

**The Problem**
I had a robot at position 5.0 meters. Two sensors tried to measure it:
- GPS: "I think it's at 5.0... but I could be off by ±3 meters" (noisy AF)
- Wheel Encoder: "It's definitely at 5.0 ± 0.5 meters" (precise but can drift)

**My Challenge**: Figure out the BEST estimate using both.

**What I Learned**
- Sensors don't fail the same way
- GPS is all over the place but honest on average
- Encoder is precise but can slowly drift
- **The key insight**: Combine them intelligently and you beat both!

**The Results**

| Method | Estimate | Error | Winner? |
|--------|----------|-------|---------|
| GPS Only | 5.140 m | 0.265 m | ❌ |
| Encoder Only | 4.961 m | 0.044 m | ✅ Good |
| Simple Average | 5.050 m | 0.110 m | ⚠️ |
| **Weighted Average** | **4.964 m** | **0.036 m** | **🏆 BEST!** |

**The Magic**: By weighting each sensor by its precision, I got the lowest error. Lower than either sensor alone!

**The Formula**
```
weight = 1 / (noise level²)

More noise → lower weight
Less noise → higher weight

Then blend them together. Done.
```

**Why This Matters**
This one idea (inverse variance weighting) is the foundation of:
- Kalman Filters (used in Apollo spacecraft)
- Every self-driving car on the road
- Drones, robots, navigation systems—everything

And I just built it from scratch in one project.

---

## 🗺️ My 25-Project Roadmap

### **LEVEL 1: THE FOUNDATION** (4 projects)
*Understanding why robots need math*

| # | Project | Status | My Notes |
|---|---------|--------|----------|
| 1 | **The Lying Sensors** | ✅ DONE | Sensor fusion basics—sensor weighting |
| 2 | **Moving Robot with Lying Sensors** | ⏳ Tomorrow | Prediction vs measurement over time |
| 3 | **Probability is Just Belief** | 🔒 Coming | Bayes' theorem and distributions |
| 4 | **The Predict-Update Dance** | 🔒 Coming | THE core pattern all filters use |

**What I'll Understand**: Why sensors fail, how to combine them, the predict-update loop

---

### **LEVEL 2: KALMAN FILTER** (3 projects)
*The optimal filtering algorithm*

| # | Project | Time |
|---|---------|------|
| 5 | **1D Kalman Filter — Falling Ball** | 90 min |
| 6 | **2D Kalman Filter — Tracking Drone** | 90 min |
| 7 | **KF Tuning Lab** | 60 min |

**Prerequisites**: Complete Level 1

---

### **LEVEL 3: EXTENDED KALMAN FILTER** (4 projects)
*Handling real robot motion (turns, rotations)*

| # | Project | Time |
|---|---------|------|
| 8 | **See KF Fail** | 45 min |
| 9 | **Jacobians** | 60 min |
| 10 | **EKF on Figure-8** | 90 min |
| 11 | **EKF Localization** | 90 min |

**Prerequisites**: Complete Level 2

---

### **LEVEL 4: SENSOR FUSION** (3 projects)
*Combining multiple sensors intelligently*

| # | Project | Time |
|---|---------|------|
| 12 | **Complementary Filter** | 60 min |
| 13 | **GPS + IMU Fusion** | 90 min |
| 14 | **Multi-Sensor EKF** | 120 min |

**Prerequisites**: Complete Level 3

---

### **LEVEL 5: PERCEPTION** (3 projects)
*How robots see the world*

| # | Project | Time |
|---|---------|------|
| 15 | **LiDAR Simulator** | 60 min |
| 16 | **Occupancy Grid** | 90 min |
| 17 | **Point Cloud Processing** | 90 min |

**Prerequisites**: Complete Level 4

---

### **LEVEL 6: LOCALIZATION** (2 projects)
*"Where am I?" problem solved*

| # | Project | Time |
|---|---------|------|
| 18 | **Particle Filter Localization** | 120 min |
| 19 | **ICP Scan Matching** | 60 min |

**Prerequisites**: Complete Level 5

---

### **LEVEL 7: SLAM** (2 projects)
*The holy grail: map AND localize at the same time*

| # | Project | Time |
|---|---------|------|
| 20 | **EKF-SLAM** | 120 min |
| 21 | **Graph-SLAM** | 90 min |

**Prerequisites**: Complete Level 6

---

### **LEVEL 8: PATH PLANNING** (3 projects)
*Getting the robot from A to B optimally*

| # | Project | Time |
|---|---------|------|
| 22 | **A* Search** | 90 min |
| 23 | **RRT and RRT*** | 90 min |
| 24 | **DWA Local Planner** | 90 min |

**Prerequisites**: Complete Level 7

---

### **LEVEL 9: THE CAPSTONE** (1 project)
*Everything together*

| # | Project | Time |
|---|---------|------|
| 25 | **Full Autonomous Navigation** | 240 min |

**Prerequisites**: Complete Level 8

---

## 📊 Progress Tracker

```
█████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ 4% Complete

Time Invested: ~45 minutes
Time Remaining: ~31 hours
Projects Done: 1 / 25
```

---

## 💾 How It's Organized

```
robotics-learning-bootcamp/
├── README.md                    ← You are here
├── requirements.txt             ← pip install these
├── .gitignore
│
└── Project_1/                   ✅ COMPLETE
    ├── lying_sensors.py         (the code I wrote)
    ├── Figure_1.png             (scatter plot of sensor readings)
    ├── Figure_2.png             (RMSE comparison bar chart)
    └── README.md                (what I learned, detailed)

├── Project_2/ through 25/       🔒 Coming soon
```

Each project folder has:
- **Code** (Python, fully commented)
- **Visualizations** (plots showing what's happening)
- **README** (my notes on what I learned)

---

## 🚀 How to Use This

### **If You Want to Follow Along**
1. Clone the repo
2. Go to Project_1, run the code
3. See the plots, understand the concepts
4. Move to Project_2, etc.

### **If You Want to Learn Robotics**
Read each project's README first. Then look at the code. Then modify it and break it and fix it. That's when real learning happens.

### **If You're Interviewing Me**
Each project is a story I can tell:
- "I built a Kalman filter from scratch that estimates states you never directly measure"
- "I implemented SLAM so a robot could map while localizing"
- "I created a multi-sensor fusion system that handles 4 sensors at different rates"

---

## 🎯 The Learning Curve

### **After Project 1** (today)
✅ Understand why sensor fusion works  
✅ Know inverse variance weighting  
✅ See how to combine imperfect data  

### **After Projects 2-4** (1 week)
✅ Understand the predict-update loop  
✅ Know Bayes' theorem  
✅ Recognize this pattern everywhere  

### **After Projects 5-7** (2 weeks)
✅ Implement Kalman filters  
✅ Handle nonlinear systems  
✅ Track objects in real-time  

### **After Projects 8-14** (4 weeks)
✅ Multi-sensor fusion  
✅ EKF for real robot motion  
✅ Build robust systems  

### **After Projects 15-25** (8 weeks)
✅ **FULL ROBOTICS STACK**  
✅ Autonomous navigation  
✅ Understand every self-driving car algorithm  

---

## 📚 Tech Stack

- **Python** (all code)
- **NumPy** (math & matrices)
- **Matplotlib** (plotting)
- **SciPy** (scientific computing)
- **SymPy** (symbolic math—later projects)
- **Open3D** (point clouds—later projects)

All installed via:
```bash
pip install -r requirements.txt
```

---

## 🤔 Questions I Started With

**Project 1 answered:**
- Why do we need multiple sensors if one is good?
- How do we trust sensors based on precision?
- What's inverse variance weighting?
- Is there a right way to combine data?

**Projects 2-4 will answer:**
- How do we handle moving targets?
- What's the predict-update pattern?
- How do we represent uncertainty?

**Projects 5-25 will answer:**
- How does Kalman filtering work?
- How do robots map environments?
- How do they plan paths?
- How do they navigate autonomously?

---

## 💡 Why I'm Doing This

Robotics is intimidating. There are so many concepts: Kalman filters, SLAM, path planning, sensor fusion...

But they all stack on top of each other. And if I build them one by one, seeing each one work, the whole picture becomes clear.

That's the goal of this repository: **Make robotics less intimidating by building it piece by piece.**

---

## 🎬 What's Next

**Tomorrow: Project 2 — Moving Robot with Lying Sensors**

I'll extend Project 1 to handle motion. A robot moving at constant velocity, sensors trying to track it, prediction+measurement fusion.

Watch dead reckoning fail. Watch sensor fusion fix it.

---

## 📖 Resources I'm Using

- Thrun, Burgard, Fox — *Probabilistic Robotics* (the bible)
- [Kalman Filter Intuition](https://www.kalmanfilter.net/)
- ROS documentation
- Papers on SLAM, path planning, sensor fusion

---

## 👨‍💻 About This Repository

**By**: Febin  
**Start Date**: March 7, 2026  
**Philosophy**: Learn by building, not reading  
**Goal**: Understand and implement the entire robotics stack from first principles  

This isn't a textbook. This is a learning journey, documented.

---

**Next up**: Project 2 🚀

Let's keep building.
