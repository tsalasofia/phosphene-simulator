import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("input.jpg")

if img is None:
    raise FileNotFoundError("Put an image named 'input.jpg' in the same folder.")

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

grid_size = 16  # try 8, 16, 32
small = cv2.resize(gray, (grid_size, grid_size), interpolation=cv2.INTER_AREA)


small_norm = small / 255.0

# output

output_size = 400
phosphene = np.zeros((output_size, output_size), dtype=np.float32)

cell_size = output_size // grid_size

for y in range(grid_size):
    for x in range(grid_size):
        intensity = small_norm[y, x]
        cx = x * cell_size + cell_size // 2
        cy = y * cell_size + cell_size // 2

        radius = max(2, int(cell_size * 0.25))
        cv2.circle(phosphene, (cx, cy), radius, float(intensity), -1)

phosphene = cv2.GaussianBlur(phosphene, (0, 0), sigmaX=6, sigmaY=6)

fig, axes = plt.subplots(1, 4, figsize=(16, 4))

axes[0].imshow(img_rgb)
axes[0].set_title("Original")
axes[0].axis("off")

axes[1].imshow(gray, cmap="gray")
axes[1].set_title("Grayscale")
axes[1].axis("off")

axes[2].imshow(small, cmap="gray", interpolation="nearest")
axes[2].set_title(f"{grid_size}x{grid_size} Electrode Grid")
axes[2].axis("off")

axes[3].imshow(phosphene, cmap="gray")
axes[3].set_title("Simulated Phosphene Output")
axes[3].axis("off")

plt.tight_layout()
plt.show()
