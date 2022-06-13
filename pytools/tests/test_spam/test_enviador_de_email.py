import pytest

from pytools.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['foo@bar.com.br', 'thiago0743@hotmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'thiago.silva@guibon.com.br',
        'Modulo do curso pytools',
        'Primeira turma Guido Von Rossum aberta.'
    )
    assert destinatario in resultado
