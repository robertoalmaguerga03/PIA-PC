import argparse




def encriptar(msj, clv):
    try:
        message = msj
        espacios = 1
        while espacios > 0:
            clave = clv
            espacios = clave.count(' ')
            if clave.isalpha() == False:
                espacios += 1
        key = len(clave)

        SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
        translated = ''
        for symbol in message:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex + key
                
                if translatedIndex >= len(SYMBOLS):
                    translatedIndex = translatedIndex - len(SYMBOLS)
                elif translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)

                translated = translated + SYMBOLS[translatedIndex]
            else:
                # Append the symbol without encrypting/decrypting:
                translated = translated + symbol
          
        print(translated)
    except Exception as e:
        print("Ha ocurrido una falla" + str(e))
        


def desencriptar(msj, clv):
    try:
        message = msj
        espacios = 1
        while espacios > 0:
            clave = clv
            espacios = clave.count(' ')
            if clave.isalpha() == False:
                espacios += 1
        key = len(clave)

        SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

        translated = ''

        for symbol in message:
        # Note: Only symbols in the `SYMBOLS` string can be encrypted/decrypted.
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex - key
            
                if translatedIndex >= len(SYMBOLS):
                    translatedIndex = translatedIndex - len(SYMBOLS)
                elif translatedIndex < 0:
                    translatedIndex = translatedIndex + len(SYMBOLS)

                translated = translated + SYMBOLS[translatedIndex]
            else:
            # Append the symbol without encrypting/decrypting:
                translated = translated + symbol

        print(translated)
    except Exception as e:
        print("Ha ocurrido una falla" + str(e))



#if modo == 'e':
    #encriptar(msj, clv)
#elif modo1 == 'd':
    #desencriptar(msj, clv)

    
    
    
    
    

        


    
