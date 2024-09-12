import pandas as pd
path = "./excel/datos.xlsx"
sheet_name="Hoja1"
header = 0
df = pd.read_excel(path, sheet_name=
                   sheet_name, header=header)

print(df)

# Obtener información básica sobre el DataFrame
print("\nInformación Básica:")
print(df.info())

# Mostrar estadísticas descriptivas
print("\nEstadísticas Descriptivas:")
print(df.describe())

# Seleccionar una columna
print("\nSelección de una Columna:")
print(df['Nombre'])

# Filtrar filas basadas en una condición
print("\nFiltrar por Edad:")
print(df[df['Edad'] > 25])

# Ordenar el DataFrame
print("\nOrdenar por Edad:")
print(df.sort_values(by='Edad'))

# Agregar una nueva columna
df['Género'] = ['F', 'M', 'F', 'M']
print("\nDataFrame con Nueva Columna:")
print(df)

# Eliminar una columna
df = df.drop('Género', axis=1)
print("\nDataFrame sin la Columna 'Género':")
print(df)

# Filtrar filas duplicadas
df = df.drop_duplicates()
print("\nDataFrame sin Filas Duplicadas:")
print(df)

# Agregar una nueva fila
nueva_fila = {'Nombre': 'Laura', 'Edad': 26, 'Ciudad': 'Barcelona'}
sdf = df._append(nueva_fila, ignore_index=True)

print("\nDataFrame con Nueva Fila:")
print(sdf)


# Escribir el DataFrame en un nuevo archivo Excel
nombre_archivo = "./excel/nuevo_datos.xlsx"
# El argumento index=False evita que se incluya el índice en el archivo Excel
sdf.to_excel(nombre_archivo, index=False) 