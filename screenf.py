order={}
def bill():
    print("        MODE OF PAYMENT     ")
    print("1. Pay on Delivery")
    print("2. Pay Online")
    mop=int(input("Choose Payment Mode: "))
    if mop==1:
        print("Keep Your Cash/Card Ready!")
        print("YOUR ORDER WILL BE DELIVERED SHORTLY!!")
        print("Our Valet is on his Way With your Piping Hot Food")
    elif mop==2:
        print("1.Credit Card\n2.Debit Card")
        p=int(input("Enter your choice: "))
        if p==1:
            print("1.VISA Card\n2.Master Card\n3.Diners Club\n4.American Express")
            k=int(input("Enter your choice: "))
            if k==1 or k==2:
                cnam=input("Enter card holder name: ")
                cnum=input("Enter card number: ")
                while True:
                    ccheck=False
                    cvv=input("Enter CVV: ")
                    for i in cvv:
                        if i in '1234567890':
                            ccheck=True
                    if len(cvv)==3 and ccheck==True:
                            break
                    else:
                        print("INVALID CVV")
                while True:
                    forma=False
                    date=input("Enter month and year of card expiry in MM-YYYY format: ")
                    l=date.split("-")
                    h=l[0]
                    g=l[1]
                    if len(h)==2 or len(h)==1 and len(g)==4:
                        forma=True
                    if forma==True:
                        break
                    else:
                        print("Enter valid month and year of card expiry in proper format")
                print("Payment Successful!")
                print()
                print("YOUR ORDER WILL BE DELIVERED SHORTLY!!")
                print("Our Valet is on his Way With your Piping Hot Food")

            elif k==3:
                cnam=input("Enter card holder name: ")
                cnum=input("Enter card number: ")
                while True:
                    ccheck=False
                    cvv=input("Enter CVV: ")
                    for i in cvv:
                        if i in '1234567890':
                            ccheck=True
                    if len(cvv)==3 and ccheck==True:
                            break
                    else:
                        print("INVALID CVV")
                while True:
                    forma=False
                    date=input("Enter month and year of card expiry in MM-YYYY format: ")
                    l=date.split("-")
                    h=l[0]
                    g=l[1]
                    if len(h)==2 or len(h)==1 and len(g)==4:
                        forma=True
                    if forma==True:
                        break
                    else:
                        print("Enter valid month and year of card expiry in proper format")
                print("Payment Successful!")
                print()
                print("YOUR ORDER WILL BE DELIVERED SHORTLY!!")
                print("Our Valet is on his Way With your Piping Hot Food")
            elif k==4:
                cnam=input("Enter card holder name: ")
                cnum=input("Enter card number: ")
                while True:
                    ccheck=False
                    cvv=input("Enter CVV: ")
                    for i in cvv:
                        if i in '1234567890':
                            ccheck=True
                    if len(cvv)==3 and ccheck==True:
                            break
                    else:
                        print("INVALID CVV")
                while True:
                    forma=False
                    date=input("Enter month and year of card expiry in MM-YYYY format: ")
                    l=date.split("-")
                    h=l[0]
                    g=l[1]
                    if len(h)==2 or len(h)==1 and len(g)==4:
                        forma=True
                    if forma==True:
                        break
                    else:
                        print("Enter valid month and year of card expiry in proper format")
                print("Payment Successful!")
                print()
                print("YOUR ORDER WILL BE DELIVERED SHORTLY!!")
                print("Our Valet is on his Way With your Piping Hot Food")
            else:
                print("INVALID INPUT")
        elif p==2:
            print("1.VISA Card\n2.Master Card")
            k=int(input("Enter your choice: "))
            if k==1 or k==2:
                cnam=input("Enter card holder name: ")
                cnum=input("Enter card number: ")
                while True:
                    ccheck=False
                    cvv=input("Enter CVV: ")
                    for i in cvv:
                        if i in '1234567890':
                            ccheck=True
                    if len(cvv)==3 and ccheck==True:
                            break
                    else:
                        print("INVALID CVV")
                while True:
                    forma=False
                    date=input("Enter month and year of card expiry in MM-YYYY format: ")
                    l=date.split("-")
                    print(l)
                    h=l[0]
                    g=l[1]
                    if len(h)==2 or len(h)==1 and len(g)==4:
                        forma=True
                    if forma==True:
                        break
                    else:
                        print("Enter valid month and year of card expiry in proper format")
                print("Payment Successful!")
                print()
                print("YOUR ORDER WILL BE DELIVERED SHORTLY!!")
                print("Our Valet is on his Way With your Piping Hot Food")
