import bge

def showCube():
    
    # Encontrando e atribuindo o controlador lógico a variável 'cont'
    cont = bge.logic.getCurrentController()
    
    # Variavel que armazana um booleano se o botão mostrar cubo foi clicado ou não
    cubeButtonClicked = cont.sensors["Mouse Over Cube Button"].positive and cont.sensors["Left Button Cube Button"].positive
    
    # Verifica se o botão foi clicado e se o cubo já não está visível
    if cubeButtonClicked and bge.logic.getCurrentScene().objects['Cube'].visible ==  False:
        
        # Mostra o cubo e esconde todos os outros sólidos e suas informações              
        bge.logic.getCurrentScene().objects['Tetrahedron'].setVisible(False)
        bge.logic.getCurrentScene().objects['Tetrahedron Information'].setVisible(False)
        bge.logic.getCurrentScene().objects['Tetrahedron Vertices'].setVisible(False)
        bge.logic.getCurrentScene().objects['Tetrahedron Edges'].setVisible(False)
        bge.logic.getCurrentScene().objects['Tetrahedron Faces'].setVisible(False)
        
        bge.logic.getCurrentScene().objects['Cube'].setVisible(True)
        
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
    
showCube()