from unittest.mock import Mock

import pytest

from pytools.spam.main import EnviadorDeSpam
from pytools.spam.enviador_de_email import Enviador
from pytools.spam.modelos import Usuario

@pytest.mark.parametrize(
    'usuarios',
    [
         [
            Usuario(nome='Thiago', email='thiago0743@hotmail.com'),
            Usuario(nome='Valentina', email='thiago0743@hotmail.com')
        ],
        [
            Usuario(nome='Thiago', email='thiago0743@hotmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'thiago0743@hotmail.com',
        'Curso Python Pro',
        'Confira os modulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count

def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Thiago', email='thiago0743@hotmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'thiago0743@hotmail.com',
        'Curso Python Pro',
        'Confira os modulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'thiago0743@hotmail.com',
        'thiago0743@hotmail.com',
        'Curso Python Pro',
        'Confira os modulos fantásticos'
    )
