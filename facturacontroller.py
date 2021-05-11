from factura import factura
class facturacontoller:
    def __init__(self):
        self.listafacturas ={}
        self.productos={'puerta':5,'tornillo':10,'martillo':3}

    def addfactura(self,factura):
        if factura.getId() not in self.listafacturas:
            self.listafacturas[factura.getId()] = factura
            return True
        return False

    def listar(self):
        return self.listafacturas            
    def mostrarProductos(self):
        listaProductos=""
        for i in self.productos:
            listaProductos+=" - "+str(i)+"\n"

        return listaProductos

    def facturaPagada(self,id):
        if id in self.listafacturas:
            self.listafacturas[id].facturaPagada()
            return True

        return False
    def registrarlinea(self,id,producto,cantidad):
        if id in self.listafacturas:
            if producto in self.productos:

                base=self.productos[producto]*int(cantidad)
                self.listafacturas[id].addLineaFactura(producto,cantidad,base)
                return True
        return False
   

    