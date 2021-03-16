import bge

def showIcosahedron():
    
    # Encontrando e atribuindo o controlador lógico a variável 'cont'
    cont = bge.logic.getCurrentController()
    
    # Variavel que armazana um booleano se o botão mostrar icosaedro foi clicado ou não
    icosahedronButtonClicked = cont.sensors["Mouse Over Icosahedron Button"].positive and cont.sensors["Left Button Icosahedron Button"].positive
    
    # Verifica se o botão foi clicado e se o icosaedro já não está visível
    if icosahedronButtonClicked and bge.logic.getCurrentScene().objects['Icosahedron'].visible ==  False:
        
        # Mostra o icosaedro e esconde todos os outros sólidos                
        bge.logic.getCurrentScene().objects['Tetrahedron'].setVisible(False)
        bge.logic.getCurrentScene().objects['Tetrahedron Information'].setVisible(False)
        bge.logic.getCurrentScene().objects['Tetrahedron Vertices'].setVisible(False)
        bge.logic.getCurrentScene().objects['Tetrahedron Edges'].setVisible(False)
        bge.logic.getCurrentScene().objects['Tetrahedron Faces'].setVisible(False)
        
        bge.logic.getCurrentScene().objects['Cube'].setVisible(False)
        bge.logic.getCurrentScene().objects['Cube Information'].setVisible(False)
        bge.logic.getCurrentScene().objects['Cube Vertices'].setVisible(False)
        bge.logic.getCurrentScene().objects['Cube Edges'].setVisible(False)
        bge.logic.getCurrentScene().objects['Cube Faces'].setVisible(False)
        
        bge.logic.getCurrentScene().objects['Octahedron'].setVisible(False)
        bge.logic.getCurrentScene().objects['Octahedron Information'].setVisible(False)
        bge.logic.getCurrentScene().objects['Octahedron Vertices'].setVisible(False)
        bge.logic.getCurrentScene().objects['Octahedron Edges'].setVisible(False)
        bge.logic.getCurrentScene().objects['Octahedron Faces'].setVisible(False)
        
        bge.logic.getCurrentScene().objects['Dodecahedron'].setVisible(False)
        bge.logic.getCurrentScene().objects['Dodecahedron Information'].setVisible(False)
        bge.logic.getCurrentScene().objects['Dodecahedron Vertices'].setVisible(False)
        bge.logic.getCurrentScene().objects['Dodecahedron Edges'].setVisible(False)
        bge.logic.getCurrentScene().objects['Dodecahedron Faces'].setVisible(False)
        
        bge.logic.getCurrentScene().objects['Icosahedron'].setVisible(True)
        
        bge.logic.setAnimRecordFrame(0)
    
showIcosahedron()