def food():
    import tkinter
    while True:
            print("Available cuisines are:\n1.Greek\n2.French\n3.Italian\n")
            cuisine=int(input("Choose your Cuisine please: "))
            if cuisine==1:
                print()
                print("1.Starters\n2.Main Course\n3.Dessert")
                corse=int(input("Choose what you want to eat: "))
                if corse==1:
                    while True:
                        import csv
                        
                        f=open("GreekStarters.csv")
                        x=csv.reader(f,delimiter=",")
                        f=open("GreekStarters.txt", "r")
                        lst=[]
                        for i in range(5):
                            s=f.readline()
                            ns=s.replace("\n", "")
                            t=ns.split(",")
                            lst.append(t)
                        class Table:
                              def __init__(self,root):
                                  for i in range(5):
                                    for j in range(3):
                                          self.e = tkinter.Entry(root, width=35, font=('Freestyle Script',20,'bold'), justify = tkinter.CENTER, bg = "cadetblue1")
                                          self.e.grid(row=i, column=j)
                                          self.e.insert(tkinter.END, lst[i][j])

                        root = tkinter.Tk()
                        root.title("Greek Starters")
                              

                        t = Table(root)
                        root.mainloop()
                        

                        bev=input("Enter desired order code: ")
                        qty=int(input("Enter quantity: "))
                        f=open("GreekStarters.csv")
                        x=csv.reader(f,delimiter=",")
                        for i in x:
                            if i[0]==bev:
                                rate=int(i[3])*qty
                                bnam=i[1]
                            
                        f.close()
                        d={}
                        d[bnam]=rate
                        order.update(d)
                        ch=input("Press y to order more Greek starters or any other key to exit: ")
                        if ch!='y':
                            break
                elif corse==2:
                    while True:
                        import csv
                        f=open("GreekMaincourse.csv")
                        x=csv.reader(f,delimiter=",")
                        f=open("GreekMaincourse.csv")
                        x=csv.reader(f,delimiter=",")
                        f=open("GreekMaincourse.txt", "r")
                        lst=[]
                        for i in range(5):
                            s=f.readline()
                            ns=s.replace("\n", "")
                            t=ns.split(",")
                            lst.append(t)
                        class Table:
                              def __init__(self,root):
                                  for i in range(5):
                                    for j in range(3):
                                          self.e = tkinter.Entry(root, width=35, font=('Freestyle Script',20,'bold'), justify = tkinter.CENTER, bg = "cadetblue1")
                                          self.e.grid(row=i, column=j)
                                          self.e.insert(tkinter.END, lst[i][j])

                        root = tkinter.Tk()
                        root.title("Greek Maincourse")
                              

                        t = Table(root)
                        root.mainloop()
                        

                        f.close()
                        bev=input("Enter desired order code: ")
                        qty=int(input("Enter quantity: "))
                        f=open("GreekMaincourse.csv")
                        x=csv.reader(f,delimiter=",")
                        for i in x:
                            if i[0]==bev:
                                rate=int(i[3])*qty
                                bnam=i[1]
                            
                        f.close()
                        d={}
                        d[bnam]=rate
                        order.update(d)
                        ch=input("Press y to order more Greek maincourse or any other key to exit: ")
                        if ch!='y':
                            break
                elif corse==3:
                    while True:
                        import csv
                        f=open("GreekDessert.csv")
                        x=csv.reader(f,delimiter=",")
                        f=open("GreekDessert.csv")
                        x=csv.reader(f,delimiter=",")
                        f=open("GreekDesserts.txt", "r")
                        lst=[]
                        for i in range(5):
                            s=f.readline()
                            ns=s.replace("\n", "")
                            t=ns.split(",")
                            lst.append(t)
                        class Table:
                              def __init__(self,root):
                                  for i in range(5):
                                    for j in range(3):
                                          self.e = tkinter.Entry(root, width=35, font=('Freestyle Script',20,'bold'), justify = tkinter.CENTER, bg = "cadetblue1")
                                          self.e.grid(row=i, column=j)
                                          self.e.insert(tkinter.END, lst[i][j])

                        root = tkinter.Tk()
                        root.title("Greek Desserts")
                              

                        t = Table(root)
                        root.mainloop()
                        

                        f.close()
                        bev=input("Enter desired order code: ")
                        qty=int(input("Enter quantity: "))
                        f=open("GreekDessert.csv")
                        x=csv.reader(f,delimiter=",")
                        for i in x:
                            if i[0]==bev:
                                rate=int(i[3])*qty
                                bnam=i[1]
                            
                        f.close()
                        d={}
                        d[bnam]=rate
                        order.update(d)
                        ch=input("Press y to order more Greek deserts or any other key to exit: ")
                        if ch!='y':
                            break
                else:
                    print("Inavlid Input")
            elif cuisine==2:
                print()
                print("1.Starters\n2.Main Course\n3.Dessert")
                corse=int(input("Choose what you want to eat: "))
                if corse==1:
                    while True:
                        import csv
                        f=open("FrenchStarters.csv")
                        x=csv.reader(f,delimiter=",")
                        f=open("FrenchStarters.txt", "r")
                        lst=[]
                        for i in range(5):
                            s=f.readline()
                            ns=s.replace("\n", "")
                            t=ns.split(",")
                            lst.append(t)
                        class Table:
                              def __init__(self,root):
                                  for i in range(5):
                                    for j in range(3):
                                          self.e = tkinter.Entry(root, width=35, font=('Freestyle Script',20,'bold'), justify = tkinter.CENTER, bg = "light coral")
                                          self.e.grid(row=i, column=j)
                                          self.e.insert(tkinter.END, lst[i][j])

                        root = tkinter.Tk()
                        root.title("French Starters")
                              

                        t = Table(root)
                        root.mainloop()
                        

                        f.close()
                        bev=input("Enter desired order code: ")
                        qty=int(input("Enter quantity: "))
                        f=open("FrenchStarters.csv")
                        x=csv.reader(f,delimiter=",")
                        for i in x:
                            if i[0]==bev:
                                rate=int(i[3])*qty
                                bnam=i[1]
                            
                        f.close()
                        d={}
                        d[bnam]=rate
                        order.update(d)
                        ch=input("Press y to order more French starters or any other key to exit: ")
                        if ch!='y':
                            break
                elif corse==2:
                    while True:
                        import csv
                        f=open("FrenchMaincourse.csv")
                        x=csv.reader(f,delimiter=",")
                        f=open("FrenchMaincourse.txt", "r")
                        lst=[]
                        for i in range(5):
                            s=f.readline()
                            ns=s.replace("\n", "")
                            t=ns.split(",")
                            lst.append(t)
                        class Table:
                              def __init__(self,root):
                                  for i in range(5):
                                    for j in range(3):
                                          self.e = tkinter.Entry(root, width=35, font=('Freestyle Script',20,'bold'), justify = tkinter.CENTER, bg = "light coral")
                                          self.e.grid(row=i, column=j)
                                          self.e.insert(tkinter.END, lst[i][j])

                        root = tkinter.Tk()
                        root.title("French Maincourse")
                              

                        t = Table(root)
                        root.mainloop()
                        f.close()
                        bev=input("Enter desired order code: ")
                        qty=int(input("Enter quantity: "))
                        f=open("FrenchMaincourse.csv")
                        x=csv.reader(f,delimiter=",")
                        for i in x:
                            if i[0]==bev:
                                rate=int(i[3])*qty
                                bnam=i[1]
                            
                        f.close()
                        d={}
                        d[bnam]=rate
                        order.update(d)
                        ch=input("Press y to order more of French main course or any other key to exit: ")
                        if ch!='y':
                            break
                elif corse==3:
                    while True:
                        import csv
                        f=open("FrenchDessert.csv")
                        x=csv.reader(f,delimiter=",")
                        f=open("FrenchDesserts.txt", "r")
                        lst=[]
                        for i in range(5):
                            s=f.readline()
                            ns=s.replace("\n", "")
                            t=ns.split(",")
                            lst.append(t)
                        class Table:
                              def __init__(self,root):
                                  for i in range(5):
                                    for j in range(3):
                                          self.e = tkinter.Entry(root, width=35, font=('Freestyle Script',20,'bold'), justify = tkinter.CENTER, bg = "light coral")
                                          self.e.grid(row=i, column=j)
                                          self.e.insert(tkinter.END, lst[i][j])

                        root = tkinter.Tk()
                        root.title("French Desserts")
                              

                        t = Table(root)
                        root.mainloop()
                        f.close()
                        bev=input("Enter desired order code: ")
                        qty=int(input("Enter quantity: "))
                        f=open("FrenchDessert.csv")
                        x=csv.reader(f,delimiter=",")
                        for i in x:
                            if i[0]==bev:
                                rate=int(i[3])*qty
                                bnam=i[1]
                            
                        f.close()
                        d={}
                        d[bnam]=rate
                        order.update(d)
                        ch=input("Press y to order more French deserts or any other key to exit: ")
                        if ch!='y':
                            break
                else:
                    print("Inavlid Input")
            elif cuisine==3:
                print()
                print("1.Starters\n2.Main Course\n3.Dessert")
                corse=int(input("Choose what you want to eat: "))
                if corse==1:
                    while True:
                        import csv
                        f=open("ItalianStarters.csv")
                        x=csv.reader(f,delimiter=",")
                        f=open("ItalianStarters.txt", "r")
                        lst=[]
                        for i in range(5):
                            s=f.readline()
                            ns=s.replace("\n", "")
                            t=ns.split(",")
                            lst.append(t)
                        class Table:
                              def __init__(self,root):
                                  for i in range(5):
                                    for j in range(3):
                                          self.e = tkinter.Entry(root, width=35, font=('Freestyle Script',20,'bold'), justify = tkinter.CENTER, bg = "khaki1")
                                          self.e.grid(row=i, column=j)
                                          self.e.insert(tkinter.END, lst[i][j])

                        root = tkinter.Tk()
                        root.title("Italian Starters")
                              

                        t = Table(root)
                        root.mainloop()
                        f.close()
                        bev=input("Enter desired order code: ")
                        qty=int(input("Enter quantity: "))
                        f=open("ItalianStarters.csv")
                        x=csv.reader(f,delimiter=",")
                        for i in x:
                            if i[0]==bev:
                                rate=int(i[3])*qty
                                bnam=i[1]
                            
                        f.close()
                        d={}
                        d[bnam]=rate
                        order.update(d)
                        ch=input("Press y to order more Italian starters or any other key to exit: ")
                        if ch!='y':
                            break
                elif corse==2:
                    while True:
                        import csv
                        f=open("ItalianMaincourse.csv")
                        f=open("ItalianMaincourse.txt", "r")
                        lst=[]
                        for i in range(5):
                            s=f.readline()
                            ns=s.replace("\n", "")
                            t=ns.split(",")
                            lst.append(t)
                        class Table:
                              def __init__(self,root):
                                  for i in range(5):
                                    for j in range(3):
                                          self.e = tkinter.Entry(root, width=35, font=('Freestyle Script',20,'bold'), justify = tkinter.CENTER, bg = "khaki1")
                                          self.e.grid(row=i, column=j)
                                          self.e.insert(tkinter.END, lst[i][j])

                        root = tkinter.Tk()
                        root.title("Italian Maincourse")
                              

                        t = Table(root)
                        root.mainloop()
                        f.close()
                        bev=input("Enter desired order code: ")
                        qty=int(input("Enter quantity: "))
                        f=open("ItalianDessert.csv")
                        x=csv.reader(f,delimiter=",")
                        for i in x:
                            if i[0]==bev:
                                rate=int(i[3])*qty
                                bnam=i[1]
                            
                        f.close()
                        d={}
                        d[bnam]=rate
                        order.update(d)
                        ch=input("Press y to order more of Italin main course or any other key to exit: ")
                        if ch!='y':
                            break
                elif corse==3:
                    while True:
                        import csv
                        f=open("ItalianDessert.csv")
                        f=open("ItalianDesserts.txt", "r")
                        lst=[]
                        for i in range(5):
                            s=f.readline()
                            ns=s.replace("\n", "")
                            t=ns.split(",")
                            lst.append(t)
                        class Table:
                              def __init__(self,root):
                                  for i in range(5):
                                    for j in range(3):
                                          self.e = tkinter.Entry(root, width=35, font=('Freestyle Script',20,'bold'), justify = tkinter.CENTER, bg = "khaki1")
                                          self.e.grid(row=i, column=j)
                                          self.e.insert(tkinter.END, lst[i][j])

                        root = tkinter.Tk()
                        root.title("Italian Desserts")
                              

                        t = Table(root)
                        root.mainloop()
                        f.close()
                        bev=input("Enter desired order code: ")
                        qty=int(input("Enter quantity: "))
                        f=open("ItalianDessert.csv")
                        x=csv.reader(f,delimiter=",")
                        for i in x:
                            if i[0]==bev:
                                rate=int(i[3])*qty
                                bnam=i[1]
                            
                        f.close()
                        d={}
                        d[bnam]=rate
                        order.update(d)
                        ch=input("Press y to order more Italian deserts or any other key to exit: ")
                        if ch!='y':
                            break
                else:
                    print("Inavlid Input")
            cont=input("Press Y to order more foods or any other key to exit: ")
            if cont!='Y':
                print("Yay! Order received",order)
                print()
                print("                        BILL            ")
                print("=" * 65)
                print("%10s"%"S.NO.","%30s"%"NAME","%20s"%"PRICE")
                print("=" * 65)

                sno=1

                for i,j in order.items():
                    print("%10s"%sno,"%30s"%i,"%20s"%j)
                    sno=sno+1
                print("=" * 65)
                totalp=0
                for i in order.values():
                    totalp=totalp+int(i)
                print(" "*55,"Total",totalp)
                print()
                bill()
                break
