#Programa de inventarios
import os
#Funciones

def limpia():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def guarda_matriz(matriz,nombre):
    with open(nombre,'w', encoding='utf-8') as archivo:
        for renglon in matriz:
             cadena=','.join(renglon)
             archivo.write(cadena+'\n')
             
def leer_archivo(nombre):
    matriz=[]
    with open (nombre, 'r', encoding = 'utf-8') as archivo:
        for linea in archivo:
            sin_enter = linea.rstrip()
            lista = sin_enter.split(',')
            matriz.append(lista)
        return matriz
    
def imprimir_lista(lista):
    for elemento in lista:
        print(elemento, end="       ")   

def imprimir_lista2(lista):
    for elemento in lista:
        print(f'{elemento:>10}', end="       ")  
        
def imprimir_matriz(matriz):
    for lista in matriz:
        for elemento in lista:
            print(f'{elemento:>20}', end="  ")
        print('\n')

def registrar_ventas(cant):
     # Guardamos el inventario en una variable, enviandolo a una funcion que lo abre y nos lo devuelve como una matriz.
    inventario=leer_archivo('inventario')
    #Pide id del vendedor
    id_vendedor=input('Ingrese el ID del vendedor ------> \n')
    #Inicializamos el acumulador para sumar en 0
    suma = 0
    #Condicional para comprobar si el id ingresado existe o es correcto
    if id_vendedor in ['1V','2V','3V']:
        #Si es correcto, guardamos en la variable ventas, la funcion que abre el archivo del vendedor correspondiente a el ID,y nos lo devuelve como una matriz.
        ventas=leer_archivo(f'{id_vendedor}_ventas')
        #For para la cantidad de productos que se indico para registrar
        for i in range(cant):
            #Se pide el ID de cada producto ingresado para comprobar su existencia y la cantidad vendida de ese producto
            id_producto=input(f'Ingrese el ID del producto {i+1} --->')
            cant_prod=input(f'Ingrese la cantidad vendida del producto {i+1} --->')
            #For para recorrer la matriz del archivo de ventas
            for z in range(0,len(ventas)):
                #Condicional para comprobar la existencia del producto en la matriz
                if id_producto in ventas[z][0]:
                    #Si existe y su cantidad es diferente a cero, suma la cantidad vendida del producto a la cantidad de ventas de ese producto del vendedor.
                    #posteriormente le resta esa cantidad a la matriz de inventarios de ese producto.
                    #y por ultimo se manda a la funcion para sobre escribir los nuevos valores a sus archivos correspondientes.
                    if int(inventario[z][3]) != 0:
                        suma = int(ventas[z][3])+int(cant_prod)
                        ventas[z][3] = str(suma)
                        inventario[z][3]=str((int(inventario[z][3])-int(cant_prod)))
                        guarda_matriz(ventas,f'{id_vendedor}_ventas')
                        guarda_matriz(inventario,'inventario') 
                        print('¡Su registro de ventas ha sido exitoso!')
                        break
                    else:
                        #Si en el inventario ya no hay productos manda este mensaje
                        print('No hay artículos suficientes para hacer esta venta')
                        suma = 1
                        break
            #Condicional que uitliza el acumulador para evaluar si el producto no existe.       
            if suma == 0:
                print('El id del producto no existe.')
        #Se envian los la matriz de ventas y el id del vendedor a la función reporte de ventas        
        reporte_ventas(ventas, f'{id_vendedor}')  
        reporte_articulos()                          
    else:
        #Si el id del vendedor es invalido.
        print('El id de vendedor es incorrecto.')

    
