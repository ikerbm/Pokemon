import requests
import random


def obtener_pokemon(id_name) -> dict:
    response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon/{id_name}"
    )

    response.raise_for_status()

    return response.json()


def generar_readme(data: dict) -> str:
    nombre = data["name"].capitalize()

    tipos = "\n".join(
        f"- {tipo['type']['name'].capitalize()}"
        for tipo in data["types"]
    )
    stats = "\n".join(
        f'- {stat["stat"]["name"].capitalize()}: {stat["base_stat"]}'
        for stat in data["stats"]
    )

    return f"""# Pokémon del día

## {nombre}
## ID: {data["id"]}
### Tipos
{tipos}
### Stats
{stats}
"""

if __name__ == "__main__":
    id = random.randint(1, 1028)
    data = obtener_pokemon(id)

    print(data)

    contenido = generar_readme(data)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(contenido)