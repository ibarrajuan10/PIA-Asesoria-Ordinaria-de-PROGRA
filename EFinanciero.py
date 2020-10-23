class EstadoFinanciero:
    def __init__(self,MPDI,PPI,ATI,MPDF,PPF,ATF,MODF,CMPDF,GIDFF,GCMPDF,DRCMPDF):
        self.__MPDI=MPDI
        self.__PPI=PPI
        self.__ATI=ATI
        self.__MPDF=MPDF
        self.__PPF=PPF
        self.__ATF=ATF
        self.__MODF=MODF
        self.__CMPDF=CMPDF
        self.__GIDFF=GIDFF
        self.__GCMPDF=GCMPDF
        self.__DRCMPDF=DRCMPDF
    
    def RealizarEF(self):
        ComprasTotales=(self.__CMPDF+self.__GCMPDF)
        ComprasNetasDeMateriales=(ComprasTotales-self.__DRCMPDF)
        MaterialesDisponibles=(ComprasNetasDeMateriales+self.__MPDI)
        MateriaPrimaUtilizada=(MaterialesDisponibles-self.__MPDF)
        CostoPrimo=(MateriaPrimaUtilizada+self.__MODF)
        CostoIncurrido=(CostoPrimo+self.__GIDFF)
        TotalDeProduccionEnProcesos=(CostoIncurrido+self.__PPI)
        CostoDeProduccion=(TotalDeProduccionEnProcesos-self.__PPF)
        TotalDeArticulosListosParaLaVenta=(CostoDeProduccion+self.__ATI)
        CostoDeProduccionDeLoVendido=(TotalDeArticulosListosParaLaVenta-self.__ATF)
        
        print(f"Estas son tus Compras Totales : {ComprasTotales} ")
        print(f"Estas son tus Compras Netas De Materiales : {ComprasNetasDeMateriales} ")
        print(f"Estas son tus Materiales Disponibles : {MaterialesDisponibles} ")
        print(f"Esta es tu Materia Prima Utilizada : {MateriaPrimaUtilizada} ")
        print(f"Esto es tu Costo Primo : {CostoPrimo} ")
        print(f"Este es tu Costo Incurrido/Costo Previo : {CostoIncurrido} ")
        print(f"Este es tu Total De Produccion En Procesos : {TotalDeProduccionEnProcesos} ")
        print(f"Este es tu Costo De Produccion : {CostoDeProduccion} ")
        print(f"Esto es tu Total De Articulos Listos Para La Venta : {TotalDeArticulosListosParaLaVenta} ")
        print(f"Este es tu Costo de Produccion De Lo Vendido : { CostoDeProduccionDeLoVendido} ")
        print("-"*100)