def registrar_llegada_articulos_almacen():
     # Guardamos el inventario en una variable, enviandolo a una funcion que lo abre y nos lo devuelve como una matriz.
    inventario=leer_archivo('inventario')
    #Pide id del vendedor
    id_vendedor=input('Ingrese el ID del que recibio------> \n')
    #Se verifica que el id exista.
    if id_vendedor in ['1R','2R','3R']:
        #Si existe el id, se pregunta que es lo que desea realizar.
        opci=input('1-Si desea agregar un articulo nuevo ingrese---->N.\n2-Si desea registrar al almacen de un producto existente ingrese---->E\n----> ')
        #Si se selecciona existente entonces entra a este condicional
        if opci == 'E' or opci=='e':
            #Se pide la cantidad de productos a almacenar
            cant_alm=int(input('Cantidad de productos:'))
            #Si la cantidad es mayor a cero entra a el condicional
            if cant_alm>0:
                #For anidado el primero para la cantidad de productos a almacenar.
                for i in range(cant_alm):
                    #Se pide el id del producto y la cantidad de ese producto que llego
                    id_producto=input(f'Ingrese el ID del producto {i+1}--->')          
                    cant_prod=input(f'Ingrese el la cantidad que llego del producto {i+1}-->')
                    #for para agregar a el inventario los productos y cantidades ingresadas
                    for z in range(len(inventario)):
                        #Condicional para comprobar que el id del producto existe, posteriormente lo suma a el inventario y lo guarda en el archivo de inventario con la función.
                        if id_producto in inventario[z][0]:
                            inventario[z][3]=str((int(inventario[z][3])+int(cant_prod)))
                            guarda_matriz(inventario,'inventario') 
                            print('¡Su registro en el almacen ha sido exitoso!')
                            break;
                        else:
                            break;
                        #Si el id no exise manda este mensaje
                    if id_producto not in inventario[z][0]:
                        print('El producto no existe')
            else:
                #Si la cantidad ingresada es menor a 0
                print('Error:La cantidad debe ser mayor a cero')
                #Condicional para cuando seleccione el nuevo producto
        elif opci == 'N' or 'n':
            #Inicializo lista vacia
            nuevo_art=[]
            #Se pide la cantidad de articulos que desea ingresar
            cant_art=int(input('Cantidad de articulos que desea ingresar: \n'))
            #Si la cantidad de articulos ingresada es mayor a 0 entra a el for
            if cant_art>0:
                #For para agregar cada articul.
                for i in range(cant_art):
                    #id automatico y se guarda en la lista nuevo_art
                    id_n=str(len(inventario)+1)
                    nuevo_art.append(id_n)
                    #Se pide el nombre y se guarda en la lista nuevo_art
                    nombre=input('Ingrese el NOMBRE del articulo nuevo: \n')
                    nuevo_art.append(nombre)
                    #Se pide el modelo y se guarda en la lista nuevo_art
                    modelo=input('Ingrese el MODELO del articulo nuevo: \n')
                    nuevo_art.append(modelo)
                    #Se pide la cantidad y se guarda en la lista nuevo_art
                    cant=input('Ingrese la CANTIDAD del articulo nuevo: \n')
                    nuevo_art.append(cant)
                    #Se pide el precio unitario y se guarda en la lista nuevo_art
                    precio_u=input('Ingrese el PRECIO UNITARIO del articulo nuevo: \n')
                    nuevo_art.append(precio_u)
                    #Se agrega a la matrriz del inventario la lista con el articulo nuevo y sus caracteristicas.
                    inventario.append(nuevo_art)
                    #Se guarda el inventario actualizado
                    guarda_matriz(inventario,'inventario') 
                    print('¡Su registro en el almacen ha sido exitoso!')                       
            else:
                print('Error:La cantidad debe ser mayor a cero')
                #Manejo de error cuando la cantidad es menor a cero         
        else:
            print('Error: La opcion que selecciono no existe')
             #Manejo de error cuando opcion no existe 
    else:
        print('El id de recepcion es incorrecto.')
         #Manejo de error cuando el id del recepcionista es incorrecto 
    
    
    
