import bge

def cameraMovement():
    
    # Atribuindo o objeto que contêm o bloco lógico do controlador a variável 'owner'
    owner = bge.logic.getCurrentController().owner
    
    # Encontrando e atribuindo o teclado lógico
    keyboard = bge.logic.keyboard
    
    # Sensor tecla seta para cima
    upKey = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.UPARROWKEY]
    
    # Sensor tecla seta para baixo
    downKey = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.DOWNARROWKEY]
    
    # Sensor tecla seta para esquerda
    leftKey = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.LEFTARROWKEY]
    
    # Sensor tecla seta para direita
    rightKey = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.RIGHTARROWKEY]
    
    # Sensor tecla seta E
    eKey = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.EKEY]
    
    # Sensor tecla seta Q 
    qKey = bge.logic.KX_INPUT_ACTIVE == keyboard.events[bge.events.QKEY]
    
    # Se tecla seta para cima for pressionada, mover camera para cima
    if upKey:
        owner.applyMovement((0, 0.02, 0), True)
        
    # Se tecla seta para baixo for pressionada, mover camera para baixo
    if downKey:
        owner.applyMovement((0, -0.02, 0), True)
       
    # Se tecla seta para esquerda for pressionada, mover camera para esquerda 
    if leftKey:
        owner.applyMovement((-0.02, 0, 0), True)
        
    # Se tecla seta para direita for pressionada, mover camera para direita
    if rightKey:
        owner.applyMovement((0.02, 0, 0), True)
        
    # Se tecla seta para direita for pressionada, mover camera para frente
    if eKey:
        owner.applyMovement((0, 0, -0.05), True)
        
        # Se tecla seta para direita for pressionada, mover camera para trás
    if qKey:
        owner.applyMovement((0, 0, 0.05), True)
    
cameraMovement()