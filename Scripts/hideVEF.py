import bge

def hideVEF():
    
    # Armazena e verifica se o frame atual da animação e diferente de 0
    currentFrame = bge.logic.getAnimRecordFrame()    
    if(currentFrame != 0):
        
        # Se o frame for diferente do inicial esconde todas as informações, vertices, arestas e faces de todos poliedros
        bge.logic.getCurrentScene().objects['Tetrahedron Information'].setVisible(False)
        bge.logic.getCurrentScene().objects['Tetrahedron Vertices'].setVisible(False)
        bge.logic.getCurrentScene().objects['Tetrahedron Edges'].setVisible(False)
        bge.logic.getCurrentScene().objects['Tetrahedron Faces'].setVisible(False)
        
        bge.logic.getCurrentScene().objects['Cube Information'].setVisible(False)
        bge.logic.getCurrentScene().objects['Cube Vertices'].setVisible(False)
        bge.logic.getCurrentScene().objects['Cube Edges'].setVisible(False)
        bge.logic.getCurrentScene().objects['Cube Faces'].setVisible(False)
        
        bge.logic.getCurrentScene().objects['Octahedron Information'].setVisible(False)
        bge.logic.getCurrentScene().objects['Octahedron Vertices'].setVisible(False)
        bge.logic.getCurrentScene().objects['Octahedron Edges'].setVisible(False)
        bge.logic.getCurrentScene().objects['Octahedron Faces'].setVisible(False)
        
        bge.logic.getCurrentScene().objects['Dodecahedron Information'].setVisible(False)
        bge.logic.getCurrentScene().objects['Dodecahedron Vertices'].setVisible(False)
        bge.logic.getCurrentScene().objects['Dodecahedron Edges'].setVisible(False)
        bge.logic.getCurrentScene().objects['Dodecahedron Faces'].setVisible(False)
        
        bge.logic.getCurrentScene().objects['Icosahedron Information'].setVisible(False)
        bge.logic.getCurrentScene().objects['Icosahedron Vertices'].setVisible(False)
        bge.logic.getCurrentScene().objects['Icosahedron Edges'].setVisible(False)
        bge.logic.getCurrentScene().objects['Icosahedron Faces'].setVisible(False)

hideVEF()