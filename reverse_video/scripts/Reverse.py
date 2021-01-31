import math
import numpy as np

L=300.0 #前后轮轴距
w=150.0 #轴长
D=80.0  #后轮距离车尾的距离

#计算外轮轨迹
def getZout(x, angle):
    Lcot = L * Cot(angle)
    firstStep = Square(Lcot + (w / 2)) - Square(x + Lcot)  # (Lcot(φ)+ w/2)^2
    if(firstStep<0):  #不存在此点时返回 -1
        return -1
    secondStep = math.sqrt(firstStep) - D
    return secondStep

#计算内轮轨迹
def getZin(x, angle):
    Lcot = L * Cot(angle)
    firstStep = Square(Lcot - (w / 2)) - Square(x + Lcot)  # (Lcot(φ)- w/2)^2
    if(firstStep<0):  #不存在此点
        return -1
    secondStep = math.sqrt(firstStep) - D
    return secondStep


# 求反切值 默认参数为弧度，需要角度转弧度。
def Cot(angle):
    cot = 1 / float(math.tan(angle * math.pi / 180))
    return cot

# 求平方
def Square(number):
    square = float(math.pow(number, 2))
    return square

# 求Tan 默认的参数为弧度，需要角度转弧度
def Tan(degreef):
    tan = float(math.tan(math.radians(degreef)))
    return tan

# 获得像素坐标集
def getPointArray(angle):
    #相机内参矩阵K
    K=np.mat([
        [100, 0, 100],
        [0, 100, 100],
        [0, 0, 1]
    ])
    array=[]

    #均匀采样
    y=-50 #摄像头与地面的高度
    for x in range(-100,100):
        z=getZout(x,angle)
        if(z<0):
            continue
        camera=np.mat([[x],[y],[int(z)]]) #相机坐标点
        point=(K*camera)/int(z)
        point = np.delete(point, 2).astype(int)
        point = point.A
        array.append(np.squeeze(point))


    for x in range(-100,100):
        z=getZin(x,angle)
        if(z<0):
            continue
        camera = np.mat([[x], [y], [int(z)]])  # 相机坐标点
        point = (K * camera) / int(z)
        point = np.delete(point, 2).astype(int)
        point = point.A
        array.append(np.squeeze(point))

    return array