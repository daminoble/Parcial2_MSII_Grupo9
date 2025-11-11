# tests/tests_divisionmonteros.py

# Debería importar desde 'divisionmonteros' y la función 'dividir_monteros'
from funciones.divisionmonteros import dividir_monteros 

def test_dividir_monteros():
    assert dividir_monteros(10, 2) == 5
    assert dividir_monteros(5, 0) is None