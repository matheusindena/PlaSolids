import bge

def showDodecahedron():
    
    # Encontrando e atribuindo o controlador lógico a variável 'cont'
    cont = bge.logic.getCurrentController()
    
    # Variavel que armazana um booleano se o botão mostrar dodecaedro foi clicado ou não
    dodecahedronButtonClicked = cont.sensors["Mouse Over Dodecahedron Button"].positive and cont.sensors["Left Button Dodecahedron Button"].positive
    
    # Verifica se o botão foi clicado e se o dodecaedro já não está visível
    if dodecahedronButtonClicked and bge.logic.getCurrentScene().objects['Dodecahedron'].visible ==  False:
        
        # Mostra o dodecaedro e esconde todos os outros sólidos                
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
        
        bge.logic.getCurrentScene().objects['Dodecahedron'].setVisible(True)
        
        bge.logic.getCurrentScene().objects['Icosahedron'].setVisible(False)
        bge.logic.getCurrentScene().objects['Icosahedron Information'].setVisible(False)
        bge.logic.getCurrentScene().objects['Icosahedron Vertices'].setVisible(False)
        bge.logic.getCurrentScene().objects['Icosahedron Edges'].setVisible(False)
        bge.logic.getCurrentScene().objects['Icosahedron Faces'].setVisible(False)
        
        bge.logic.setAnimRecordFrame(0)
    
showDodecahedron()