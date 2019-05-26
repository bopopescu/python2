class parent:
    def m1( self ):
        print("parent:m1()")

    def m2( self ) :
        print ( "parent:m2()" )

class Child1(parent):
    def m3( self ):
        print("child1:m3()")
    def m2( self ):
        print("child1:m2()")

class Child2 ( parent ) :
    def m4( self ) :
        print ( "child1:m4()" )

def main():
    child1=Child1()
    child1.m1()
    child1.m2()
    child1.m3()
    child2=Child2()
    child2.m1()
    child2.m2()
    child2.m4()
main()