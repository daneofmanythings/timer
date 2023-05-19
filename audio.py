import pygame


# class TimerMixer(pygame.mixer):
#     def __init__(self):
#         super().__init__()
#
#     def play_beep(self):
#         pass


def beep():
    pygame.mixer.init()
    pygame.mixer.music.load('./sounds/beep.wav')
    pygame.mixer.music.play(1)
