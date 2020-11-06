print("----------")
print("Welcome to Deb Store!")
x = input("")
print("You can purchase anything here!")
print("1: Browse 2: Create 3: Purchase 4: Exit")
x = input("@User: ")
if x == "1":
    f = open("deb.shdes.config", "r")
    custom = f.read()
    print("Searching...")
    print("Web Tasric Game! FUN! very. #001")
    print("mat for sale #345")
    print("mad man real life toy, 7 ft! #987")
    print("secure your Device! App 2.8 #456")
    print("Privete diray bookSECRET #676")
    print(custom)
    jik = input("")
    import deb
if x == "2":
    print("Login Using WebDiFine Account:")
    print("Web Name: ")
    k = input("@User: ")
    f = open("name.config", "r")
    name = f.read()
    if k == name:
        print("ID Password: ")
        v = input("@User: ")
        f = open("id.config", "r")
        idx = f.read()
        if v == idx:
            logged = "1"
            print("----------")
            print("Creators Lab:")
            print("Enter short description:")
            des = input("@User: ")
            file = open('deb.shdes.config', 'w')
            file.write(des + " #789")
            file.close()
            print("Enter long details:")
            det = input("@User: ")
            file = open('deb.lodet.config', 'w')
            file.write(det)
            file.close()
            import deb
if x == "4":
    import WEBDIFINE
if x == "3":
    print("Enter Product NumberID:")
    num = input("@User: ")
    if num == "789":
        f = open("deb.lodet.config", "r")
        lodet = f.read()
        print(lodet)
        
    
    
    
    
    
