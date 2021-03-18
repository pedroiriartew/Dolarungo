#Importamos Flask
from flask import Flask, render_template
import DolarCompleto

#Generamos instancia de Flask en app
app = Flask(__name__)

#Generamos primer ruta con @app.route
@app.route("/")
def index():
        

    return render_template(
        "index.html",
        valor_DB_compra = DolarCompleto.DolarCompleto.BlueValorCompra(),
        valor_DB_venta = DolarCompleto.DolarCompleto.BlueValorVenta(),
        valor_DO_compra = DolarCompleto.DolarCompleto.OficialValorCompra(),
        valor_DO_venta = DolarCompleto.DolarCompleto.OficialValorVenta(),
        valor_DBol_compra = DolarCompleto.DolarCompleto.BolsaValorCompra(),
        valor_DBol_venta = DolarCompleto.DolarCompleto.BolsaValorVenta(),
        valor_DC_compra = DolarCompleto.DolarCompleto.ContadoConLiquiValorCompra(),
        valor_DC_venta = DolarCompleto.DolarCompleto.ContadoConLiquiValorVenta()
    )
#La ruta siempre responde con una función (La primera que tiene debajo en este caso index)

#Validar que estemos en este módulo
if __name__ == "__main__":
    app.run(debug=True, port=3000)