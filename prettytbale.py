import pretty_tables

headers = ["S.No", "Pokemon", "Type"]

rows = [
    [1, "Pikachu", "Electric"],
    [2, "Squirtle", "Water"],
    [3, "Charmander", "Fire"],
    [4, "Bulbasaur", "Grass"],
]

colors = [
    pretty_tables.Colors.red,
    pretty_tables.Colors.green,
    pretty_tables.Colors.purple,

]

table = pretty_tables.create(
    headers = headers,
    rows = rows,
    colors = colors,
)

print(table)