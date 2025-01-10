import pandas as pd

# Crear un DataFrame
data = {
    "Nombre": ["Carlos", "Ana", "Luis", "Elena", "Pedro", "Sara", "Carmen", "Pablo"],
    "Edad": [22, 28, 30, 25, 35, 45, 55, 60],
    "Ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla", "Zaragoza", "Bilbao", "Alicante", "Cádiz"],
    "Salario": [2000, 2500, 2200, None, 2100, 3000, 3500, None]
}
df = pd.DataFrame(data)

# Estadísticas descriptivas para columnas numéricas
print("\nEstadísticas descriptivas para columnas numéricas:\n", df.describe())

# Estadísticas descriptivas para columnas categóricas
print("\nEstadísticas descriptivas para columnas categóricas:\n", df.describe(include='object'))

