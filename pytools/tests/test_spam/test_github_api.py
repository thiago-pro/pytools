from pytools import github_api


def test_buscar_avatar():
    url = github_api.buscar_avatar('thiago-pro')
    assert 'https://avatars.githubusercontent.com/u/68643085?v=4' == url
