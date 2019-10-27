#coding:utf8

"""
责任链模式 -- 用于让多个对象处理一个请求时，或者用于预先不知道由哪个对象来处理某种特定请求时，其原则如下：

　　1、存在一个对象链（链表、树或者其他便捷的数据结构）。

　　2、一开始将请求发送给第一个对象，让其处理。

　　3、对象决定是否处理该请求。

　　4、对象将请求转发给下一个对象。

　　5、重复该过程，直到达到链尾。
"""


class Request():
    """
    具体请求类
    """
    def __init__(self, requestType ,requestContent, number = 0):
        """
        :param requestType: 请求类型
        :param requestContent: 请求内容
        :param number: 请假天数
        """
        self.requestType = requestType
        self.requestContent = requestContent
        self.number = number

    def commit(self,generalManager):
        ret = generalManager.handleRequest(self)
        print(ret)


class Manager():
    """
    经理抽象类,功能：设置上级，处理问题
    """
    def __init__(self, name):
        self.name = name

    def setSuccessor(self, successor):
        self.successor = successor

    def handleRequest(self, request):
        pass

class LineManager(Manager):
    """
    直属经理
    """
    def handleRequest(self, request):
        if request.requestType == 'Days_Off' and request.number < 3:
            return '%s:%s Num:%d Accepted OVER' % (self.name, request.requestContent, request.number)
        else:
            if self.successor != None:
                print('交给部门经理处理')
                return self.successor.handleRequest(request)

class DepartmentManager(Manager):
    """
    部门经理
    """
    def handleRequest(self, request):
        if request.requestType == 'Days_Off' and request.number < 7:
            return '%s:%s Num:%d Accepted OVER' % (self.name, request.requestContent, request.number)
        else:
            if self.successor != None:
                print('交给总经理处理')
                return self.successor.handleRequest(request)

class GeneralManager(Manager):
    """
    总经理
    """
    def handleRequest(self, request):
        if request.requestType == 'Days_Off':
            return '%s:%s Num:%d Accepted OVER' % (self.name, request.requestContent, request.number)

if __name__ == "__main__":
    lineManager = LineManager("LineManager")
    departmentManager = DepartmentManager("DepartmentManager")
    generalManager = GeneralManager("GeneralManager")
    lineManager.setSuccessor(departmentManager)
    departmentManager.setSuccessor(generalManager)
    # request = Request(requestType="Days_Off", requestContent="ASK 2 DASYS OFF", number=1)
    # request.commit(lineManager)
    # request = Request(requestType="Days_Off", requestContent="ASK 5 DASYS OFF", number=5)
    # request.commit(lineManager)
    request = Request(requestType="Days_Off", requestContent="ASK 9 DASYS OFF", number=9)
    request.commit(lineManager)

