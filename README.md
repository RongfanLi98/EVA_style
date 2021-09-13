# EVA_style

In this repository, I transform a regular image into a image with EVA style (In fact, it is One Last Kiss style). 

我在这个代码中将常规的图片转换成了EVA风格的图片(实际上是One Last Kiss风格)。

All steps is described as following:
1. Import image 1, and generate the color map with the same size;
2. Generate grayscale image;
3. Opposite, and apply Gaussian filter;
4. Apply Color Dodge with the blur image and the grayscale;
5. Apply mini value filtering;
6. Apply Overlay, which is however, not work in my code. And I replace it with my own designed Dark Areas Color Algorithm. 

![1 Original image](https://github.com/LeonardLi98/EVA_style/raw/main/img/Asuka.jpg)

![2 Gray](https://github.com/LeonardLi98/EVA_style/raw/main/img/gray.jpg)

![3 Opposite](https://github.com/LeonardLi98/EVA_style/raw/main/img/opposite.jpg)

![4 Sketch](https://github.com/LeonardLi98/EVA_style/raw/main/img/sketch.jpg)

![5 Filtering](https://github.com/LeonardLi98/EVA_style/raw/main/img/mini_value_filtering.jpg)

![6 Result](https://github.com/LeonardLi98/EVA_style/raw/main/img/result.jpg)

Available requirements:
- numpy=1.19.5
- matplotlib=3.4.1
- scipy=1.6.3