# The Lying Sensors - State Estimation Project

## 🎯 What This Project Is About

I built this to answer a simple question: **If I have two sensors measuring the same thing and both are wrong, which one should I trust?**

Turns out, the answer isn't "pick the better one." It's "use both intelligently." And that's the entire foundation of robotics.

---

## 🤔 The Problem I Solved

Imagine a robot at position **x = 5.0 meters**. Two sensors try to measure where it is:

- **GPS**: Says the robot is at 5.0 ± 3.0 meters. Very jumpy. One second it reads 2.1m, next second 7.8m. But if you average many readings, you get close to 5.0.
  
- **Wheel Encoder**: Says the robot is at 5.0 ± 0.5 meters. Super consistent! Always reads between 4.9 and 5.1. But over time, if the wheel gets dirty or the sensor drifts, it might be totally wrong.

**My challenge**: Figure out the BEST estimate of position using both.

---

## 💡 What I Built

I wrote code that:

1. **Simulated 100 sensor readings** from each sensor (with realistic noise)
2. **Plotted them** so I could SEE the difference (GPS scattered everywhere, encoder tight)
3. **Tried 4 different estimation methods**:
   - Use GPS only (too jumpy)
   - Use encoder only (good, but what about drift?)
   - Average both equally (medium)
   - Weight them by precision (best!)
4. **Compared them** using RMSE (error metric)

---

## 📊 My Results

### How Noisy Are These Sensors?

| Sensor | Mean | Spread (Std Dev) | Comment |
|--------|------|------------------|---------|
| GPS | 5.140 m | 3.049 m | All over the place |
| Encoder | 4.961 m | 0.484 m | Super tight |

### Which Method Won?

| Method | Estimate | Error (RMSE) | Rank |
|--------|----------|--------------|------|
| GPS Only | 5.140 m | 0.265 m | 4th (worst) |
| Encoder Only | 4.961 m | 0.044 m | 2nd |
| Simple Average (equal weight) | 5.050 m | 0.110 m | 3rd |
| **Weighted Average** | **4.964 m** | **0.036 m** | **1st (BEST!)** |

**The magic moment**: Weighted average beat EVEN the encoder alone!

How? By saying: "GPS is too noisy, don't trust it much. Encoder is precise, trust it WAY more."

---

## 🧠 The Math (Explained Simply)

The key idea: **Trust sensors based on how reliable they are, not randomly.**

```
Inverse Variance Weighting:
weight = 1 / (standard_deviation²)

GPS weight = 1 / (3.0²) = 0.111
Encoder weight = 1 / (0.5²) = 4.0

Encoder weight is 36x larger!
So we trust encoder 36x more.
```

Then combine them:
```
Best Estimate = (GPS_weight × GPS_reading + Encoder_weight × Encoder_reading) 
                / (GPS_weight + Encoder_weight)
```

**Why does this work?** Because mathematically, when you weight by inverse variance, you get the **minimum possible error**. It's proven to be optimal.

---

## 📈 What I Visualized

### Plot 1: The Raw Data
![Sensor Readings Plot](Figure_1.png)

**What I see here:**
- Blue dots everywhere = GPS is noisy as hell
- Orange dots in a tight line = Encoder is stable
- Red dashed line = the true position (5.0)
- The orange dots hug the red line. GPS dots are all over.

**Insight**: Visually, encoder is better. But what if both sensors drift in the same direction? That's why combining them helps.

### Plot 2: The Winner
![RMSE Comparison](Figure_2.png)

**The bar chart shows:**
- GPS bar (tallest) = biggest error
- Encoder bar (short) = small error
- Simple average bar (medium) = middle ground
- **Weighted average bar (shortest) = WINS**

This is the payoff of the whole project. One simple idea (weight by precision) beats everything.

---

## 🔑 Key Things I Learned

### 1. Sensors Lie in Different Ways
- GPS lies a lot but honestly (on average, it's correct)
- Encoder lies consistently (very precise, but can be systematically wrong)
- They're wrong in opposite ways → combine them and errors cancel!

### 2. You Can't Just Pick One
Even the good encoder (0.044m error) gets beaten by combining both (0.036m error).

This blew my mind. Combination is better than the best single sensor!

### 3. There's a Right Way to Combine
Not all combinations are equal. Inverse variance weighting is proven to be optimal.

This is why it matters in real systems:
- Self-driving cars fuse camera + lidar + radar
- Drones fuse GPS + IMU + barometer  
- Phones fuse GPS + accelerometer + compass
- All using this same principle!

### 4. This Is the Foundation of Everything
This simple project is the seed of:
- Kalman filters
- Particle filters
- SLAM (simultaneous localization and mapping)
- Every autonomous system on Earth

I'm starting with the basics, and the next 24 projects build on this.

---

## 🛠️ How to Run This

```bash
cd Project_1
python lying_sensors.py
```

It will:
1. Generate random sensor readings
2. Show two plots
3. Print error metrics for all 4 methods
4. Prove weighted average is best

**Dependencies:**
```bash
pip install numpy matplotlib
```

---

## 🚀 What's Next

I got curious about some things:

1. **What if encoder was noisier?** Would GPS suddenly be better?
   - Probably. The weights would flip.

2. **What if I add a third sensor?** Compass? Barometer?
   - Same formula! Just add more terms.

3. **What if one sensor fails?** 
   - With just two, we're stuck. But with three or more, the system keeps working.

4. **What about moving targets?**
   - This was static. Real robots move. That's Project 2.

5. **The Kalman Filter**
   - This project is literally the first step toward Kalman filtering
   - Kalman filter automates all of this and handles dynamic systems
   - That's where it gets really interesting

---

## 📝 Final Thoughts

This simple project taught me something fundamental: **Imperfect systems can be combined to make perfect-ish systems.**

It's not about having perfect sensors. It's about being smart about combining imperfect ones.

That's the entire philosophy of robotics.

---

## 📚 Code

All code is in `lying_sensors.py`. It's pretty straightforward:

1. Simulate sensors (numpy.random.normal)
2. Calculate means and variances
3. Compute weights
4. Calculate weighted average
5. Plot and compare

The math is only a few lines. The visualization makes it clear.

---

**Time invested**: 45 minutes (including understanding, coding, debugging, visualizing)  
**Difficulty**: Beginner level, but teaches advanced concepts  
**Made with**: numpy + matplotlib + curiosity

---

**Next up**: Project 2 - Moving Robot with Lying Sensors 🚀
