class Dosya():
    def __init__(self):
        with open("metin.txt","r",encoding="utf-8") as file:
            dosya_içerigi =file.read()
            kelimeler =dosya_içerigi.split()
            self.sade_kelimeler = list()
            for i in kelimeler:
                i = i.strip("\n")
                i=i.strip(" ")
                i= i.strip(".")
                i=i.strip(",")
                self.sade_kelimeler.append(i)
            for i in self.sade_kelimeler:
                print(i)
    def tum_kelimeler(self):
        kelimeler_kumesi = set()
        for i in self.sade_kelimeler:
            kelimeler_kumesi.add(i)
        print("<<<<Tüm Kelimeler>>>>")
        for i in kelimeler_kumesi:
            print(i)
            print("********************************")
    def kelime_frekansı(self):
        kelime_sozlük =dict()
        for i in self.sade_kelimeler:
            if(i in kelime_sozlük):
                kelime_sozlük[i]+=1
            else:
                kelime_sozlük[i]=1
        for kelime,sayı in kelime_sozlük.items():
            print("{} kelimesi {} defa geçiyor".format(kelime,sayı))
            print("----------------------------------------------")
dosya = Dosya()
dosya.kelime_frekansı()