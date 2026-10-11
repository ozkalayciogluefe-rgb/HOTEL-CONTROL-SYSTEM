#OTEL OTOMASYON SİSTEMİ..
import databaseControlModule as dbControl
conn = dbControl.DatabaseControl()
import json
class text:
    def __init__(self,folderName):
        self.folderName = folderName

    def read(self):
        f = open(self.folderName , "r")  
        init = json.load(f)
        return init
       
    def write(self ,list_):
        f = open(self.folderName,"w")
        json.dump(list_,f,indent = 4)
        f.close()

# roomCapacity
def personSelection(howPersonRoom,personSelect):
    try:
        for i in range(len(howPersonRoom)):
            if howPersonRoom[i] not in roomNumbersList:
                name1 = input("1. kisi ad soyad giriniz : ")
                name2 = input("2. kisi ad soyad giriniz : ")

                object = [howPersonRoom[i],name1,name2,"null"]

                if personSelect == 3:
                    object[3] = input("3.kisi ad soyad giriniz : ")


                conn.customerRegistration(object)
                print(f"{howPersonRoom[i]} numaralı oda kaydınız basarıyla yapıldı")
                
                
                break
    except IndexError:
        print(f"{personSelect} kisilik odalar dolu")   




rooms= text("./rooms.json")
twoPersonRoom = rooms.read()["twoPersonsRoom"]
threePersonRoom = rooms.read()["threePersonsRoom"]


roomNumbersList = conn.getOccupiedRooms()

while True:

    print("""
    lutfen Musteri kayıt icin 1'e 
    musteri cıkıs icin 2'ye 
    anlık dolu odalar icin 3'e 
    anlık musteri sayısı icin 4'e 
    basınız""")

    try:
        selection = int(input())

        if selection in [1,2,3,4]:
            break
        else:
            print("lutfen 1 2 3 veya 4 u secin")

    except ValueError:
        print("lutfen gecerli deger giriniz")        


if selection == 1:

    print("kac kisilik oda lazım 2 mi 3 mu ")

    while True: 
        try:
            personSelect = int(input())

            if personSelect in [2,3]:
                break 
            else:
                print("boyle bir oda yok lutfen 2 veya 3 secin")

        except ValueError:
            print("gecerli deger giriniz")

    if personSelect == 2:
        personSelection(twoPersonRoom,personSelect)
        
    elif personSelect == 3:
        personSelection(threePersonRoom,personSelect)
        
elif selection == 2:
    checkOut = input("lutfen cıkıs yapacagınız oda numarasını giriniz : ")
    conn.customerCheckOut(checkOut)

elif selection == 3:
    if roomNumbersList != []:
        roomNumbersList.sort()
        for i in roomNumbersList:
            print(f"{i} numaralı oda dolu")
    else:
        print("dolu oda yok")

elif selection == 4:
    holder = 0
    cursorTupple = conn.getCustomerCount()
    print(f"anlık oteldeki musteri sayısı : {cursorTupple}")
    


               
