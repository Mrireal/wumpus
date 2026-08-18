import pygame

ANCHO, ALTO = 900, 700
TAMAÑO_CELDA = 120
MARGEN = 30


def dibujar_celda(pantalla, rect, color, etiqueta=None, icono=None, borde=(30, 30, 30)):
    pygame.draw.rect(pantalla, borde, rect, 2)
    pygame.draw.rect(pantalla, color, rect.inflate(-8, -8))

    if etiqueta:
        font = pygame.font.SysFont("arial", 20, bold=True)
        texto = font.render(etiqueta, True, (255, 255, 255))
        pantalla.blit(texto, (rect.x + 12, rect.y + 10))

    if icono:
        font_icon = pygame.font.SysFont("arial", 40, bold=True)
        icono_txt = font_icon.render(icono, True, (255, 255, 255))
        icono_rect = icono_txt.get_rect(center=rect.center)
        pantalla.blit(icono_txt, icono_rect)


KEY_DIRECTIONS = {
    pygame.K_UP: "up",
    pygame.K_w: "up",
    pygame.K_DOWN: "down",
    pygame.K_s: "down",
    pygame.K_LEFT: "left",
    pygame.K_a: "left",
    pygame.K_RIGHT: "right",
    pygame.K_d: "right",
}


def dibujar_tablero(pantalla):
    tablero_x = 110
    tablero_y = 120
    board = [
        ["P", "", "", ""],
        ["", "", "", ""],
        ["", "", "", ""],
        ["", "", "", ""],
    ]

    for fila in range(4):
        for col in range(4):
            x = tablero_x + col * TAMAÑO_CELDA
            y = tablero_y + fila * TAMAÑO_CELDA
            rect = pygame.Rect(x, y, TAMAÑO_CELDA, TAMAÑO_CELDA)

            """if (fila, col) == (0, 0):
                dibujar_celda(pantalla, rect, (84, 180, 120), "Inicio", "🧭")
            elif (fila, col) == (1, 3):
                dibujar_celda(pantalla, rect, (104, 116, 143), "Pozo", "💀")
            elif (fila, col) == (2, 2):
                dibujar_celda(pantalla, rect, (120, 58, 58), "Wumpus", "👹")
            elif (fila, col) == (3, 1):
                dibujar_celda(pantalla, rect, (96, 92, 92), "Pozo", "🕳️")
            elif (fila, col) == (3, 3):
                dibujar_celda(pantalla, rect, (215, 180, 70), "Oro", "💰")
            else:
                dibujar_celda(pantalla, rect, (95, 130, 90), "")"""

    pygame.draw.rect(pantalla, (40, 40, 45), (90, 100, 500, 500), 3)


"""def dibujar_panel_izquierdo(pantalla):
    panel = pygame.Rect(30, 120, 220, 420)
    pygame.draw.rect(pantalla, (25, 30, 38), panel, border_radius=16)
    pygame.draw.rect(pantalla, (90, 110, 125), panel, 2, border_radius=16)

    title = pygame.font.SysFont("arial", 26, bold=True)
    pantalla.blit(title.render("Wumpus", True, (245, 245, 245)), (55, 145))

    info = [
        ("Jugador", "Aventurero"),
        ("Mapa", "4x4"),
        ("Estado", "Explorando"),
        ("Objetivo", "Recoger oro"),
    ]

    font = pygame.font.SysFont("arial", 18)
    for i, (label, value) in enumerate(info):
        y = 200 + i * 55
        pantalla.blit(font.render(label + ":", True, (185, 205, 220)), (55, y))
        pantalla.blit(font.render(value, True, (255, 255, 255)), (150, y))
"""


def dibujar_panel_derecho(pantalla):
    panel = pygame.Rect(650, 120, 200, 420)
    pygame.draw.rect(pantalla, (25, 30, 38), panel, border_radius=16)
    pygame.draw.rect(pantalla, (90, 110, 125), panel, 2, border_radius=16)

    title = pygame.font.SysFont("arial", 22, bold=True)
    pantalla.blit(title.render("Sensaciones", True, (245, 245, 245)), (685, 145))

    mensajes = [
        "Huele a peligro",
        "Hay viento",
        "Brilla el oro",
        "Todo en calma",
    ]

    font = pygame.font.SysFont("roman", 17)
    for i, texto in enumerate(mensajes):
        y = 195 + i * 55
        pygame.draw.rect(pantalla, (60, 72, 88), (675, y, 150, 36), border_radius=8)
        pantalla.blit(font.render(texto, True, (235, 235, 235)), (690, y + 9))


def dibujar_encabezado(pantalla):
    pygame.draw.rect(pantalla, (18, 23, 30), (0, 0, ANCHO, 90))
    title = pygame.font.SysFont("roman", 38, bold=True)
    subtitulo = pygame.font.SysFont("roman", 16)
    pantalla.blit(title.render("WUMPUS", True, (255, 220, 120)), (100, 25))
    pantalla.blit(
        subtitulo.render("vista de prototipo visual", True, (200, 210, 200)), (100, 68)
    )


def run_game():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Wumpus - Visual")
    reloj = pygame.time.Clock()

    ejecutando = True
    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    ejecutando = False

        pantalla.fill((24, 24, 24))
        dibujar_encabezado(pantalla)
        """dibujar_panel_izquierdo(pantalla)"""
        dibujar_tablero(pantalla)
        dibujar_panel_derecho(pantalla)
        pygame.display.flip()
        reloj.tick(30)

    pygame.quit()
