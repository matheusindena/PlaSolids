import bge

# Função para esconder os botões de vértices, arestas e faces

def showInformation():
    
    # Encontrando e atribuindo o controlador lógico a variável 'cont'
    cont = bge.logic.getCurrentController()
    
    # Variavel que armazana um booleano se o botão de informaçao foi clicado ou não
    infoButtonClicked = cont.sensors["Mouse Over Information"].positive and cont.sensors["Left Button Information"].positive
    
    currentFrame = bge.logic.getAnimRecordFrame()
    
    ############################### Tetraedro ###############################
        
    # Visibilidade do tetraedro
    tetraedro = bge.logic.getCurrentScene().objects['Tetrahedron']
    tetraedroVisibility = tetraedro.visible
    
    # Visibilidade das informações do tetraedro
    tetraedroInfo = bge.logic.getCurrentScene().objects['Tetrahedron Information']
    tetraedroInfoVisibility = tetraedroInfo.visible

    # Verifica se o tetraedro está visível, se o botão de informaçoes foi clicado e se o frame atual e o primeiro
    if tetraedroVisibility and infoButtonClicked and currentFrame == 0:
    
        # Se as informacoes estiverem aparecendo, as esconde
        if tetraedroInfoVisibility:
            tetraedroInfo.setVisible(False)
            bge.logic.getCurrentScene().objects['Tetrahedron Vertices'].setVisible(False)
            bge.logic.getCurrentScene().objects['Tetrahedron Edges'].setVisible(False)
            bge.logic.getCurrentScene().objects['Tetrahedron Faces'].setVisible(False)
            
        # Mas se não estiverem aparecendo, as mostra
        elif tetraedroInfoVisibility == False:
            tetraedroInfo.setVisible(True)
            bge.logic.getCurrentScene().objects['Tetrahedron Vertices'].setVisible(True)
            bge.logic.getCurrentScene().objects['Tetrahedron Edges'].setVisible(True)
            bge.logic.getCurrentScene().objects['Tetrahedron Faces'].setVisible(True)
    
    ################################# Cubo #################################
    
    # Visibilidade do cubo
    cube = bge.logic.getCurrentScene().objects['Cube']
    cubeVisibility = cube.visible
    
    # Visibilidade das informações do cubo
    cubeInfo = bge.logic.getCurrentScene().objects['Cube Information']
    cubeInfoVisibility = cubeInfo.visible

    # Verifica se o cubo está visível, se o botão de informaçoes foi clicado e se o frame atual e o primeiro
    if cubeVisibility and infoButtonClicked and currentFrame == 0:
    
        # Se as informacoes estiverem aparecendo, as esconde
        if cubeInfoVisibility == True:
            print("aqui")
            cubeInfo.setVisible(False)
            bge.logic.getCurrentScene().objects['Cube Vertices'].setVisible(False)
            bge.logic.getCurrentScene().objects['Cube Edges'].setVisible(False)
            bge.logic.getCurrentScene().objects['Cube Faces'].setVisible(False)
            
        # Mas se não estiverem aparecendo, as mostra
        else:
            cubeInfo.setVisible(True)            
            bge.logic.getCurrentScene().objects['Cube Vertices'].setVisible(True)
            bge.logic.getCurrentScene().objects['Cube Edges'].setVisible(True)
            bge.logic.getCurrentScene().objects['Cube Faces'].setVisible(True)
        
    ################################ Octaedro ################################
    
    # Visibilidade do octaedro
    octaedro = bge.logic.getCurrentScene().objects['Octahedron']
    octaedroVisibility = octaedro.visible
    
    # Visibilidade das informações do octaedro
    octaedroInfo = bge.logic.getCurrentScene().objects['Octahedron Information']
    octaedroInfoVisibility = octaedroInfo.visible

    # Verifica se o octaedro está visível, se o botão de informaçoes foi clicado e se o frame atual e o primeiro
    if octaedroVisibility and infoButtonClicked and currentFrame == 0:
    
        # Se as informacoes estiverem aparecendo, as esconde
        if octaedroInfoVisibility == True:
            octaedroInfo.setVisible(False)
            bge.logic.getCurrentScene().objects['Octahedron Vertices'].setVisible(False)
            bge.logic.getCurrentScene().objects['Octahedron Edges'].setVisible(False)
            bge.logic.getCurrentScene().objects['Octahedron Faces'].setVisible(False)
            
        # Mas se não estiverem aparecendo, as mostra
        else:
            octaedroInfo.setVisible(True)            
            bge.logic.getCurrentScene().objects['Octahedron Vertices'].setVisible(True)
            bge.logic.getCurrentScene().objects['Octahedron Edges'].setVisible(True)
            bge.logic.getCurrentScene().objects['Octahedron Faces'].setVisible(True)
        
    ############################### Dodecaedro ###############################
    
    # Visibilidade do dodecaedro
    dodecaedro = bge.logic.getCurrentScene().objects['Dodecahedron']
    dodecaedroVisibility = dodecaedro.visible
    
    # Visibilidade das informações do dodecaedro
    dodecaedroInfo = bge.logic.getCurrentScene().objects['Dodecahedron Information']
    dodecaedroInfoVisibility = dodecaedroInfo.visible

    # Verifica se o dodecaedro está visível, se o botão de informaçoes foi clicado e se o frame atual e o primeiro
    if dodecaedroVisibility and infoButtonClicked and currentFrame == 0:
    
        # Se as informacoes estiverem aparecendo, as esconde
        if dodecaedroInfoVisibility == True:
            dodecaedroInfo.setVisible(False)
            bge.logic.getCurrentScene().objects['Dodecahedron Vertices'].setVisible(False)
            bge.logic.getCurrentScene().objects['Dodecahedron Edges'].setVisible(False)
            bge.logic.getCurrentScene().objects['Dodecahedron Faces'].setVisible(False)
            
        # Mas se não estiverem aparecendo, as mostra
        else:
            dodecaedroInfo.setVisible(True)
            bge.logic.getCurrentScene().objects['Dodecahedron Vertices'].setVisible(True)
            bge.logic.getCurrentScene().objects['Dodecahedron Edges'].setVisible(True)
            bge.logic.getCurrentScene().objects['Dodecahedron Faces'].setVisible(True)
        
    ################################ Icosaedro ################################
    
    # Visibilidade do icosaedro
    icosaedro = bge.logic.getCurrentScene().objects['Icosahedron']
    icosaedroVisibility = icosaedro.visible
    
    # Visibilidade das informações do icosaedro
    icosaedroInfo = bge.logic.getCurrentScene().objects['Icosahedron Information']
    icosaedroInfoVisibility = icosaedroInfo.visible

    # Verifica se o icosaedro está visível, se o botão de informaçoes foi clicado e se o frame atual e o primeiro
    if icosaedroVisibility and infoButtonClicked and currentFrame == 0:
    
        # Se as informacoes estiverem aparecendo, as esconde
        if icosaedroInfoVisibility == True:
            icosaedroInfo.setVisible(False)
            bge.logic.getCurrentScene().objects['Icosahedron Vertices'].setVisible(False)
            bge.logic.getCurrentScene().objects['Icosahedron Edges'].setVisible(False)
            bge.logic.getCurrentScene().objects['Icosahedron Faces'].setVisible(False)
            
        # Mas se não estiverem aparecendo, as mostra
        else:
            icosaedroInfo.setVisible(True)
            bge.logic.getCurrentScene().objects['Icosahedron Vertices'].setVisible(True)
            bge.logic.getCurrentScene().objects['Icosahedron Edges'].setVisible(True)
            bge.logic.getCurrentScene().objects['Icosahedron Faces'].setVisible(True)
        
showInformation()