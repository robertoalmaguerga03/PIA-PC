import argparse
import Mensajes
import ExtraerMetadatos
import ClavesHash512
import EnvioCorreo
import Puertos
import Shodan
import socket


parser = argparse.ArgumentParser()
parser.add_argument("-u", dest="usuario", help="El usuario para entrar")
parser.add_argument("-con", dest="contra", help="La contraseña del usuario")
parser.add_argument("-opc1", metavar="Opc1", dest="opc1",
                    help="Esto es para ejecutar solo la opcion 1")
parser.add_argument("-opc2", metavar="Opc2", dest="opc2",
                    help="Esto es para ejecutar solo la opcion 2")
parser.add_argument("-opc3", metavar="Opc3", dest="opc3",
                    help="Esto es para ejecutar solo la opcion 3")
parser.add_argument("-opc4", metavar="Opc4", dest="opc4",
                    help="Esto es para ejecutar solo la opcion 4")
parser.add_argument("-opc5", metavar="Opc5", dest="opc5",
                    help="Esto es para ejecutar solo la opcion 5")
parser.add_argument("-opc6", metavar="Opc6", dest="opc6",
                    help="Esto es para ejecutar solo la opcion 6")
parser.add_argument("-opc7", metavar="Opc7", dest="opc7",
                    help="Esto es para ejecutar solo la opcion 7")
parser.add_argument("-modo", metavar="e", dest="e",
                    help="opcion para encriptar tu frase")
parser.add_argument("-modo1", metavar="d", dest="d",
                    help="opcion para desencriptar tu frase")
parser.add_argument("-msj", metavar="msj", dest="msj",
                    help="mensaje a encriptar")
parser.add_argument("-clv", metavar="clv", dest="clv",
                    help="clv")
parser.add_argument("-ruta", metavar="ruta", dest="ruta",
                    help="opcion para introducir tu ruta")
parser.add_argument("-path", dest="path",
                    help="La ruta en la que se encuentra el archivo")
parser.add_argument("-a", dest="asunto", help="El asunto del correo")
parser.add_argument("-c", dest="cuerpo", help="El cuerpo del correo")
parser.add_argument("-r", dest="remi", help="El remitente del correo")
parser.add_argument("-d", dest="dest", help="El destinatario del correo")
parser.add_argument("-p", dest="psw", help="La contraseña del correo a utilizar")
parser.add_argument("-i", dest="img", help="El nombre del archivo que se mandará")
parser.add_argument("-ip", dest="ip", help="Dirección IP a escanear")
parser.add_argument("-api", dest="api", help="Ingresar tu apikey")
parser.add_argument("-link", dest="link", help="Ingresar un link")


params = parser.parse_args()
usuario = str(params.usuario)
contra = str(params.contra)
path = str(params.path)
ruta = str(params.ruta)
modo1 = str(params.d)
modo = str(params.e)
msj = str(params.msj)
clv = str(params.clv)
opc1 = str(params.opc1)
opc2 = str(params.opc2)
opc3 = str(params.opc3)
opc4 = str(params.opc4)
opc5 = str(params.opc5)
opc6 = str(params.opc6)
opc7 = str(params.opc7)
remi = str(params.remi)
dest = str(params.dest)
asunto = str(params.asunto)
dest = str(params.dest)
filename = str(params.img)
msg = str(params.cuerpo)
psw = str(params.psw)
ip = str(params.ip)
api = str(params.api)
link = str(params.link)
                    


print("\tINICIO DE SESIÓN")

uscorrecto = "nombre"
concorrecta = "12345"

cont = 1
if (cont == 1):
    if (usuario == uscorrecto):
        if (contra == concorrecta):
            print("Inicio de sesión satisfactorio, bienvenido " + usuario+'\n')
            cont=2
        else:
            print("Contraseña incorrecta!\n")
    else:
        print("Usuario incorrecto!\n")

if __name__=="__main__":
    if cont==2:
        if opc1 == 'opc1':
            if modo == 'e':
                print("Encriptando mensaje...\n")
                Mensajes.encriptar(msj, clv)
            elif modo1 == 'd':
                print("Desencriptando mensaje...\n")
                Mensajes.desencriptar(msj, clv)
        elif opc2 == 'opc2':
            print("Extrayendo Metadatos de imagenes...\n")
            ExtraerMetadatos.printMeta(ruta)
        elif opc3 == 'opc3':
            print("Obteniendo Hash...\n")
            ClavesHash512.claves(path)
        elif opc4 == 'opc4':
            print("Enviando correo...")
            EnvioCorreo.Envio(remi, dest, asunto, filename, msg, psw)
        elif opc5 == 'opc5':
            print("Escaneando purtos...")
            Puertos.puertos(ip)
        elif opc6 == 'opc6':
            print("Buscando servidores con API...")
            Shodan.api(api)
        elif opc7 == 'opc7':
            print("Obteniendo datos del link...")
            print(socket.gethostbyname_ex(link))
    else:
        print("Usuario y/o contraseña incorrectos")

        
        
        