def consultar_datos_inventario():
    # Guardamos el inventario en una variable, enviandolo a una funcion que lo abre y nos lo devuelve como una matriz.
    inventario=leer_archivo('inventario')
    #Solicitamos la opcion que desea
    opc=input('Si desea buscar por articulo ingrese A o si desea ver el inventario completo ingrese I: \n')
    #Condicional para cuando se desea buscar por articulo
    if opc=='A':
        #Se crea una lista vacia
        art=[]
        #Se comienza en 1 para el while
        salir=1
        #Se pide el id del articulo o el nombre del articulo que desea buscar
        articulo=input('Ingrese el id del articulo o el nombre: \n')
        #for anidado para buscar en el inventario el articulo por id o nombre, si no se encuentra en articulo a la variable salir le asigna 0 y no entra a el while, s    
        #pero si el id o el nombre es correcto a salir se le asigna 1 para que entre a el while y realice la busqueda con los for anidados.
        for z in range(len(inventario)):
            if articulo in inventario[z][0] or articulo in inventario[z][1]:
                salir=1
                break;
            else:
                salir=0
                    
                        
        if salir==0:
            print('El id o el nombre son incorrectos')
        #Para realizar busqueda de los articulos por id o nombre
        while salir!=0:
            for i in range(len(inventario)):
                for z in range(len(inventario[i])):
                    if articulo == inventario[i][0] or articulo == inventario[i][1]:
                        art.append(inventario[i][z])
            print('ID  ','     Nombre', '           Modelo           ', 'Cantidad  ', 'Precio unitario')
            #Se manda a imprimir la lista generada del articulo
            imprimir_lista(art)
            #se le asigna 0 para que no vuelva a entrar a el while
            salir=0
            
    elif opc=='I':
        #Si desea imprimir todo el inventario se manda a la funcion para imprimir matrices
        imprimir_matriz(inventario)
        
    else:
        #Manejo de error si la letra es incorrecta de las opciones ofrecidas por el programa.
        print('Error: La letra que ingresaste es incorrecta')


 #Función que devuelve el reporte de ventas del vendedor deseado. No recibe parámetros.   
def reportes_ventas_vendedor():
    cant = int(input('Ingrese la cantidad de búsquedas que desea hacer: '))
    while cant <= 0:
        print('Error: Número no válido. Por favor vuelva a ingresar')
        cant = int(input())
    # Ciclo para pedir los datos que ingresó el usuario 
    for i in range (0,cant):   
        reporte = []   
        nombre = input('Ingrese el nombre o ID del vendedor que desea ver: ')
        print('\n')
        #Se lee el archivo lista de vendedores para poder comparar sus nombres o ID
        empleados = leer_archivo('lista_vendedores')
        #Ciclo hata la longitud de empleados para hacer comparaciones
        for j in range(0,len(empleados)):     
            #Si el dato ingresado se encuentra en la lista actual columna 0, se encontró por ID. En la columna 1 encontró por nombre
            if nombre in empleados[j][0] or nombre in empleados[j][1]:
                #En cualquier caso, a archivo se le asignará el ID de la lista que tuvo coincidencia (debido al nombre de los archivos)
                archivo = str(empleados[j][0])
                #Se lee e imprime el archivo de reporte correspondiente a ese ID
                reporte = leer_archivo(f'{archivo}_reporte')       
                print('             Artículo                Cantidad              Total\n')
                imprimir_matriz(reporte)
        #En caso de que no se haya encontrado el vendedor, la lista datos se habrá quedado vacía. Por eso se hizo una condicional para comprobar si esa lista es igual a cero
        if len(reporte) <= 0:
            print('Error: No se encontró al vendedor\n')                
    input('Enter para continuar')

#Función que devuelve el reporte de ventas del artículo deseado. No recibe parámetros.   
def reportes_ventas_artículo():        
    cant = int(input('Ingrese la cantidad de búsquedas que desea hacer: '))
    while cant <= 0:
        print('Error: Número no válido. Por favor vuelva a ingresar')
        cant = int(input())
    
    for i in range (0,cant):   
        reporte = []   
        nombre = input('Ingrese el nombre o ID del artículo que desea ver: ')
        print('\n')
        archivo = leer_archivo('inventario')
        for j in range(0,len(archivo)):    
            #Si existe una coincidencia con el nombre ingresado y la lista en su elemento 0 (ID) o 1 (nombre) imprime la lista que corresponde
            if nombre == archivo[j][0] or nombre == archivo[j][1]:
                reporte = leer_archivo('articulo_reporte')       
                print('   Artículo            Cantidad        Precio           Total\n')
                lista = (reporte[j])
                imprimir_lista2(lista)
                print('\n')
                break
        #Si la longitud de la variable reporte es menor a 1, quiere decir que no se leyó el archivo. Por lo tanto, no se encontró el artículo.
        if len(reporte) < 1:
            print('Error: No se encontró el artículo\n')                
    input('Enter para continuar')


