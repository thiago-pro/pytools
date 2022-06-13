from pytools.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Thiago', email='thiago0743@hotmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Thiago', email='thiago0743@hotmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

