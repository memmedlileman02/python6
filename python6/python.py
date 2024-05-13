class bank:
    def __init__(self, kart, balans=0):
        self.kart = kart
        self.balans = balans

    def balansGoster(self):
        return self.balans

    def balansArtir(self, miqdar):
        self.balans += miqdar
        return f"{miqdar} AZN balansiniza elave edildi. Sizin yeni balansiniz: {self.balans} AZN"

    def balans_cixart(self, miqdar):
        if self.balans >= miqdar:
            self.balans -= miqdar
            return f"{miqdar} AZN pul cekdiniz.Sizin yeni  balansiniz: {self.balans} AZN"
        else:
            return "balansinizda kifayet qeder vesait yoxdur!"

class kredit(bank):
    def __init__(self, kart, kredit_miqdari=0):
        super().__init__(kart)
        self.kredit_miqdari = kredit_miqdari

    def kredit_vermek(self, miqdar):
        self.kredit_miqdari += miqdar
        return f"{miqdar} AZN kredit cekdiniz. Sizin umumi kredit miqdariniz: {self.kredit_miqdari} AZN"

    def kredit_odenis(self):
        return self.kredit_miqdari / 12

bank_hesab = bank("Kapital bank")
print(bank_hesab.balansGoster()) 
print(bank_hesab.balansArtir(50000)) 
print(bank_hesab.balans_cixart(1000))  
print(bank_hesab.balans_cixart(100)) 


kredi_karti = kredit("Kapital bank")
print(kredi_karti.kredit_vermek(20000)) 
# print(f"{kredi_karti.kredit_odenis():.2f}")
