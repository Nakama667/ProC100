class Atm:
    def __init__(self,cardNumber) :
        self.cardNumber = cardNumber

    def Verify (self):
        yourCard = int(input("Digite o numero do seu cartão: "))
        if self.cardNumber == yourCard:
            print("Verified")
        else:
            print("Wrong Number")
c1 = Atm(1234321)
c1.Verify()