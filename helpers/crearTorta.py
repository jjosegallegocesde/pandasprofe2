import matplotlib.pyplot as plt
import pandas as pd

def graficarTortaSalarios(dataFrame,rangos,columnaInteresRango,columnaAPromediar,nombreGrafica):

    fig2 = plt.figure()
    # Crear la columna de rangos de edad
    dataFrame['rango_nuevo'] = pd.cut(dataFrame[columnaInteresRango], bins=rangos)
    # Calcular la suma del salario por rango de edad
    salarioPorRango = dataFrame.groupby('rango_nuevo')[columnaAPromediar].sum()
    # Obtener los datos de salario y rango de edad
    salario = salarioPorRango.values
    rangosEdad = salarioPorRango.index
    # Crear la gráfica de torta
    #plt.pie(salario, labels=rangosEdad, autopct='%1.1f%%')
    plt.pie(salario, labels=rangosEdad, autopct='%1.1f%%')
    plt.title('Distribución del salario por rango de edad')
    plt.savefig(f'./assets/img/{nombreGrafica}.png', dpi=300, bbox_inches='tight')
