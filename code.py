def isGreater(x, y) :
    if x > y and x > 0:
        return abs(x)
    elif x < y and y > 0 :
        return abs(y)
    else :
        return 1
        
def isLowerThanZero(x, y) :
    if x > y and y < 0 :
        return abs(y)
    elif x < y and x < 0 :
        return abs(x)
    else :
        return 1

class Point () :
    
    def __init__(self, x, y) :
        self.x = x
        self.y = y
        
    def __add__(self, other) :
        return Vector(self.x, self.y, other.x, other.y)
        
class Vector ():
    
    def __init__(self, x1, y1, x2, y2) :
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
class chart () :
    
    def __init__(self, other) :
        self.x1 = other.x1
        self.x2 = other.x2
        self.y1 = other.y1
        self.y2 = other.y2
        
    
    def setArr(self) :
        arr = []
        border = 1
        
        for i in range(isGreater(self.y1, self.y2) + isLowerThanZero(self.y1, self.y2) + 1 + (border*2)) :
            arr.append([])
            for j in range(isGreater(self.x1, self.x2) + isLowerThanZero(self.x1, self.x2) + 1 + (border*2)) :
                arr[i].append(" ")
                
        yAxis = (border + isLowerThanZero(self.x1, self.x2))
        xAxis = (border + isGreater(self.y1, self.y2))
        
        for i in range(len(arr)) :
            arr[i][yAxis] = "|"
        for i in range(len(arr[xAxis])) :
            arr[xAxis][i] = "-"
            
        arr[(-(self.y1)) + xAxis][(self.x1) + yAxis] = "+"
        arr[(-(self.y2)) + xAxis][(self.x2) + yAxis] = "+"
                
        for i in range(len(arr)) :
            print(arr[i])
        
a = Point(-2,-5)
b = Point(-10,-3)

aUb = a + b

chart(aUb).setArr()