#Función que devuelve una consulta específica, buscando ventas por nombre de vendedor o artículo. No recibe parámetros.
def consultar_datos_ventas():
    cant = int(input('Ingrese la cantidad de búsquedas que desea hacer: '))
    while cant <= 0:
        print('Error: Número no válido. Por favor vuelva a ingresar')
        cant = int(input())
    
    for i in range (0,cant):   
        reporte = []
        busqueda = []   
        total_art = 0
        total_vent = 0
        nombre = input('Ingrese el nombre o ID del vendedor o nombre de artículo que desea consultar: ')
        print('\n')
        inventario = leer_archivo('inventario')
        empleados = leer_archivo('lista_vendedores')
        for j in range(0,len(empleados)):     
            #Si el elemento 0 (ID) o 1 (nombre) de la lista actual coincide con el nombre que ingresó el usuario
            if nombre == empleados[j][0] or nombre == empleados[j][1]:
                #Se guarda el ID del empleado que tuvo la coincidencia para utilizarlo en la función leer, pues se requiere enviar el nombre del archivo a la función
                archivo = str(empleados[j][0])
                reporte = leer_archivo(f'{archivo}_reporte')  
                for lista in range (len(reporte)):
                    #En estas variables se guarda la suma del elemento en la lista que correspone a los artículos vendidos (1) y al total de venta (2)
                    total_art += int(reporte[lista][1])
                    total_vent +=  int(reporte[lista][2])
                #Se agregan estas dos variables a una lista busqueda
                busqueda.append(str(total_art))    
                busqueda.append(str(total_vent))
                #Se envía dicha lista a una función para que se imprima con un espaciado con el que se muestre de manera ordenada al usuario
                print('   Art Vendidos      Total\n')
                imprimir_lista2(busqueda)
                print('\n')
                #En caso de terminar este ciclo, se habrá concluido la búsqueda
                break
        for j in range(0,len(inventario)):   
            #Si el nombre ingresado coincide con el elemento 1 (nombre) de la lista actual en el archivo de inventario
            if  nombre == inventario[j][1]:
                #Quiere decir que se hizo una búsqueda por artículo, por lo tanto, se guarda en una variable el reporte de ventas por artículo
                reporte = leer_archivo('articulo_reporte') 
                #Se guardan los elementos correspondientes al total de artículos vendidos y al total de las ventas de la lista en la que se encontró la coincidencia  
                total_art = int(reporte[j][1])
                total_vent =  int(reporte[j][3])                  
                busqueda.append(str(total_art))    
                busqueda.append(str(total_vent))                
                print('   Art Vendidos        Total\n')
                imprimir_lista2(busqueda)
                print('\n')
                break
        if len(reporte) < 1:
            print('Error: No se encontró el artículo\n')                
    input('Enter para continuar')

#Función que actualiza el archivo de ventas del vendedor correspondiente. Recibe una matriz con las ventas y el nombre del archivo del vendedor.
def reporte_ventas(archivo, nombre):
    matriz = []
    for k in range(len(archivo)):
        matriz.append([])            
        matriz[k].append(archivo[k][1])
        matriz[k].append(archivo[k][3])
        #Se multiplica el elemento de cantidad de artículos por el precio unitario y se almacena
        total = int(archivo[k][3])*int(archivo[k][4])
        matriz[k].append(str(total))
    guarda_matriz(matriz,f'{nombre}_reporte')
    reporte = leer_archivo(f'{nombre}_reporte')
    return reporte

#Función que actualiza el reporte de artículos cuando se hace una venta. No recibe parámetros.
def reporte_articulos():
    matriz = []
    vendedor1 = leer_archivo('1V_reporte')
    vendedor2 = leer_archivo('2V_reporte')
    vendedor3 = leer_archivo('3V_reporte')
    inventario = leer_archivo('inventario')
    for k in range(len(inventario)):
        matriz.append([])            
        matriz[k].append(inventario[k][1])
        #Agrega la suma de los artículos vendidos (por todos los vendedores) en la lista que se encuentra el ciclo.
        total_art = int(vendedor1[k][1]) + int(vendedor2[k][1]) + int(vendedor3[k][1])
        matriz[k].append(str(total_art))
        matriz[k].append(inventario[k][4])
        #Se obtiene el total de las ventas multiplicando el elemento que corresponde al precio por el total de artículos.
        total_vent = total_art * int(inventario[k][4])
        matriz[k].append(str(total_vent))
    guarda_matriz(matriz,'articulo_reporte')
    reporte = leer_archivo('articulo_reporte')
    return reporte

