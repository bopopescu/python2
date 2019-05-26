from M10class._3account2str import Account
class CheckingAccount(Account):
    def __init__(self,number,name,blance = 0,credit_limit=10000):
        super(CheckingAccount,self).__init__(number,name,blance)
        self.credit_limit = credit_limit

        # self.number= number
        # self.name = name
        # self.blance = blance
        # self.creditlimit =creditlimit
    def withdraw( self , amount ) :
        try :
            if (amount > self.blance +self.credit_limit) :
                raise ValueError
            else :
                self.blance -= amount
        except ValueError :
            print ( "over credit limit" )

    def __str__ ( self ):
        return super(CheckingAccount, self).__str__() \
               + ',credit_limit={}'.format(self.credit_limit) #super for over write
# def main():
#    ca= CheckingAccount("11111111111",'jean',5000)
#    ca.deposit(3000)
#    print(ca.blance)
#    ca.withdraw(13000)
#    print(ca.blance)
#
# main()

