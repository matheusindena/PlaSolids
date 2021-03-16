import bge

def animationOctahedron():
    
    # Encontrando e atribuindo o controlador lógico a variável 'cont'
    cont = bge.logic.getCurrentController()
    
    # Verifica se o octahedron esta visivel
    if bge.logic.getCurrentScene().objects['Octahedron'].visible:
    
        # Verifica se o sensor da roda do mouse para cima foi ativado e se a animação não se encontra em seu limite inferior  
        if cont.sensors["Scroll Up"].positive and bge.logic.getAnimRecordFrame() > 0:
        
            # Verifica em qual frame a animacao se encontra
            currentFrame = bge.logic.getAnimRecordFrame()
        
            # Encontrando e atribuindo o atuador responsável pela animacao a variavel 'act'
            act = cont.actuators["Octahedron Action"]
        
            # Designa qual ação será executada
            act.action = "Octahedron Animation"
        
            # A ação inicia no frame atual
            act.frameStart = currentFrame
        
            # A ação termina dois frame a trás
            act.frameEnd = currentFrame - 1
        
            # Ativa a ação 
            cont.activate(act)
        
            # Define o frame em que o programa se encontra       
            bge.logic.setAnimRecordFrame(currentFrame - 1)
    
        # Verifica se o sensor da roda do mouse para baixo foi ativado e se a animação não se encontra em seu limite superior
        if cont.sensors["Scroll Down"].positive and bge.logic.getAnimRecordFrame() < 25:
        
            # Verifica em qual frame a animacao se encontra
            currentFrame = bge.logic.getAnimRecordFrame()
        
            # Encontrando e atribuindo o atuador responsável pela animacao a variavel 'act'
            act = cont.actuators["Octahedron Action"]
        
            # Designa qual ação será executada
            act.action = "Octahedron Animation"
        
            # A ação inicia no frame atual
            act.frameStart = currentFrame
        
            # A ação termina dois frame a frente
            act.frameEnd = currentFrame + 1
        
            # Ativa a ação 
            cont.activate(act)
        
            # Define o frame em que o programa se encontra       
            bge.logic.setAnimRecordFrame(currentFrame + 1)
        
animationOctahedron()