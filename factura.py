class factura:
    def __init__(self,id,fecha,nife,nifr):
        self.id=id
        self.fecha=fecha
        self.nife=nife
        self.nifr=nifr
        self.base=0
        self.iva=21
        self.total=0
        self.pagada=False
        self.lineas = []
      

    def getNlineas(self):
        return self.Nlineas    
    def setNlineas(self):
        self.Nlineas = self.Nlineas+1
    def getId(self):
        return self.id

    def getFecha(self):
        return self.fecha

    def getNife(self):
        return self.nife

    def getNifr(self):
        return self.nifr

    def getPagada(self):
        return self.pagada

    def getBase(self):
        return self.base

    def getIva(self):
        return self.iva

    def getTotal(self):
        return self.total

    def getLineas(self):
        return self.lineas
                                          
    def setLineas(self,nombre,cantidad,total):
        if nombre in self.lineas:
            self.lineas[nombre] += cantidad
     
    def addLineaFactura(self,producto,cantidad,base):
        self.base+=base
        self.total=self.base+(self.base*(self.iva/100))
        self.lineas.append((producto,cantidad,base))        
    def mostrarLineasFactura(self):
        lineasS=""
        for i in self.lineas:
            lineasS+="\t"+str(i[0])+"\t"+str(i[1])+"\t"+str(i[2])+"\n\t"

        return lineasS  
    def facturaPagada(self):
        self.pagada=True    