import bge

def menuEnd():

    # Encontrando e atribuindo o controlador lógico a variável 'cont'
    cont = bge.logic.getCurrentController()

    # Se o botão estiver visivel e for clicado, encerra o programa
    if cont.sensors["Mouse Over End"].positive and cont.sensors["Left Button End"].positive and bge.logic.getCurrentScene().objects['End Button'].visible:
        
        bge.logic.endGame()
        
menuEnd()