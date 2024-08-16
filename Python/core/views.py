from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "")

def cadastro(request):
    contexto  = {

    }

    # processa o cadastro do usuario

    return render(request,"", contexto)

def configuracoes(request):
    contexto = {

    }

    # processa as configuracoes


    return render(
        request,
        "",
        contexto
    )

def obtem_mensagem(request):
    pass


def sair(request):
    pass

