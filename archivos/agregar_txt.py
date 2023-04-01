with open('archivos\\texto_cristobal.txt','a', encoding = 'UTF-8') as archivo: # 'a' da permiso de escritura agregando
    # Usando un bucle para agregar varias lineas
    archivo.write('\n')
    for i in range(5):
        archivo.write(f'linea {i+1} agregada\n')