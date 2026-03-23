# 🧠 Phosphene Vision Simulator

A Python project that simulates how visual information might be perceived through a low-resolution retinal implant using phosphene-style rendering.

## 📌 Overview

This project takes an input image and transforms it into a simplified representation resembling artificial vision produced by visual prosthetics.

The pipeline:
1. Load an image
2. Convert it to grayscale
3. Downsample it to a low-resolution grid (simulating electrode arrays)
4. Map each pixel to a glowing circular "phosphene"
5. Apply blur to simulate light diffusion

---

##  Example Output
<img width="1445" height="584" alt="image" src="https://github.com/tsalasofia/phosphene-simulator/Screenshot 2026-03-23 193223" />

The output consists of four stages:
- Original image
- Grayscale version
- Low-resolution electrode grid
- Simulated phosphene vision

---

##  Technologies Used

- Python
- OpenCV
- NumPy
- Matplotlib

---

## Installation

Install dependencies:

pip install opencv-python numpy matplotlib
