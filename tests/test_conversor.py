import sys 
import os 

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src')) 
from conversor import celsius_a_fahrenheit, fahrenheit_a_celsius, celsius_a_kelvin, kelvin_a_celsius 

def test_celsius_a_fahrenheit(): 
    assert celsius_a_fahrenheit(0) == 32 
    assert celsius_a_fahrenheit(100) == 212 

def test_fahrenheit_a_celsius(): 
    assert fahrenheit_a_celsius(32) == 0 
    assert fahrenheit_a_celsius(212) == 100 

def test_celsius_a_kelvin(): 
    assert celsius_a_kelvin(0) == 273.15 

def test_kelvin_a_celsius(): 
    assert kelvin_a_celsius(273.15) == 0 

def test_kelvin_negativo(): 
    try: 
        kelvin_a_celsius(-5) 
        assert False 
    except ValueError: 
        assert True
