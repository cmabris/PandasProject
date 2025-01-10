import pandas as pd

# Crear un DataFrame
data = {
    "Nombre": ["Carlos", "Ana", "Luis", "Elena", "Pedro", "Sara", "Carmen", "Pablo"],
    "Edad": [22, 28, 30, 25, 35, 45, 55, 60],
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla", "Zaragoza", "Bilbao", "Alicante", "Cádiz"],
    "Salario": [2000, 2500, 2200, None, 2100, 3000, 3500, None]
}
df = pd.DataFrame(data)

# Identificar valores nulos
print("\nValores nulos en el DataFrame:\n", df.isnull())

# Contar valores nulos por columna
print("\nConteo de valores nulos por columna:\n", df.isnull().sum())

# Verificar si hay valores nulos en todo el DataFrame
print("\n¿Hay valores nulos en el DataFrame?:", df.isnull().any().any())

