class Account :
    def __init__(self,number,name,blance = 0):
        self.number= number
        self.name = name
        self.blance = blance

    def deposit( self , amount ) :
        try :
            if (amount <= 0) :
                raise ValueError
            else :
                self.blance += amount
        except ValueError :
            print ( "please input a positive number" )


    def withdraw( self , amount ) :
        try :
            if (amount > self.blance) :
                raise ValueError
            else :
                self.blance -= amount
        except ValueError :
            print ( "blance is not enough" )


# def main() :
#     acc = Account ( "1231245","Tina")
#     print ( "number =",acc.number )
#     print ( "name =",acc.name )
#     print ( "blance =",acc.blance )
#
#     acc.deposit(5000)
#     print ( "blacne= ",acc.blance )
#     acc.withdraw (2000)
#     print ( "blacne= ",acc.blance )
#
#     acc1 = Account ("655465","Stephen",10000)
#     print ( "number =" , acc1.number )
#     print ( "name =" , acc1.name )
#     print ( "blance =" , acc1.blance )
#
#     acc1.deposit ( 5000 )
#     print ( "blacne= " , acc1.blance )
#     acc1.withdraw ( 2000 )
#     print ( "blacne= " , acc1.blance )
#     print ( acc )
#     print ( acc1 )
#
#
# main()
