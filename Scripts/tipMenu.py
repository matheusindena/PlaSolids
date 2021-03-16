import bge

def tipMenu():
    
    # Encontrando e atribuindo o controlador lógico a variável 'cont'
    cont = bge.logic.getCurrentController()
    
    # Verifica se o mouse está por cima do botão fechar e se a dica não está visivel
    if cont.sensors["Mouse Over Open Menu"].positive and bge.logic.getCurrentScene().objects['Open Menu Tip'].visible == False:
        
        # Esconde a dica
        bge.logic.getCurrentScene().objects['Open Menu Tip'].setVisible(True)   
        
    # Verifica se o mouse não está por cima do botão ajuda e se a dica está visivel    
    elif cont.sensors["Mouse Over Open Menu"].positive == False and bge.logic.getCurrentScene().objects['Open Menu Tip'].visible:
        
        # Esconde a dica
        bge.logic.getCurrentScene().objects['Open Menu Tip'].setVisible(False)
            
tipMenu()