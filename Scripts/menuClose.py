import bge

def menuClose():
    
    # Encontrando e atribuindo o controlador lógico a variável 'cont'
    cont = bge.logic.getCurrentController()
    
    # Se o botão estiver visivel e for clicado, esconde as informações do menu
    if cont.sensors["Mouse Over Close Menu"].positive and cont.sensors["Left Button Close Menu"].positive and bge.logic.getCurrentScene().objects['Menu'].visible == True:
        
        bge.logic.getCurrentScene().objects['Menu'].setVisible(False)
        bge.logic.getCurrentScene().objects['Close Menu Button'].setVisible(False)
        bge.logic.getCurrentScene().objects['Help Button'].setVisible(False)
        bge.logic.getCurrentScene().objects['End Button'].setVisible(False)
            
menuClose()