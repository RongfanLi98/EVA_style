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

![Original image](https://github.com/LeonardLi98/EVA_style/raw/main/img/Asuka.jpg)

![Result](https://github.com/LeonardLi98/EVA_style/raw/main/img/result.jpg)

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
