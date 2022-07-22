import sqlite3,os,time,winsound

                                    #TUDO COMPLETO

class Manager:
    def __init__(self):
        self.name = ""
        self.phone = ""
        self.adress = ""

    def add(self):
        running = True
        while running:
            os.system("cls")
            print("--------ADD CONTACT-------")
            print()
            time.sleep(0.2)
            self.name = input("name: ")
            time.sleep(0.2)
            self.phone = input("Phone: ")
            time.sleep(0.2)
            self.adress = input("Adress: ")
            db = sqlite3.connect("connection")
            cursor = db.cursor()
            cursor.execute(""" INSERT INTO contacts\
                            (Name, Phone, Adress)VALUES(?,?,?)""",\
                                (self.name, self.phone, self.adress))
            db.commit()
            outro_contacto = input("Deseja adicionar outro contacto? [Y/N] : ")
            if outro_contacto == "y":
                continue
            elif outro_contacto == "Y":
                continue
            else:
                db.close()
                running = False
                print("------A VOLTAR PARA O MENU------")
                time.sleep(2)
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
        winsound.Beep(2000,50)
        print("-----------MENU-----------")
        time.sleep(0.05)
        print()
        print("1 :) Add")
        time.sleep(0.05)
        
        print("2 :) remove")
        time.sleep(0.05)
        
        print("3 :) Update")
        time.sleep(0.05)
        
        print("4 :) List")
        time.sleep(0.05)

        print("5 :) Terminate")
        print()
        
        opcao = input("Selecione uma opção: ")
        if opcao == "1":
            self.add()
        elif opcao == "2":
            self.remove()
        elif opcao == "3":
            self.update()
        elif opcao == "4":
            self.get_list()
        elif opcao == "5":
            self.finish()
        else:
            winsound.Beep(2500,100)
            print("ERROR, TENTA NOVAMENTE.")
            time.sleep(2)
            self.menu()
            
    def main(self):
        os.system("cls")
        if os.path.isfile("connection"):
            db = sqlite3.connect("connection")
            time.sleep(1)
            winsound.Beep(2000,50)
            print()
            print("CONECTADO AO BANCO DE DADOS")
            time.sleep(1)
            self.menu()            
        else:
            print("ESTA CONEXAO NAO EXISTE")
            print()
            time.sleep(1)
            winsound.Beep(2000,50)       
            print("Creating new conection file")
            time.sleep(1)
            db = sqlite3.connect("connection")
            cursor = db.cursor()
            cursor.execute("""CREATE TABLE contacts
                            (Name TEXT, Phone TEXT, Adress TEXT)""")
            winsound.Beep(2000,50)
            print()
            print("conexao criada com sucesso.")
            print("conectado com sucesso.")
            time.sleep(3)
            self.menu()





contacts_manager = Manager()
contacts_manager.main()