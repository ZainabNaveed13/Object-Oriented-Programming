from datetime import datetime
class address:

    def __init__(self, street, area, city):
        self.street = street
        self.area = area
        self.city = city

    def __str__(self):
        vstr = ""
        vstr+= str(self.street) + ',' + str(self.area) + ',' + str(self.city)
        return vstr

class items:

    def __init__(self, pt, rt, qty):
        self.pt = pt
        self.rate = rt
        self.qty =  qty

    def __str__(self):
        vstr =''
        vstr+= str(self.pt) +'  \t\t\t' +str(self.rate) +'\t\t'+str(self.qty)
        return vstr

class Bill:

    def __init__(self, No, Date, Name, Adress, item):
        self.no = No
        self.date = Date
        self.Name = Name
        self.Adress = Adress
        self.items = item

    def __str__(self):
        T = 0
        vstr =''
        vstr += "MOBILO"+'\n'
        vstr += "Mobile City"+'\n'
        vstr += "Deals in all kinds of Mobile sets and accsessories"+'\n'
        vstr += "Cell No:0321_0000000"+'\n'
        vstr += "CASHMENO"+'\n'+'NO:'+str(self.no)+'\n'
        vstr += "DATE:" + str(self.date.strftime('%d-%b-%Y'))+'\n'
        vstr += "CUSTOMER NAME:"+str(self.Name) +'\n'
        vstr += "CUSTOMER ADRESS:" + str(self.Adress) +'\n'
        vstr += "Particulars\t\t\t" + "Qty\t\t"+"Rate" +'\n'
        for i in range(len(self.items)):
            T += (self.items[i].qty*self.items[i].rate)
            vstr += str(self.items[i])+'\n'
        vstr+='\n'
        vstr += "Signature:" + "\t\t\t\t" +"Total : " +str(T)+'\n'+'\n'
        vstr += "Adress:Basement #2 ,Allahwala Plaza,Markaz K8,Islamabad"
        return vstr

def main():
    B1 = Bill(998, datetime.now(),"Usman", address('Street#2',"Canal bank","LHR"),
    [items("Mouse", 1, 2000),
    items("Handfree", 2, 700),
    items("Keyboard",1,3500),
    items("Card",2,1800)])
    print(B1)
    print("____________________________________")
    print("____________________________________")
    B2 = Bill(999, datetime.now(),"Usman", address('Street#3',"Gulberg","LHR"),
    [items("Mouse", 1, 1500),
    items("Handfree", 2, 600),
    items("Keyboard",3,3500),
    items("Card",4,2000)])
    print(B2)

if __name__=="__main__":
    main()
