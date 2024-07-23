import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)
edges = (
    (0,1),
    (1,2),
    (2,3),
    (3,0),
    (4,5),
    (5,6),
    (6,7),
    (7,4),
    (0,4),
    (1,5),
    (2,6),
    (3,7)
)
faces = (
    (0,1,5,4),
    (1,2,6,5),
    (2,3,7,6),
    (3,0,4,7),
    (4,5,6,7),
    (0,1,2,3)
)
colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,1,0),
    (1,0,1),
    (0,1,1)
)
def draw_dice():
    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        glColor3fv(colors[i])
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()
    glColor3fv((0,0,0))
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)
    dice_faces = [1, 2, 3, 4, 5, 6]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    glRotatef(random.randint(0,360), 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_dice()
        pygame.display.flip()
        pygame.time.wait(10)
if __name__ == "__main__":
    main()
