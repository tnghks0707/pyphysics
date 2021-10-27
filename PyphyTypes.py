import PyphyObject

def toClass(str):
    if(str == "Ground"):
        return Ground

class Type:
    TypeNumber = 0

    def __init__(self):
        pass

    def TypeName(self):
        return None

#중력가속도에 영향을 받지 않고, 물체와 충돌했을 때 대부분의 운동량을 흡수함
class Ground(Type):
    def getTypeName(self):
        return "Ground"
