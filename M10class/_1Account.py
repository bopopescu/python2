class Account :
    pass


def deposit( acc , amount ) :
    try :
        if (amount <= 0) :
            raise ValueError
        else :
            acc.blance += amount
    except ValueError :
        print ( "please input a positive number" )


def withdraw( acc , amount ) :
    try :
        if (amount > acc.blance) :
            raise ValueError
        else :
            acc.blance -= amount
    except ValueError :
        print ( "blance is not enough" )


def main() :
    acc = Account ( )
    acc.number = "1231245"
    acc.name = "Tina"
    acc.blance = 0

    print ( "number =",acc.number )
    print ( "name =",acc.name )
    print ( "blance =",acc.blance )

    acc1 = Account ( )
    acc1.number = "655465"
    acc1.name = "Stephen"
    acc1.blance = 100000

    deposit(acc1,3000)
    withdraw ( acc1 , 4000 )

    print ( acc1.number )
    print ( acc1.name )
    print ( acc1.blance )


main ( )
