class Point:
    def __init__(self,x,y):

        self.x=x
        self.y=y
    def __str__( self ):
        return"{},{}".format(self.x,self.y)
    def __add__(self, other):
        x = self.x+other.x
        y= self.y+other.y
        return Point(x,y)

    # def __eq__( self,other ):
    #     x= self.x==other.x
    #     y= self.y==other.y
    #     return Point(x,y)

    # def __eq__(self, other):
    #     if self.x==other.x and self.y==other.y:
    #         return True
    #     else :
    #         return  False


    # def __eq__( self , other ) :
    #     return True if self.x==other.x and self.y==other.y else  False

    def __eq__( self , other ) :

        return self.x==other.x and self.y==other.y

def main():

    p1=Point(20,30)
    print(p1)
    p2 = Point (20 ,30 )
    print ( p2 )
    print(p1+p2)
    print ( p1 == p2 )

main()