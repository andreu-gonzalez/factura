from factura import factura
from facturacontroller import facturacontoller
from datetime import datetime
con = facturacontoller()
lista=[]
while True:
    print("1-Añadir factura")
    print("2-Listar facturas no pagadas")
    print("3-Listar facturas pagadas")
    print("4-Pagar")
    print("5-Salir")

    while True:
        try:
            opcion=int(input("Que opcion eliges"))
            break
        except ValueError:
            print("Solo numeros") 
    if opcion == 1:
        id=input("Dime la id de la factur")
        now = datetime.now()
        fecha = now.strftime("%d/%m/%Y %H:%M")
        nife=input("Dime el nif del emisor")
        nifr=input("Dime el nif del receptor")
        fac = factura(id,fecha,nife,nifr)
        if con.addfactura(fac)==True:
            print("Se ha guardado")
        else:
            print("No se ha guardado")
        while True:
            print("¿Qué productos quieres añadir?")
            #productos
            print(con.mostrarProductos())
            
            producto=input("Selecciona uno(para acabar pon fin)")

            if producto=="fin":
                break
            else:
                cantidad=input("escoga una cantidad ")
                if con.registrarlinea(id,producto,cantidad):
                    print("Linea añadida")
                    print()
                else:
                    print("Error al añadir la linea")
                    print()    
    if opcion==2:
        print("***LISTA FACTURAS PENDIENTES DE PAGO**")
        listafacturas = con.listar()
        if (len(listafacturas)==0):
            print("Aun no hay facturas")
        else:
            print("1-Totales")
            print("2-NIF EMISOR")
            print("3-NIF RECEPTOR")
            while True:
                try:
                 opcion=int(input("Que opcion eliges"))
                 break
                except ValueError:
                    print("Solo numeros") 
            if opcion ==1:
                pagada= False
                for i in listafacturas:
                    if pagada == listafacturas[i].getPagada():
                        print("ID",listafacturas[i].getId())
                        print("fecha",listafacturas[i].getFecha())
                        print("Nif emisor",listafacturas[i].getNife())
                        print("Nif receptor",listafacturas[i].getNifr())
                        print("Pagado",listafacturas[i].getPagada())
                        print("base",listafacturas[i].getBase())
                        print("total",listafacturas[i].getTotal())
                        print("Lineas",listafacturas[i].mostrar())
               
            if opcion ==2:
                pagada= False
                nife=input("Dime el nif del emisor")
                for i in listafacturas:
                    if pagada == listafacturas[i].getPagada():
                        if nife == listafacturas[i].getNife():
                            print("ID",listafacturas[i].getId())
                            print("fecha",listafacturas[i].getFecha())
                            print("Nif emisor",listafacturas[i].getNife())
                            print("Nif receptor",listafacturas[i].getNifr())
                            print("Pagado",listafacturas[i].getPagada())
                            print("base",listafacturas[i].getBase())
                            print("total",listafacturas[i].getTotal())
                            print("Lineas",listafacturas[i].mostrar())
            if opcion ==3:
                pagada= False
                nifr=input("Dime el nif del emisor")
                for i in listafacturas:
                    if pagada == listafacturas[i].getPagada():
                        if nifr == listafacturas[i].getNifr():
                            print("ID",listafacturas[i].getId())
                            print("fecha",listafacturas[i].getFecha())
                            print("Nif emisor",listafacturas[i].getNife())
                            print("Nif receptor",listafacturas[i].getNifr())
                            print("Pagado",listafacturas[i].getPagada())
                            print("base",listafacturas[i].getBase())
                            print("total",listafacturas[i].getTotal())
                            print("Lineas",listafacturas[i].mostrar())
    if opcion==3:
        print("***LISTA FACTURAS PAGO**")
        listafacturas = con.listar()
        if (len(listafacturas)==0):
            print("Aun no hay facturas")
        else:
            print("1-Totales")
            print("2-NIF EMISOR")
            print("3-NIF RECEPTOR")
            while True:
                try:
                 opcion=int(input("Que opcion eliges"))
                 break
                except ValueError:
                    print("Solo numeros") 
            if opcion ==1:
                pagada= True
                for i in listafacturas:
                    if pagada == listafacturas[i].getPagada():
                            print("ID",listafacturas[i].getId())
                            print("fecha",listafacturas[i].getFecha())
                            print("Nif emisor",listafacturas[i].getNife())
                            print("Nif receptor",listafacturas[i].getNifr())
                            print("Pagado",listafacturas[i].getPagada())
                            print("base",listafacturas[i].getBase())
                            print("total",listafacturas[i].getTotal())
                            print("Lineas",listafacturas[i].mostrar())
            if opcion ==2:
                pagada= True
                nife=input("Dime el nif del emisor")
                for i in listafacturas:
                    if pagada == listafacturas[i].getPagada():
                        if nife == listafacturas[i].getNife():
                            print("ID",listafacturas[i].getId())
                            print("fecha",listafacturas[i].getFecha())
                            print("Nif emisor",listafacturas[i].getNife())
                            print("Nif receptor",listafacturas[i].getNifr())
                            print("Pagado",listafacturas[i].getPagada())
                            print("base",listafacturas[i].getBase())
                            print("total",listafacturas[i].getTotal())
                            print("Lineas",listafacturas[i].mostrar())
            if opcion ==3:
                pagada= True
                nifr=input("Dime el nif del emisor")
                for i in listafacturas:
                    if pagada == listafacturas[i].getPagada():
                        if nifr == listafacturas[i].getNifr():
                            print("ID",listafacturas[i].getId())
                            print("fecha",listafacturas[i].getFecha())
                            print("Nif emisor",listafacturas[i].getNife())
                            print("Nif receptor",listafacturas[i].getNifr())
                            print("Pagado",listafacturas[i].getPagada())
                            print("base",listafacturas[i].getBase())
                            print("total",listafacturas[i].getTotal())
                            print("Lineas",listafacturas[i].mostrar())
    if opcion==4:
        id=input("Introduce el id de la factura: ")

        if con.facturaPagada(id):
            print("Factura Pagada!")
        else:
            print("Error al pagar la factura!")                        