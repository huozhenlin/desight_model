"""
工厂模式，是通过专门设计一个类来负责创建其他类，被创建的实例拥有共同的父类
"""


# 四则运算抽象类
class Operation(object):

    def __init__(self, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2

    def getResult(self):
        pass


# 加法运算类
class OpeartionAdd(Operation):

    def getResult(self):
        return self.num1 + self.num2


# 减法运算类
class OpeartionSub(Operation):

    def getResult(self):
        return self.num1 - self.num2


# 乘法运算类
class OpeartionMul(Operation):

    def getResult(self):
        return self.num1 * self.num2


# 除法运算类
class OpeartionDiv(Operation):

    def getResult(self):
        if self.num2 == 0:
            return "被除数不能为0"
        return self.num1 / self.num2


# 未知运算符
class OpeartionUndefind(Operation):

    def getResult(self):
        return '操作符号错误'


# 具体策略类
class Context():

    def __init__(self, ch):
        self.ch = ch
        self.mapping = {"+": OpeartionAdd, "-": OpeartionSub, "/": OpeartionDiv, "*": OpeartionMul}

    def GetResult(self):
        if self.ch in self.mapping:
            return self.mapping.get(self.ch)
        else:
            return OpeartionUndefind


# 简单工厂类
class OperationFactory(object):

    def choose_oper(self, ch):
        return Context(ch).GetResult()()


if __name__ == '__main__':
    oper = '*'  # 操作符
    OF = OperationFactory()
    oper_obj = OF.choose_oper(oper)
    oper_obj.num1 = 10
    oper_obj.num2 = 10
    result = oper_obj.getResult()
    print(result)
