#OTEL OTOMASYON SİSTEMİ..


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

                object = {
                    "number" : howPersonRoom[i],
                    "person1" : name1,
                    "person2" : name2
                }

                if personSelect == 3:
                    object["person3"] = input("3. kisi ad soyad giriniz : ")
                
                
                
                ctrlFPerson["rooms"].append(object)
                filePerson.write(ctrlFPerson)
                break
    except IndexError:
        print(f"{personSelect} kisilik odalar dolu")   



filePerson = text("./hotell.json")
rooms= text("./rooms.json")
twoPersonRoom = rooms.read()["twoPersonsRoom"]
threePersonRoom = rooms.read()["threePersonsRoom"]
ctrlFPerson = filePerson.read()
roomNumbersList = []

for i in ctrlFPerson["rooms"]:
    roomNumbersList.append(i["number"])

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
    checkOut = int(input("lutfen cıkıs yapacagınız oda numarasını giriniz : "))
    for room in ctrlFPerson["rooms"]:
        if room["number"] == checkOut:
            ctrlFPerson["rooms"].remove(room)
            break  
    filePerson.write(ctrlFPerson)     

elif selection == 3:
    if ctrlFPerson["rooms"] != []:
        for room in ctrlFPerson["rooms"]:
            roomNumber = room["number"]
            guests = []

            for person in room:
                if room[person] != "" and person != "number":
                    guests.append(room[person])
            print(f"{roomNumber} numaralı odadaki musteriler {guests}")        
    else:
        print("dolu oda yok")

elif selection == 4:
    holder = 0
    for room in ctrlFPerson["rooms"]:
        for person in room:
            if room[person] != "" and person != "number":
                holder += 1
    print(f"Oteldeki musteri sayisi {holder}")
               
