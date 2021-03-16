import bge

def showTetrahedron():
    
    # Encontrando e atribuindo o controlador lógico a variável 'cont'
    cont = bge.logic.getCurrentController()
    
    # Variavel que armazana um booleano se o botão mostrar tetraedro foi clicado ou não
    tetrahedronButtonClicked = cont.sensors["Mouse Over Tetrahedron Button"].positive and cont.sensors["Left Button Tetrahedron Button"].positive
    
    # Verifica se o botão foi clicado e se o tetraedro já não está visível
    if tetrahedronButtonClicked and bge.logic.getCurrentScene().objects['Tetrahedron'].visible ==  False:
        
        # Mostra o tetraedro e esconde todos os outros sólidos                
        bge.logic.getCurrentScene().objects['Tetrahedron'].setVisible(True)        
        
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
        
        bge.logic.getCurrentScene().objects['Icosahedron'].setVisible(False)
        bge.logic.getCurrentScene().objects['Icosahedron Information'].setVisible(False)
        bge.logic.getCurrentScene().objects['Icosahedron Vertices'].setVisible(False)
        bge.logic.getCurrentScene().objects['Icosahedron Edges'].setVisible(False)
        bge.logic.getCurrentScene().objects['Icosahedron Faces'].setVisible(False)
        
        bge.logic.setAnimRecordFrame(0)
    
showTetrahedron()