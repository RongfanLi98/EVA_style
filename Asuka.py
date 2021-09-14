from lib import *
import os
from scipy.ndimage import gaussian_filter
import argparse
from matplotlib.image import imread

# Define the save path in function save first.

parser = argparse.ArgumentParser('Asuka')
parser.add_argument("--input", type=str, default="./img/Asuka.jpg", help='Image path')
parser.add_argument("--out_path", type=str, default="./img", help='Out put path')
parser.add_argument("--out_name", type=str, default="result.jpg", help='Name of the out put file, including format, e.g., result.jpg.')
parser.add_argument("--dpi", type=int, default=300, help='DPI, e.g., 300')
parser.add_argument("--threshold", type=int, default=230, help='In [0, 255]')
parser.add_argument("--sketch", type=eval, default=False, help='Weather output the sketches, true or false')
args = parser.parse_args()

img_path = args.input
out_path = args.out_path
out_name = args.out_name
dpi = args.dpi
print("File exists?:", os.path.exists(img_path))

# img = [height, width, channel]
img = imread(img_path)
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
img_opposite = 255 - img_gray
# GaussianFilter
blur_img = gaussian_filter(img_opposite, sigma=5)
img_sketch = dodge(blur_img.reshape(height, width), img_gray)
# Other methods to generate sketch
# img4 = Linear_dodge(blur_img, img_gray)
# img5 = Color_dodge(img_opposite, img_gray)

img_min = min_functin(img_sketch.copy(), 3, 3)
# save(img_min, cmap="gray", name="mini_value_filtering")

# Add up dimensions
img_final = img_min.repeat(3, axis=-1).astype('uint8')

# Color the dark areas using threshold
threshold = args.threshold
h, w, c = img_final.shape
result = img_final.copy()
for i in range(h):
    for j in range(w):
        if img_final[i][j].mean() < threshold:
            result[i][j] = img_color[i][j]

if args.sketch:
    save(os.path.join(out_path, 'gray.jpg'), img_gray, cmap="gray", dpi=dpi)
    save(os.path.join(out_path, 'opposite.jpg'), img_opposite, cmap="gray", dpi=dpi)
    save(os.path.join(out_path, 'blur.jpg'), blur_img, cmap="gray", dpi=dpi)
    save(os.path.join(out_path, 'sketch.jpg'), img_sketch, cmap="gray", dpi=dpi)

save(os.path.join(out_path, out_name), result, dpi=dpi)
