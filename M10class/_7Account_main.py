from M10class._3account2str import   Account

from M10class._5checkingaccount1 import CheckingAccount


def main():
    acc =  Account ("655465","Stephen",10000)#class._3account2str
    acc.deposit(8000)
    print(acc)#acc.blance
    acc.withdraw(6000)
    print(acc)#acc.blance

    ca= CheckingAccount("11111111111",'jean',5000,20000)#M10class._5checkingaccount1
    ca.deposit(3000)
    print(ca)#(ca.blance)
    ca.withdraw(13000)
    print(ca)#(ca.blance) 繼承__STR

main()