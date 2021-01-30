import math

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

