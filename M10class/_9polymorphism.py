class Dog:
    def run( self ):
        print('Dog:run()')
    def eat( self ):
        print("Dog:eat()")

class Tiger:
    def run( self ):
        print('Tiger:run()')
    def eat( self ) :
        print ( "Tiger:eat()" )

class Horse:
    def run( self ):
        print('Horse:run()')
    def eat( self ) :
        print ( "Horse:eat()" )

def main1(): #yi ban xie fa


    dog = Dog()
    dog.run()
    tiger = Tiger ( )
    tiger.run ( )
    horse= Horse()
    horse.run()
    print("------------")

    # test(dog)
    # test(tiger)
    # test(horse)
main1()


def test( animal ) :
    animal.run ( )
    animal.eat()
    print("-------------")
def main2():
    dog = Dog()
    dog.run()
    tiger = Tiger ( )
    tiger.run ( )
    horse= Horse()
    horse.run()
    test(dog)
    test(tiger)
    test(horse)
main2()
