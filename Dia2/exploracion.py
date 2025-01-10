import pandas as pd

# Crear un DataFrame
data = {
    "Nombre": ["Carlos", "Ana", "Luis", "Elena", "Pedro", "Sara", "Carmen", "Pablo"],
    "Edad": [22, 28, 30, 25, 35, 45, 55, 60],
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla", "Zaragoza", "Bilbao", "Alicante", "Cádiz"],
    "Salario": [2000, 2500, 2200, None, 2100, 3000, 3500, None]
}
df = pd.DataFrame(data)

# Ver las primeras filas
print("Primeras filas del DataFrame:\n", df.head())

# Ver las últimas filas
print("\nÚltimas filas del DataFrame:\n", df.tail())

# Información general del DataFrame
print("\nInformación del DataFrame:")
print(df.info())

# Dimensiones del DataFrame
print("\nDimensiones del DataFrame:", df.shape)

# Nombres de las columnas
print("\nNombres de las columnas:", df.columns)

# Tipos de datos de cada columna
print("\nTipos de datos de cada columna:\n", df.dtypes)

