import bge

def tipInformation():
    
    # Encontrando e atribuindo o controlador lógico a variável 'cont'
    cont = bge.logic.getCurrentController()
    
    # Verifica se o mouse está por cima do botão ajuda e se a dica não está visivel
    if cont.sensors["Mouse Over Information"].positive and bge.logic.getCurrentScene().objects['Information Button Tip'].visible == False:
        
        # Mostra a dica
        bge.logic.getCurrentScene().objects['Information Button Tip'].setVisible(True)
        
    # Verifica se o mouse não está por cima do botão ajuda e se a dica está visivel    
    elif cont.sensors["Mouse Over Information"].positive == False and bge.logic.getCurrentScene().objects['Information Button Tip'].visible:
        
        # Esconde a dica
        bge.logic.getCurrentScene().objects['Information Button Tip'].setVisible(False) 
            
tipInformation()