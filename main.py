import pandas as pd

from data.data1 import apartamento1,apartamento2
from helpers.crearTablasHTML import crearTabla
from helpers.creargrafica import graficarPromedio
from helpers.crearTorta import graficarTortaSalarios

from fpdf import FPDF

tabla1=pd.DataFrame(apartamento1,columns=['edad'])
tabla2=pd.DataFrame(apartamento2,columns=['edad'])
tabla3=pd.read_csv("./data/empleados.csv")

#FILTRANDO O APLICANDO CONDICIONES A MI DATAFRAME
analistas1=tabla3.query('cargo=="analista1"')
analistas2=tabla3.query('cargo=="analista2"')
jubilados=tabla3.query('edad>=50')

#Generemos las tablas para el reporte
crearTabla(analistas1,"analistas1")
crearTabla(analistas2,"analistas2")
crearTabla(jubilados,"jubilados")

#Generamos graficas
graficarPromedio(jubilados,'cargo','salario','graficaJubilados')
graficarTortaSalarios(analistas1,[20,30,40,50,60],'edad','salario','promediosAnalistas1')
graficarTortaSalarios(analistas2,[20,30,40,50,60],'edad','salario','promediosAnalistas1')





'''# Crear instancia de la clase FPDF
pdf = FPDF()
# Agregar página
pdf.add_page()
# Establecer fuente y tamaño de letra
pdf.set_font("Arial", size=12)
# Establecer color de línea
pdf.set_draw_color(0, 0, 0)  # Color negro
# Dibujar título de la tabla
pdf.cell(200, 10, txt="Tabla de analistas1:", ln=1, align="L")
# Obtener los datos de la tabla analistas1
tabla_analistas1 = analistas1.to_string()
# Dividir los datos en filas
filas = tabla_analistas1.split("\n")
# Dibujar filas y columnas de la tabla
for fila in filas:
    columnas = fila.split()
    for columna in columnas:
        pdf.cell(40, 10, txt=columna, border=1)  # Dibuja celda con borde
    pdf.ln()  # Cambia de línea al final de cada fila
# Agregar espacio adicional después de la tabla
pdf.ln(10)
# Guardar archivo PDF
pdf.output("archivo.pdf")'''



