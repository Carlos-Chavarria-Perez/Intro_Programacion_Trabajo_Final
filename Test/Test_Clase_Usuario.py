import unittest
from unittest.mock import patch
from Clase_Usuario import Usuario

class TestUsuario(unittest.TestCase):
    def test_registrar_usuario(self):
        username = "NuevoUsuario"
        password = "nuevacontraseña"
        integrante = "IntegranteNuevo"

        usuario = Usuario(username, password, integrante)

        Usuario.lista_usuarios = []

        self.assertEqual(usuario.username, username)
        self.assertEqual(usuario.password, password)