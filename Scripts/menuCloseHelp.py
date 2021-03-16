import bge

def menuCloseHelp():
    
    # Encontrando e atribuindo o controlador lógico a variável 'cont'
    cont = bge.logic.getCurrentController()
    
    # Se o botão estiver visivel e for clicado, esconde as informações de ajuda   
    if cont.sensors["Mouse Over Help Close"].positive and cont.sensors["Left Button Help Close"].positive and bge.logic.getCurrentScene().objects['Help Close Button'].visible:
        
        bge.logic.getCurrentScene().objects['Help'].setVisible(False)
        bge.logic.getCurrentScene().objects['Help Close Button'].setVisible(False)
            
menuCloseHelp()