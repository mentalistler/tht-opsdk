from tools import PanelFind
from tools import colorprint
from tools import SQLVulnDetector
from tools import dorkwithselenium

def main():
    while(True):
        colorprint.colorprint("Yapmak istediğiniz işlemi seçin")
        print("1) Dork Tara")
        print("2) SQL Injection Kontrolü")
        print("3) Panel Tara")
        print("4) Hızlı Panel Tara")
        print("5) Dork Tara > SQL Injection > Panel Tara")
        print("6) Dork Tara > SQL Injection > Hızlı Panel Tara")

        usr = int(input(">> "))
        if(usr == 1):
            colorprint.colorprint("Dork tarama işlemi başlatıldı!")
            dorkwithselenium.aramamotoru()
            colorprint.colorprint("Dork tarama işlemi tamamlandı!")
        elif(usr == 2):
            UrlList = open("files/results.txt", "r").read().splitlines()
            colorprint.colorprint("SQL Injection kontrol işlemi başlatıldı!")
            SQLVulnDetector.VulnMain(UrlList,20) 
            colorprint.colorprint("SQL Injection kontrol işlemi tamamlandı!")

        elif(usr == 3):
            colorprint.colorprint("Panel Tarama işlemi başlatıldı!")
            PanelFind.main(0)
            colorprint.colorprint("Panel Tarama işlemi tamamlandı!")

        elif(usr == 4):
            colorprint.colorprint("Hızlı Panel Tarama işlemi başlatıldı!")
            PanelFind.main(1)
            colorprint.colorprint("Hızlı Tarama işlemi tamamlandı!")
        elif(usr==5):
            colorprint.colorprint("Dork tarama işlemi başlatıldı!")
            dorkwithselenium.aramamotoru()
            colorprint.colorprint("Dork tarama işlemi tamamlandı!")
            UrlList = open("results/results.txt", "r").read().splitlines()
            colorprint.colorprint("SQL Injection kontrol işlemi başlatıldı!")
            SQLVulnDetector.VulnMain(UrlList,20) 
            colorprint.colorprint("SQL Injection kontrol işlemi tamamlandı!")
            colorprint.colorprint("Panel Tarama işlemi başlatıldı!")
            PanelFind.main(0)
            colorprint.colorprint("Panel Tarama işlemi tamamlandı!")
        elif(usr==6):
            colorprint.colorprint("Dork tarama işlemi başlatıldı!")
    #        dorkwithselenium.aramamotoru()
            colorprint.colorprint("Dork tarama işlemi tamamlandı!")
            UrlList = open("results/results.txt", "r").read().splitlines()
            colorprint.colorprint("SQL Injection kontrol işlemi başlatıldı!")
   #         SQLVulnDetector.VulnMain(UrlList,20) 
            colorprint.colorprint("SQL Injection kontrol işlemi tamamlandı!")
            colorprint.colorprint("Panel Tarama işlemi başlatıldı!")
            PanelFind.main(1)
            colorprint.colorprint("Panel Tarama işlemi tamamlandı!")
        else:
            colorprint.colorprint("Lütfen yapmak istediğiniz işlemi doğru girin.","v")
main()