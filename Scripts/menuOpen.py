import bge

def menuOpen():
    
    # Encontrando e atribuindo o controlador lógico a variável 'cont'
    cont = bge.logic.getCurrentController()
    
    # Se o botão for clicado e o menu não estiver visível, mostra todas as informações do mesmo   
    if cont.sensors["Mouse Over Open Menu"].positive and cont.sensors["Left Button Open Menu"].positive and bge.logic.getCurrentScene().objects['Menu'].visible == False:
        
        bge.logic.getCurrentScene().objects['Menu'].setVisible(True)
        bge.logic.getCurrentScene().objects['Close Menu Button'].setVisible(True)
        bge.logic.getCurrentScene().objects['Help Button'].setVisible(True)
        bge.logic.getCurrentScene().objects['End Button'].setVisible(True)
            
menuOpen()