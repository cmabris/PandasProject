import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("Titanic-Dataset.csv")

# Verificar el contenido del DataFrame
print("Contenido del Dataframe:\n", df)
print("\nInformación del DataFrame:\n", df.info())

print("Valores nulos por columna:\n", df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].mean())

print("Valores nulos por columna:\n", df.isnull().sum())

# Eliminar columnas con más del 50% de valores nulos
umbral = len(df) * 0.5

columns_to_drop = df.columns[df.isnull().sum() > umbral]

df_cleaned = df.drop(columns=columns_to_drop)
print("Contenido del Dataframe limpio:\n", df_cleaned)

# Convertir la columna Embarked a tipo categórico
df["Embarked"] = df["Embarked"].astype("category")
print("Contenido del Dataframe con tipo de datos cambiados:\n", df)






