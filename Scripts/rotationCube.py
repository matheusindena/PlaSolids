import bge
    
def rotationCube():
    
    # Verifica se o objeto está visivel para prosseguir
    if bge.logic.getCurrentScene().objects['Cube'].visible:
        
        # Atribuindo o objeto que contêm o bloco lógico do controlador a variável 'owner'
        owner = bge.logic.getCurrentController().owner
                            
        # Encontrando e atribuindo o teclado lógico
        keyboard = bge.logic.keyboard
    
        # Sensor tecla W
        wKey = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.WKEY]
    
        # Sensor tecla S
        sKey = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.SKEY]
    
        # Sensor tecla A
        aKey = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.AKEY]
    
        # Sensor tecla D
        dKey = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.DKEY]
    
        # Se tecla W for pressionada
        if wKey:
            owner.applyRotation([0.02, 0.0, 0.0])
        
        # Se tecla S for pressionada
        if sKey:
            owner.applyRotation([-0.02, 0.0, 0.0])
        
        # Se tecla A for pressionada
        if aKey:
            owner.applyRotation([0.0, 0.0, -0.02])
        
        # Se tecla D for pressionada
        if dKey:
            owner.applyRotation([0.0, 0.0, 0.02])
    
rotationCube()