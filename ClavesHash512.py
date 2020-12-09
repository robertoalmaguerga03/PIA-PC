try:
    import hashlib, os, argparse
except ImportError:
    print('Error de importación')
    os.system('pip3 install -r requirements.txt')
    print("Saliendo, vuelve a ejecutar el programa")
    exit()
        
#parser = argparse.ArgumentParser()
#parser.add_argument("-ruta", dest="path", help="La ruta en la que se encuentra el archivo")
#params = parser.parse_args()
#print(params.path)

def claves(path):
    #if params.path != None:
        #path = input ("Escriba el nombre del archivo")
    #else:
        #print("no escribió nada")
            
    file_obj = open (path,"rb")
    file = file_obj.read()

    Hash = hashlib.sha512(file)
    Hashed = Hash.hexdigest()
    print ("El valor HASH del archivo ingresado es: ", Hashed)
