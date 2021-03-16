import bge

def showOctahedron():
    
    # Encontrando e atribuindo o controlador lógico a variável 'cont'
    cont = bge.logic.getCurrentController()
    
    # Variavel que armazana um booleano se o botão mostrar octaedro foi clicado ou não
    octahedronButtonClicked = cont.sensors["Mouse Over Octahedron Button"].positive and cont.sensors["Left Button Octahedron Button"].positive
    
    # Verifica se o botão foi clicado e se o octaedro já não está visível
    if octahedronButtonClicked and bge.logic.getCurrentScene().objects['Octahedron'].visible ==  False:
        
        # Mostra o octaedro e esconde todos os outros sólidos                
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
        
        bge.logic.getCurrentScene().objects['Octahedron'].setVisible(True)
        
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
    
showOctahedron()