import bge

def polyhedronsProperties():
    
    # Encontrando e atribuindo o controlador lógico a variável 'cont'
    cont = bge.logic.getCurrentController()
    
    # Se o botão for clicado e as propriedades não estiverem visíveis, as mostra    
    if cont.sensors["Mouse Over Properties"].positive and cont.sensors["Left Button Properties"].positive and bge.logic.getCurrentScene().objects['Polyhedrons Properties'].visible == False:
        
        bge.logic.getCurrentScene().objects['Polyhedrons Properties'].setVisible(True)
        
    # Se o botão for clicado e as propriedades estiverem visíveis, as esconde            
    elif cont.sensors["Mouse Over Properties"].positive and cont.sensors["Left Button Properties"].positive and bge.logic.getCurrentScene().objects['Polyhedrons Properties'].visible == True:
        
        bge.logic.getCurrentScene().objects['Polyhedrons Properties'].setVisible(False)
            
polyhedronsProperties()