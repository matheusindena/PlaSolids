import bge

def tipProperties():
    
    # Encontrando e atribuindo o controlador lógico a variável 'cont'
    cont = bge.logic.getCurrentController()
    
    # Verifica se o mouse está por cima do botão ajuda e se a dica não está visivel
    if cont.sensors["Mouse Over Properties"].positive and bge.logic.getCurrentScene().objects['Polyhedrons Properties Tip'].visible == False:
        
        # Mostra a dica
        bge.logic.getCurrentScene().objects['Polyhedrons Properties Tip'].setVisible(True)
        
    # Verifica se o mouse não está por cima do botão ajuda e se a dica está visivel    
    elif cont.sensors["Mouse Over Properties"].positive == False and bge.logic.getCurrentScene().objects['Polyhedrons Properties Tip'].visible:
        
        # Esconde a dica
        bge.logic.getCurrentScene().objects['Polyhedrons Properties Tip'].setVisible(False) 
            
tipProperties()