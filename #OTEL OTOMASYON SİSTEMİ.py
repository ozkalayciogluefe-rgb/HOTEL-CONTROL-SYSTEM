#OTEL OTOMASYON SİSTEMİ
class text:
    def __init__(self,folderName):
        self.folderName = folderName

    def read(self):
       f = open(self.folderName , "r")  
       init = f.read()
       return init

    def write(self ,list_):
        f = open(self.folderName,"a")
        writeing = f.write(str(list_))
        return writeing

    def delete(self,fp,checkOut):
        f = open(self.folderName,"w")
        f.close()
        for i in fp:
            if checkOut in i:
                fp.remove(i)
        for x in fp:
            f = open(self.folderName,"a")        
            f.write(str(x) + '\n')

    def lenPersons(self,lp):
        f = open(self.folderName,"r")
        lp = f.readlines()
        return lp

twoPersonRoom = [121,122,123,124,125,126,127,128,129]
threePersonRoom = [131,132,133,134,135,136,137,138,139]
filePerson = text("persons.txt")
ctrlFPerson = filePerson.read().split("/")
fp = list(filePerson.read().splitlines())
printing = filePerson.read()
holder = 0

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
        try:
            for i in range(0,10):
                if str(twoPersonRoom[i]) not in ctrlFPerson:
                    filePerson.write("/" + str(twoPersonRoom[i]) + "/")
                    name = input("lutfen ad soyad giriniz ")
                    filePerson.write(name + "/" + '\n')
                    break
        except IndexError:
            print("iki kisilik odalar dolu")

    if personSelect == 3:
        try:
            for i in range(0,10):
                if str(threePersonRoom[i]) not in ctrlFPerson:
                    filePerson.write("/" + str(threePersonRoom[i]) + "/")
                    name = input("lutfen ad soyad giriniz ")
                    filePerson.write(name + "/" + '\n')
                    break
        except IndexError:
            print("3 kisilik odalar dolu")   

elif selection == 2:
    checkOut = input("lutfen cıkıs yapacagınız oda numarasını giriniz : ")
    filePerson.delete(fp,checkOut)

elif selection == 3:
    print(filePerson.read())

elif selection == 4:
    holder = 0
    for i in fp:
        counter = 0
        if i != '':
            for x in i:
                if x == ",":
                    counter += 1
            holder += counter + 1
    print(holder) 




    
               
               