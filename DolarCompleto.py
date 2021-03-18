import DolarClass

#ACÁ LO QUE VOY A HACER ES LLAMAR A LOS DISTINTOS MÓDULOS DE DÓLAR PARA MODULARIZAR TODO
#ESTE SCRIPT VA A SER SÓLO UNA INTERFAZ

class DolarCompleto:

    dolarOficial = DolarClass.Dolar("https://www.dolarhoy.com/cotizaciondolaroficial")
    dolarBlue = DolarClass.Dolar("https://www.dolarhoy.com/cotizaciondolarblue")
    dolarBolsa = DolarClass.Dolar("https://www.dolarhoy.com/cotizaciondolarbolsa")
    dolarLiqui = DolarClass.Dolar("https://www.dolarhoy.com/cotizaciondolarcontadoconliqui")

    @classmethod
    def BlueValorCompra(cls):
        return cls.dolarBlue.GetValorCompra()

    @classmethod
    def BlueValorVenta(cls):
        return cls.dolarBlue.GetValorVenta()

    @classmethod
    def OficialValorCompra(cls):
        return cls.dolarOficial.GetValorCompra()

    @classmethod
    def OficialValorVenta(cls):
        return cls.dolarOficial.GetValorVenta()

    @classmethod
    def BolsaValorCompra(cls):
        return cls.dolarBolsa.GetValorCompra()

    @classmethod
    def BolsaValorVenta(cls):
        return cls.dolarBolsa.GetValorVenta()

    @classmethod
    def ContadoConLiquiValorCompra(cls):
        return cls.dolarLiqui.GetValorCompra()

    @classmethod
    def ContadoConLiquiValorVenta(cls):
        return cls.dolarLiqui.GetValorVenta()  