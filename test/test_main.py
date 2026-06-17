
from src.main import *

def test_pokemon_has_name():
    data = obtener_pokemon("pikachu")
    assert data["name"] == "pikachu"