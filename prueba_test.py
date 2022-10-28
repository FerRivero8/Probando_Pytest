import pytest
import main

def test_constructor():
    objeto = main.claseNombre()
    assert objeto.getNombre() == "Pablo"

def test_constructor2():
    objeto = main.claseNombre()
    assert objeto.getNombre() == "Pablo"

def test_constructor3():
    objeto = main.claseNombre()
    assert objeto.getNombre() == "Pablo"

def test_constructor4():
    objeto = main.claseNombre()
    assert objeto.saludar() == "Juan"
