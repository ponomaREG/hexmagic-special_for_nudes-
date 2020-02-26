import sys
import os



STATIC_FILE_NAME = "PLEASE!!!WAIT.jpg"


def rename(new_name,old_name=STATIC_FILE_NAME):
    os.remove(new_name)
    os.rename(old_name,new_name)


def make(filename,what_we_gona_do):
    try:
        file = open(filename,"rb")
        file_2 = open(STATIC_FILE_NAME,"wb")
        count=0
        for line in file.readlines():
            for byte in line:
                count+=1
                if(count==2):
                    if(what_we_gona_do):
                        byte-=1
                    else:
                        byte+=1
                byte_2 = byte.to_bytes(1,byteorder='big')
                file_2.write(byte_2)
        rename(filename)
        file.close()
        file_2.close()
    except FileNotFoundError:
        print("Ошибка!")


args = sys.argv
if(len(args[1:])<1):
    print("Нет аргументов. Пиши help")
else:
    if(args[1]=="help"):
        print("python3 Hexmagic.py [--broke/--fix] filename")
    elif(len(args[1:])==1):
        print("Видимо, ты забыл название файла")
    else:
        key = args[1]
        namefile = args[2]
        if(key == "--broke"):
            make(namefile,True)

        elif(key=="--fix"):
            make(namefile,False)
        else:
            print("Неверный ключ")






