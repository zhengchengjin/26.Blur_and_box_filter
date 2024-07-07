#5.2 方盒滤波与均值滤波
#boxFilter(src,ddepth,ksize[,dst[,anchor[,normalize[,borderType]]]])方盒滤波
#src是要进行卷积的原图片
#ddepth是卷积之后图片的位深，即卷积之后图片的数据类型，一般设为-1，表示核原图类型一致
#kernel是卷积核的大小，用元组或者ndarray表示，要求数据类型必须是float型
#anchor锚点，即卷积核的中心点，是可选参数，默认是(-1,-1)
#normalize：
#normalize=True时，a=1/（W*H）滤波器的宽高
#normalize=False时，a=1
#一般情况下我们都使用normal=True的情况，这时 方盒滤波 等价于 均值滤波
#borderType边界类型，一般不设
#方盒滤波的卷积核的形式如下：
# K=a[1 1 1 ... 1 1]
#    [1 1 1 ... 1 1]
#    [.............]
#    [1 1 1 ... 1 1]
#blur(src,ksize[,dst[,anchor[,borderType]]]) 均值滤波


import cv2
import numpy as np

blueberry = cv2.imread('./blueberry.jpg')

# #方盒滤波
# #不用手动创建卷积核，只需要告诉方盒滤波，卷积核的大小是多少
# box_blueberry = cv2.boxFilter(blueberry,-1,(5,5),normalize = True)#会进行自动补全（补零），即自动设置合适的padding，保证和原图一样大
# #注：第一个参数：要进行卷积的图片 第二个参数：卷积之后图片的位深 第三个参数：卷积核大小 第四个参数（normalize）一般为True
#
# cv2.imshow('box_blueberry',np.hstack((blueberry,box_blueberry)))
#
# cv2.waitKey(0)
# cv2.destoryAllWindows()

#均值滤波

blur_blueberry = cv2.blur(blueberry,(5,5))#会进行自动补全（补零），保证和原图一样大
# 滤波无“位深（ddepth）”和“normalize”这两个参数

cv2.imshow('blur_blueberry',np.hstack((blueberry,blur_blueberry)))

cv2.waitKey(0)
cv2.destroyAllWindows()

