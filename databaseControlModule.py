import psycopg2
class DatabaseControl:
    def __init__(self):
        self.connection =  psycopg2.connect(database = "otel_otomasyon_db", user = "postgres", password = "Eminefe99*",host = "localhost", port = "5432")
        self.cursor = self.connection.cursor()
    # getOccupiedRooms fonksyonu ile anlık dolu odalar listelenir
    def getOccupiedRooms(self):
        self.cursor.execute('select number from otelotomasyon_db')
        cursorTupple = self.cursor.fetchall()
        roomNumbersList = []
        for i in cursorTupple:
            roomNumbersList.append(i[0])
        return roomNumbersList                   

    #Musteri kaydı icin veri tabanına baglama ve veri ekleme fonksyonu
    def customerRegistration(self,object):
        self.cursor.execute('insert into "otelotomasyon_db" (number,person1,person2,person3) values (%s,%s,%s,%s)',(object[0],object[1],object[2],object[3]))
        self.connection.commit()

    #Musteri cıkıs icin veri tabanından baglama ve veri silme fonksyonu    
    def customerCheckOut(self,checkOut):
        self.cursor.execute('delete from "otelotomasyon_db" where number = %s',(checkOut,))
        self.connection.commit()


    # getCustomerCount fonksyonu ile anlık musteri sayısı listelenir
    def getCustomerCount(self):
        self.cursor.execute('select * from otelotomasyon_db')
        cursorTupple = self.cursor.fetchall()
        customerCount = 0
        for i in cursorTupple:
            if i[1] != "null":
                customerCount += 1
            if i[2] != "null":
                customerCount += 1
            if i[3] != "null":
                customerCount += 1
        return customerCount

