# 目录

- 概述

  - 算法效果

- 具体实现

  - 程序流程

  - 编程原理与方法

  - 细节处理

    

## 概述

该项目是基于python编写的简易的数独游戏解密器，略微简单粗糙。实现了可视化界面，输入数独谜面之后，程序将会给出一个正确答案（若答案不唯一，也只会给出一个答案）。

**数独游戏的规则**

在九宫格(3格宽×3格高)的正方形状，每一格又细分为一个九宫格。在每一个小九宫格中，填入1-9的数字。

要求：
	1、每一行的数字不重复
	2、每一列的数字不重复
	3、每一大宫内的数字不重复

<img src="C:\Users\hasee\AppData\Roaming\Typora\typora-user-images\image-20191221234715212.png" alt="image-20191221234715212" style="zoom:50%;" />

#### 算法效果

<img src="C:\Users\hasee\AppData\Roaming\Typora\typora-user-images\image-20191221235129651.png" alt="image-20191221235129651" style="zoom:67%;" />



## 具体实现

### 程序流程

<img src="C:\Users\hasee\AppData\Roaming\Typora\typora-user-images\image-20191221235433734.png" alt="image-20191221235433734" style="zoom:80%;" />

### 编程原理与方法

1. tkinter库的使用

   ​      tkinter是Python的标准GUI库Python。

   ​      使用 tkinter可以快速的创建GUI应用程序。

2. 解数独的算法

- 为每个空位建立备选数字列表data_list。
- 判断数字是否重复，是否允许填入。
- 刷新备选数字列表(循环)。
- 对具有多个备选数字的位置依次尝试。类似深度优先遍历算法，一旦某位置的数字judge为True，则允许开始下一位置的猜测。

### 细节处理

-  判断输入的数独题目是否合理

<img src="C:\Users\hasee\AppData\Roaming\Typora\typora-user-images\image-20191222000839683.png" alt="image-20191222000839683" style="zoom: 67%;" />

<img src="C:\Users\hasee\AppData\Roaming\Typora\typora-user-images\image-20191222000854890.png" alt="image-20191222000854890" style="zoom:67%;" />



