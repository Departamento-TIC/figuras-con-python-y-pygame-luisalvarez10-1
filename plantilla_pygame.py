# Plantilla básica para gráficos estáticos con Pygame
# Basada en la estructura de programarcadegames.com

import pygame
import math

# --- Colores (R, G, B) ---
NEGRO   = (  0,   0,   0)
BLANCO  = (255, 255, 255)
ROJO    = (255,   0,   0)
VERDE   = (  0, 255,   0)
AZUL    = (  0,   0, 255)
AMARILLO= (255, 255,   0)
NARANJA = (255, 165,   0)

# --- Inicialización de Pygame ---
pygame.init()

# --- Tamaño de la ventana ---
ANCHO = 700
ALTO  = 500
pantalla = pygame.display.set_mode((ANCHO, ALTO))

# --- Título de la ventana ---
pygame.display.set_caption("Mis gráficos")

# --- Bucle principal ---
hecho = False
reloj = pygame.time.Clock()

while not hecho:

    # 1) Gestión de eventos (no modificar)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True

    # 2) Fondo de la pantalla
    pantalla.fill(BLANCO)

    # -------------------------------------------------------
    # 3) DIBUJA AQUÍ TUS FIGURAS
    # -------------------------------------------------------

    # Línea: pygame.draw.line(pantalla, color, [x1, y1], [x2, y2], grosor)
    # Rectángulo: pygame.draw.rect(pantalla, color, [x, y, ancho, alto], grosor)
    #   grosor=0 → relleno; grosor>0 → solo borde
    # Elipse / círculo: pygame.draw.ellipse(pantalla, color, [x, y, ancho, alto], grosor)
    # Polígono: pygame.draw.polygon(pantalla, color, [[x1,y1],[x2,y2],...], grosor)
    # Arco: pygame.draw.arc(pantalla, color, [x, y, ancho, alto], ang_inicio, ang_fin, grosor)
    #   ángulos en radianes; 0 = derecha, math.pi/2 = arriba
    

    pygame.draw.rect(pantalla, ROJO, [200, 150, 200, 200], 0)
    pygame.draw.rect(pantalla, BLANCO, [220, 170, 75, 75], 0)
    pygame.draw.rect(pantalla, NARANJA, [310, 200, 75, 150], 0)
    pygame.draw.line(pantalla, NEGRO, [310, 350], [350, 450], 2)
    pygame.draw.line(pantalla, NEGRO, [385, 350], [425, 450], 2)
    pygame.draw.line(pantalla, NEGRO, [100, 450], [600, 450], 2)
    pygame.draw.polygon(pantalla, VERDE, [[300, 20], [150, 150], [450, 150]], 0)

    

    # -------------------------------------------------------
    # 4) Actualizar pantalla (no modificar)
    # -------------------------------------------------------
    pygame.display.flip()
    reloj.tick(60)

# --- Salir de Pygame ---
pygame.quit()
