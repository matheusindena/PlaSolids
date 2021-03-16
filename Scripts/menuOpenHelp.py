import bge

def menuOpenHelp():
    
    # Encontrando e atribuindo o controlador lógico a variável 'cont'
    cont = bge.logic.getCurrentController()
    
    # Se o botão estiver visivel e for clicado, mostra as informações de ajuda
    if cont.sensors["Mouse Over Help"].positive and cont.sensors["Left Button Help"].positive and bge.logic.getCurrentScene().objects['Help Button'].visible:
        
        bge.logic.getCurrentScene().objects['Help'].setVisible(True)
        bge.logic.getCurrentScene().objects['Help Close Button'].setVisible(True)
            
menuOpenHelp()