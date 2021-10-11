# EVA style image

In this repository, I transform a regular image into a image with EVA style (In fact, it is One Last Kiss style). 

我在这个代码中将常规的图片转换成了EVA风格的图片(实际上是One Last Kiss风格)。

All steps is described as following:
1. Import image 1, and generate the color map with the same size;
2. Generate grayscale image;
3. Opposite, and apply Gaussian filter;
4. Apply Color Dodge with the blur image and the grayscale;
5. Apply mini value filtering;
6. Apply Overlay, which is however, not work in my code. And I replace it with my own designed Dark Areas Color Algorithm. 

![Original image](https://github.com/RongfanLi98/EVA_style/raw/main/img/Asuka.jpg)

![Result](https://github.com/RongfanLi98/EVA_style/raw/main/img/result.jpg)

# Arguments

The default arguments will take an image named "Asuka.jpg" under ./img (i.e., img is a folder, and it is in the same folder with Asuka.py), and it outputs an image named "result.jpg". The default quality of image is 300 dpi. If you set --sketch=true, it will output temporary files. As for threshold, you can tune it to try different style.

--input, type=str, default="./img/Asuka.jpg", help='Image path'

--out_path, type=str, default="./img", help='Out put path'

--out_name, type=str, default="result.jpg", help='Name of the out put file, including format, e.g., result.jpg.'

--dpi, type=int, default=300, help='DPI, e.g., 300'

--threshold, type=int, default=230, help='In [0, 255]'

--sketch, type=eval, default=False, help='Weather output the sketches, true or false'

# Available requirements

- numpy=1.19.5
- matplotlib=3.4.1
- scipy=1.6.3

# Acknowledge

Thanks to [黑暗之环](https://www.bilibili.com/video/BV1Uf4y1n7zK), [鹿枫a](https://space.bilibili.com/29121574) and [
Matrix_11](https://blog.csdn.net/matrix_space/category_9263542_3.html).

I really like Asuka, so I made her the cover.

I would be very happy if he helped you. And I would work harder if you donated to support me (scan the QR code).

![Result](https://github.com/LeonardLi98/EVA_style/raw/main/img/support.jpg)
