import pygame
from constants import *

class Post:
    def __init__(self, username, location, description):
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = 0
        self.comments = []
        self.font = pygame.font.Font(None, 24)

    def display(self, screen):
        screen.fill((255, 255, 255))

        username_text = self.font.render(self.username, True, WHITE)
        screen.blit(username_text, (POST_USERNAME_X, POST_USERNAME_Y))

        location_text = self.font.render(self.location, True, WHITE)



