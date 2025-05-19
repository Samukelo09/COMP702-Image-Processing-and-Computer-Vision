import numpy as np

# Image and parameters
img = np.array([
    [0, 0, 1, 1],
    [0, 0, 1, 1],
    [0, 2, 2, 2],
    [2, 2, 3, 3]
])
levels = 4  # Gray levels (0-3)

# Co-occurrence matrix calculator
def glcm(image, dx, dy, levels):
    matrix = np.zeros((levels, levels), dtype=int)
    rows, cols = image.shape
    for i in range(rows):
        for j in range(cols):
            ni, nj = i + dx, j + dy
            if 0 <= ni < rows and 0 <= nj < cols:
                matrix[image[i, j], image[ni, nj]] += 1
    return matrix

# Compute GLCMs for all directions
directions = {
    "P45° (d=1)": (-1, 1),
    "P90° (d=1)": (-1, 0),
    "P135° (d=1)": (-1, -1),
    "P0° (d=2)": (0, 2)
}
glcms = {name: glcm(img, dx, dy, levels) for name, (dx, dy) in directions.items()}

# Compute features for P0° (d=1)
P = glcm(img, 0, 1, levels) / np.sum(glcm(img, 0, 1, levels))  # Normalize
i, j = np.indices(P.shape)

# Haralick features
features = {
    "Energy": np.sum(P**2),
    "Entropy": -np.sum(P[P > 0] * np.log2(P[P > 0])),
    "Max Probability": np.max(P),
    "Contrast": np.sum((i - j)**2 * P),
    "IDM": np.sum(P / (1 + (i - j)**2)),
    "Correlation": (np.sum((i - np.sum(P * i)) * (j - np.sum(P * j)) * P) / 
                   (np.std(i) * np.std(j)))
}

print("GLCMs:")
for name, matrix in glcms.items():
    print(f"{name}:\n{matrix}\n")

print("Features for P0° (d=1):")
for name, value in features.items():
    print(f"{name}: {value:.4f}")