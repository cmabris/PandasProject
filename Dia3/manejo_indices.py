import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    "Producto": ["Manzanas", "Plátanos", "Naranjas", "Peras", "Piñas", "Sandías"],
    "Precio": [1.2, 0.8, 1.5, 1.3, 1.4, 1.1],
    "Stock": [100, 150, 120, 90, 100, 100]
}
df = pd.DataFrame(data)
print("DataFrame original:\n", df)

# Configurar un índice

df_indexado = df.set_index("Producto")
print("DataFrame indexado:\n", df_indexado)

# Convertir el índice en una columna
df_reset = df_indexado.reset_index()
print("DataFrame reseteado:\n", df_reset)

# Modificar las etiquetas
df_indexado.index = ["A", "B", "C", "D", "E", "F"]
print("DataFrame con índice modificado:\n", df_indexado)

df_reset = df_indexado.reset_index()
print("DataFrame reseteado:\n", df_reset)

# Acceso y selección de datos usando índices
fila = df_indexado.loc["A"]
print("Fila con índice A:\n", fila)

varias_filas = df_indexado.loc[["A", "C"]]
print("Filas seleccionadas:\n", varias_filas)

# Índices jerárquicos
multi_index = pd.MultiIndex.from_tuples(
    [("Frutas", "Manzanas"), ("Frutas", "Plátanos"), ("Frutas", "Naranjas"), ("Frutas", "Peras"), ("Frutas", "Piñas"), ("Frutas", "Sandías")],
    names=["Categoría", "Producto"]
)
df_multi = pd.DataFrame(data, index=multi_index).drop(columns="Producto")
print("Dataframe con índices jerárquicos:\n", df_multi)












