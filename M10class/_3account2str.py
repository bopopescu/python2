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
    def __str__(self):
        return 'number= {}, name = {} ,blance ={}'.format(self.number, self.name,self.blance )
#
# def main() :
#     acc = Account ( "1231245","Tina")
#     print ( "number =",acc.number )
#     print ( "name =",acc.name )
#     print ( "blance =",acc.blance )
#     print ( acc )
#
#
# main()
