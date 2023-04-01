with open('archivos\\texto_cristobal.txt','w', encoding = 'UTF-8') as archivo: # 'w' da permiso de escritura
    # Sobre escribe el archivo
    #archivo.write('Holaa xdd nose que poner')
    archivo.writelines(['alpaca random para ver que tal\n','almuadilla w'])