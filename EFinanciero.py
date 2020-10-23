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
        