def bevy():
    import csv
    import tkinter
    f=open("Beverages.csv")
    x=csv.reader(f,delimiter=",")
    f=open("Beverages.txt", "r")
    lst=[]
    for i in range(5):
        s=f.readline()
        ns=s.replace("\n", "")
        t=ns.split(",")
        lst.append(t)
    class Table:
          def __init__(self,root):
              for i in range(5):
                for j in range(3):
                      self.e = tkinter.Entry(root, width=35, font=('Freestyle Script',20,'bold'), justify = tkinter.CENTER, bg = "olivedrab1")
                      self.e.grid(row=i, column=j)
                      self.e.insert(tkinter.END, lst[i][j])

    root = tkinter.Tk()
    root.title("Beverages")
    t = Table(root)
    
    root.mainloop()
    f.close()
    print()
    while True:
        bev=input("Enter desired order code: ")
        qty=int(input("Enter quantity: "))
        import csv
        f=open("Beverages.csv")
        x=csv.reader(f,delimiter=",")
        for i in x:
            if i[0]==bev:
                rate=int(i[3])*qty
                bnam=i[1]
        f.close()
        d={}
        d[bnam]=rate
        order.update(d)
        ch=input("Press y to order more beverages or any other key to exit: ")
        if ch!='y':
            break
    print("Your orders are:\n",order)
    ch=input("Press k to add foods or any other key to exit: ")
    if ch=='k':
        food()
    else:
        print("Yay! Order received",order)
        print()
        print("                        BILL            ")
        print("=" * 65)
        print("%10s"%"S.NO.","%30s"%"NAME","%20s"%"PRICE")
        print("=" * 65)

        sno=1

        for i,j in order.items():
            print("%10s"%sno,"%30s"%i,"%20s"%j)
            sno=sno+1
        print("=" * 65)
        totalp=0
        for i in order.values():
            totalp=totalp+int(i)
        print(" "*55,"Total",totalp)
        print()
        bill()
def f_f():
    print("Please select what you want to proceed with\n\n1.Beverages\n2.Food\n")
    choose=int(input("Enter you choice: "))
    print()
    order={}
    if choose==1:
        bevy()
    elif choose==2:
        food()
    else:
        print("Invalid Input")