#Función que actualiza todos los archivos cuando se agrega un nuevo artículo. Recibe la lista del artículo que se ingresó.
def actualiza_vendedores (lista):
    reporte = []
    reporte_articulo = []

    venta1 = leer_archivo('1V_ventas')
    venta2 = leer_archivo('2V_ventas')
    venta3 = leer_archivo('3V_ventas')
    reporte1 = leer_archivo('1V_reporte')
    reporte2 = leer_archivo('2V_reporte')
    reporte3 = leer_archivo('3V_reporte')
    articulo = leer_archivo('articulo_reporte')

    venta1.append(lista)
    venta2.append(lista)
    venta3.append(lista)
    
    reporte.append(lista[1])
    reporte.append('0')
    reporte.append('0')

    reporte_articulo.append(lista[1])
    reporte_articulo.append('0')
    reporte_articulo.append(lista[4])
    reporte_articulo.append('0')

    reporte1.append(reporte)
    reporte2.append(reporte)
    reporte3.append(reporte)
    articulo.append(reporte_articulo)

    guarda_matriz(venta1,'1V_ventas') 
    guarda_matriz(venta2,'2V_ventas')  
    guarda_matriz(venta3,'3V_ventas')   
    guarda_matriz(reporte1,'1V_reporte')  
    guarda_matriz(reporte2,'2V_reporte')  
    guarda_matriz(reporte3,'3V_reporte')  
    guarda_matriz(articulo,'articulo_reporte')

#Programa principal
print("***********************************************************************")
print('AUTOX')
print("***********************************************************************")
opc = 0

while opc != "7":
    limpia()
    print("_______________________________________________________________________")
    print("""
        1.-Registrar ventas.
        2.-Registrar llegada de artículos al almacén.
        3.-Consultar datos del inventario.
        4.-Consultar datos de las ventas.
        5.-Mostrar reportes de ventas por vendedor.
        6.-Mostrar reportes de ventas por artículo.
        7.-Salir""")
    print("________________________________________________________________________")
    opc = input('Opción a ejecutar: ')
    
    if opc == "1":
        print("*********************")
        print('Seleccionaste ¡Registrar ventas!')
        print("________________________________________________________________________")
        print("BIENVENIDO A REGISTRO DE VENTAS \n")
        cant_ven=int(input('Cantidad de productos a registrar: \n'))
        if cant_ven>0:
            registrar_ventas(cant_ven)
        else:
            print('Error: El numero que ingresaste es incorrecto o incluiste algunas letras')
        input('Enter para continuar')
    elif opc == "2":
        print("*****************************")
        print('¡Seleccionaste Registrar llegada de artículos al almacén!')
        print("*****************************")
        registrar_llegada_articulos_almacen()
        
    elif opc == "3":
        print("******************************************************************")
        print('¡Seleccionaste Consultar datos del Consultar datos del inventario!')
        print("******************************************************************")
        consultar_datos_inventario()
    elif opc == "4":
        print("*********************************************")
        print('¡Seleccionaste Consultar datos de las ventas!')
        print("*********************************************")
        consultar_datos_ventas()
    elif opc == "5":
        print("*******************************************************")
        print('¡Seleccionaste Mostrar reportes de ventas por vendedor!')
        print("*******************************************************")        
        reportes_ventas_vendedor()
    elif opc == "6":
        print("*******************************************************")
        print('¡Seleccionaste Mostrar reportes de ventas por artículo!')
        print("*******************************************************")  
        reportes_ventas_artículo()        
    elif opc == "7":
        print("***********************************************************************")
        print('Gracias por usar la app de INVETARIOS AUTOX')
        print("***********************************************************************")
    else:
        print("***********************************************************************")
        print('Esa opción no existe :(')
        print("***********************************************************************")
    


