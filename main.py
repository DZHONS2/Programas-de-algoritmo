#crear , actualizar, buscar, eliminar, salir 

#nombre, edad telefono
database=[]
def create():
    iden=len(database)+1 
    nombre=input("nombre: ")
    edad= int(input("edad: "))
    tel = input("telefono: ")
    
    persona={
        "id":iden, 
        "nombre":nombre,
        "edad":edad,
        "tel":tel
    }
    
    database.append(persona)
    
def read():
    if len(database)==0:
        print("sin contactos ")
    else:
        print("---------------------------")
        for persona in database: 
            print(f"ID: {persona["id"]} nombre: {persona["nombre"]} edad: {persona["edad"]} tel: {persona["tel"]}")
        print("---------------------------")
        
def find():
    if len(database)==0:
        print("no hay registros para buscar")
    else:
        idbus=int(input("digite el ID para buscar: "))
        enc=0
        for persona in database: 
            if persona["id"]==idbus:
                enc=1
                
                print("-----------------------")
                print(f"ID: {persona["id"]} nombre: {persona["nombre"]} edad: {persona["edad"]} tel: {persona["tel"]}")
                print("-----------------------")
        if enc == 0:
            print("no hay suficionetes usuarios")
            
#ttt#
def update():
    if len(database)==0:
        print("base de datos vacia")
    else: 
        read()
        idmod= int(input("ID a modificar: "))
        nombre= input("nombre modificado: ")
        edad= input("edad modificado: ")        
        tel= input("telefono modificado: ")
        
        personaMod={
        "id":idmod, 
        "nombre":nombre,
        "edad":edad,
        "tel":tel
        }
        for i,persona in enumerate(database):
            if persona["id"]==idmod:
                database[i]=personaMod
                
def delete():
    if len(database)==0:
        print("no hay registros")
    else: 
        read()
        idDel=int(input("Ingrese el ID a Elininar"))
        
        for i, persona in enumerate(database):
            if persona["id"]==idDel: 
                database.pop(i)
                
                persona
        

def menu(): 
    while True:  
    
    
        print("Lista de contacto")
        print(" 1. crear contacto")
        print(" 2. ver contactor")
        print(" 3. buscar contacto")
        print(" 4. actualizar contacto")
        print(" 5. eliminar contacto")
        print(" 6. salir ")
        
        op=input("ingrese una Opcion: ")
        if op=="1":
            create()
        elif op=="2":
            read()
        elif op=="3":
            find()
        elif op=="4":
            update()
        elif op=="5":
            delete()
        elif op=="6":
            print("saliendo... ")
            break
        
menu()

        
        q