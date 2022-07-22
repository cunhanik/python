import os, sqlite3, time, winsound

class Manager:
    def __init__(self):
        self.name = ""
        self.phone = ""
        self.adress = ""


    def add(self):
        os.system("cls")
        running = True
        while running:
            os.system("cls")
            print("------------------ Creating a Contact -----------------------")
            print()
            time.sleep(0.3)
            self.name = input("What is your Name: ")
            time.sleep(0.3)
            self.phone = input("What is your Phone: ")
            time.sleep(0.3)
            self.adress = input("What is your Adress: ")
            db = sqlite3.connect("bot1")
            cursor = db.cursor()
            cursor.execute(""" INSERT INTO IMPORTS\
                            (name, phone, adress)VALUES(?,?,?)""",\
                                (self.name, self.phone, self.adress))
            os.system("cls")
            print("CREATING AND SAVING THE CONTACT")
            time.sleep(0.3)
            print(".")
            time.sleep(0.3)
            print(".")
            time.sleep(0.3)
            print(".")
            time.sleep(0.3)
            print(".")
            time.sleep(0.3)
            print(".")
            os.system("cls")
            time.sleep(0.2)
            print("SUCCESSFULLY CREATED")
            time.sleep(1)
            print("SAVED")
            db.commit()
            time.sleep(2)
            os.system("cls")
            another = input("                        You Want Add another contact?     [YES/NO] :  ")
            if another == "YES":
                continue
            elif another == "y":
                continue
            elif another == "Y":
                continue
            elif another == "yes":
                continue
            else:
                running = False
                db.close()
                time.sleep(1)
                print("----BACK TO MENU----")
                time.sleep(1)
                os.system("cls")
                self.menu()

    def update(self):
        pass

    def remove(self):
        pass
    
    def get_list(self):
        pass

    def finish(self):
        pass

    def menu(self):
        os.system("cls")
        winsound.Beep(2500,300)
        time.sleep(1)
        print("-----MENU-----")
        time.sleep(0.3)
        print("1 :) Add")
        time.sleep(0.3)
        print("2 :) Update")
        time.sleep(0.3)
        print("3 :) Remove")
        time.sleep(0.3)
        print("4 :) List")
        time.sleep(0.3)
        print("5 :) Finish")
        time.sleep(1)
        opcao = input("                         Which option do you want to use :  ")
        if opcao == "1":
            self.add()
        elif opcao == "2":
            self.update()
        elif opcao == "3":
            self.remove()
        elif opcao == "4":
            self.get_list()
        elif opcao == "5":
            self.finish()
        else:
            os.system("cls")
            winsound.Beep(1000,300)
            time.sleep(0.3)
            print("Invalid option.")
            time.sleep(0.5)
            os.system("cls")
            time.sleep(0.5)
            print("please, try again: ")
            time.sleep(1)
            self.menu()

    def main(self):
        os.system("cls")
        if os.path.isfile("bot1"):
            db = sqlite3.connect("bot1")
            time.sleep(0.5)
            print("SUCCESSFULLY CONNECTED")
            time.sleep(1)
            self.menu()
        else:
            os.system("cls")
            time.sleep(2)
            print("ERROR, YOU ARE NOT AUTHORIZED TO ENTER THE DATABASE")
            winsound.Beep(1000,500)
            time.sleep(2)
            os.system("cls")
            time.sleep(1)
            print("CREATING A NEW CONNECTION FILE")
            time.sleep(0.2)
            print(".")
            time.sleep(0.2)
            print(".")
            time.sleep(0.2)
            print(".")
            time.sleep(0.2)
            print(".")
            time.sleep(0.2)
            print(".")
            time.sleep(0.2)
            os.system("cls")
            time.sleep(0.2)
            print("SUCCESSFULLY CREATED")
            time.sleep(1)
            db = sqlite3.connect("bot1")
            cursor = db.cursor()
            cursor.execute("""CREATE TABLE IMPORTS
                            (name TEXT, phone TEXT, adress TEXT)""")
            self.menu()
        


contacts_manager = Manager()
contacts_manager.main()