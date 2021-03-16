import bge

def programRestart():
    
    # Encontrando e atribuindo o controlador lógico a variável 'cont'
    cont = bge.logic.getCurrentController()

    # Se o botão for clicado, reinicia o programa para sua configuração inicial
    if cont.sensors["Mouse Over Restart"].positive and cont.sensors["Left Button Restart"].positive:
        
        bge.logic.restartGame()
        
programRestart()