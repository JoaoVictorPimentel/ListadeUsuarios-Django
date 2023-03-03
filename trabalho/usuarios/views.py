from django.shortcuts import render

usuarios = [
    {
        'id': 1,
        'titulo': 'Usuário um'
    },
    {
        'id': 2,
        'titulo': 'Usuário dois'
    },
    {
        'id': 3,
        'titulo': 'Usuário três'
    }
]

def listarUsuarios(request):
    context = {
        'usuarios': usuarios
    }
    return render(request, 'listar_usuarios.html', context)

def detalharUsuario(request, id):
    usuario = usuarios[id-1]
    return render(request, 'detalhe_usuario.html', {'usuario': usuario})

