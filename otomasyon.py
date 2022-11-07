


class Sirket():
    def __init__(self,ad):
        self.ad = ad
        self.calisma = True
    
    def program(self):
        secim = self.menuSecim()

        if secim == 1:
            self.calisanEkle()
        if secim == 2:
            self.calisanCikar()
        if secim == 3:
            ay_yil_secim = input("Yıllık bazda görmek ister misiniz? (e/h)")
            if ay_yil_secim == "e":
                self.verilecekMaasGoster(hesap="y")
            else:    
                self.verilecekMaasGoster()
        if secim == 4:
            self.maaslariVer()
        if secim == 5:
            self.masrafGir()
        if secim == 6:
            self.gelirGir()

    def menuSecim(self):
        secim = int(input("****{} otomasyonuna hoşgeldiniz ****\n\n1-Çalışan Ekle\n2-Çalışan Çıkar\n3-Verilecek Maaşı Göster\n4-Maaşları Ver\n5-Masraf Gir\n6-Gelir Gir\n\nSeçiminizi giriniz:".format(self.ad)))
        while secim <1 or secim >6:
            secim = int(input("Lütfen 1 ile 6 arasında bir seçim yapınız:"))
        return secim

    def calisanEkle(self):
        id = 1
        ad = input ("Çalışanın adınız giriniz:")   
        soyad = input ("Çalışanın soyadını giriniz:")   
        yas = input ("Çalışanın yaşını giriniz:")   
        cinsiyet = input ("Çalışanın cinsiyetini giriniz:")   
        maas = input ("Çalışanın maaşını giriniz:")  

        with open ("calisanlar.txt","r") as dosya:
            calisanListesi = dosya.readlines()

        if len(calisanListesi) == 0:
            id = 1
        else:
            with open ("calisanlar.txt","r") as dosya:
                id = int(dosya.readlines()[-1].split(")")[0]) + 1

        with open ("calisanlar.txt","a+") as dosya:
            dosya.write("{}){}-{}-{}-{}-{}\n".format(id,ad,soyad,yas,cinsiyet,maas))
       
    def calisanCikar(self):
        with open("calisanlar.txt","r") as dosya:
          calisanlar = dosya.readlines()
       
        gCalisanlar =[]
       
        for calisan in calisanlar:
          gCalisanlar.append(" ".join(calisan[:-1].split("-")))

        for calisan in gCalisanlar:
            print(calisan)
        
        secim = int(input("Lütfen çıkarmak istediğiniz kullanıcının numarasını giriniz(1-{}:".format(len(gCalisanlar))))
        while secim < 1 or secim > len(gCalisanlar):
         secim = int(input("Lütfen (1-{}) arasında numara giriniz: ".format(len(gCalisanlar))))

        calisanlar.pop(secim - 1)

        sayac = 1
        dCalisanlar = []

        for calisan in calisanlar:
          dCalisanlar.append(str(sayac) + ")" + calisan.split(")")[1])
          sayac += 1
        
        with open ("calisanlar.txt","w") as dosya:
            dosya.writelines(dCalisanlar)


    def verilecekMaasGoster(self,hesap = "a"):
        with open ("calisanlar.txt","r") as dosya:
            calisanlar = dosya.readlines()
        maaslar = []

        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-1]))
        
        if hesap == "a":
            print("Bu ay vermeniz gereken toplam maaş:{}".format(sum(maaslar)))
        else:
            print("Bu yıl vermeniz gereken toplam maaş:{}".format(sum(maaslar)*12))
        
    def maaslariVer(self):
        with open ("calisanlar.txt","r") as dosya:
            calisanlar = dosya.readlines()

        maaslar = []

        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-1]))

        toplamMaas = sum(maaslar)

        with open("butce.txt","r") as dosya:
            tbutce = int(dosya.readlines()[0])
        
        tbutce = tbutce - toplamMaas

        with open("butce.txt","w") as dosya:
            dosya.write(str(tbutce))
        


sirket = Sirket ("Elmas Company")
while sirket.calisma:
    sirket.program()

