import pandas as pd

notas = pd.Series([8.5, 6.0, 9.5, 7.0], index=["Ana", "Bruno", "Carla", "Diego"])

print("Notas dos colegas:")
print(notas)
print("media da turma:", notas.mean())
print("maior nota:", notas.idxmax(), "com", notas.max())
print("menor nota:", notas.idxmin(), "com", notas.min())

filmes = pd.DataFrame({
    "titulo": ["Cidade de Deus", "Central do Brasil", "O Auto da Compadecida", "Tropa de Elite", "Ainda Estou Aqui"],
    "ano": [2002, 1998, 2000, 2007, 2024],
    "nota": [9.0, 8.5, 9.5, 8.0, 8.8],
})

print("\nTabela de filmes:")
print(filmes)
print("\nUma coluna:")
print(filmes["titulo"])
print("\nDuas colunas:")
print(filmes[["titulo", "nota"]])
print("\nTipos das colunas:")
print(filmes.dtypes)
