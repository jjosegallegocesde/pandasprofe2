import matplotlib.pyplot as plt


def graficarPromedio(dataFrame,columnaEjeX,columnaInteres,nombreGrafica):

    colores = ['blue', 'green', 'red', 'orange']

    salario_promedio = dataFrame.groupby(columnaEjeX)[columnaInteres].mean()
    plt.bar(salario_promedio.index, salario_promedio,color=colores)
    plt.xlabel('Cargo')
    plt.ylabel('Salario Promedio')
    plt.title('Salario Promedio por Cargo para Jubilados')
    plt.savefig(f'./assets/img/{nombreGrafica}.png', dpi=300, bbox_inches='tight')
