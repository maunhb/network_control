
class Pigou_3_os():
    def __init__(self,degree=1):
        self.degree = degree

    def cost_1(self,x1,x2,x3):
        return 1
    def cost_2(self,x1,x2,x3):
        return  (x1 + x2 + x3)**self.degree

    def social_cost_1(self,x1,x2,x3,p1):
        return (p1-x1)*self.cost_1(x1,x2,x3) + x1*self.cost_2(x1,x2,x3)
    def social_cost_2(self,x1,x2,x3,p2):
        return (p2-x2)*self.cost_1(x1,x2,x3) + x2*self.cost_2(x1,x2,x3)
    def social_cost_3(self,x1,x2,x3,p3):
        return (p3-x3)*self.cost_1(x1,x2,x3) + x3*self.cost_2(x1,x2,x3)
    def social_cost(self,x1,x2,x3):
        return (1-x1-x2-x3)*self.cost_1(x1,x2,x3) + (x1+x2+x3)*self.cost_2(x1,x2,x3) 


class Pigou_2_os():
    def __init__(self,degree=1):
        self.degree = degree

    def cost_1(self,x1,x2):
        return 1
    def cost_2(self,x1,x2):
        return  (x1 + x2)**self.degree

    def social_cost_1(self,x1,x2,p1):
        return (p1-x1)*self.cost_1(x1,x2) + x1*self.cost_2(x1,x2)
    def social_cost_2(self,x1,x2,p2):
        return (p2-x2)*self.cost_1(x1,x2) + x2*self.cost_2(x1,x2)
    def social_cost(self,x1,x2):
        return (1-x1-x2)*self.cost_1(x1,x2) + (x1+x2)*self.cost_2(x1,x2) 
