from lib import *
import os
from scipy.ndimage import gaussian_filter

# Define the save path in function save first.

img_path = "./img/Asuka.jpg"
print("File exists?:", os.path.exists(img_path))

# img = [height, width, channel]
img = matplotlib.image.imread(img_path)
height = img.shape[0]
width = img.shape[1]

# Create color map. ffae22, c93cfa, ff3c3e, 24cfff, 30ffcc
a = [255, 174, 34]
b = [201, 60, 250]
c = [255, 60, 62]
d = [36, 207, 255]
e = [48, 255, 204]
img_color = my_color(height, width, [a, b, c, d, e])

# Need to resize, if use other color map
# color_path = "./img/color.png"
# img_color = matplotlib.image.imread(color_path)
# img_color = resize(img_color, height, width)

img_gray = gray(img)
save(img_gray, cmap="gray", name="gray")

img_opposite = 255 - img_gray
save(img_opposite, cmap="gray", name="opposite")

# GaussianFilter
blur_img = gaussian_filter(img_opposite, sigma=5)
save(blur_img, cmap="gray", name="blur")

img_sketch = dodge(blur_img.reshape(height, width), img_gray)
save(img_sketch, cmap="gray", name="sketch")

# Other methods to generate sketch
# img4 = Linear_dodge(blur_img, img_gray)
# img5 = Color_dodge(img_opposite, img_gray)

img_min = min_functin(img_sketch.copy(), 3, 3)
# save(img_min, cmap="gray", name="mini_value_filtering")

# Add up dimensions
img_final = img_min.repeat(3, axis=-1).astype('uint8')

# Color the dark areas using threshold
threshold = 230
h, w, c = img_final.shape
result = img_final.copy()
for i in range(h):
    for j in range(w):
        if img_final[i][j].mean() < threshold:
            result[i][j] = img_color[i][j]

save(result, name="result")
