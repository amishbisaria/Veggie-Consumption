#imports
import pygame
import random
import numpy as np

#setup screen and window
pygame.init()
WIDTH, HEIGHT = 1280, 720
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Veggie Consumption")

#define images
broccoli = pygame.image.load("./Veggies/broccoli.png")
carrot = pygame.image.load("./Veggies/carrot.png")
lettuce = pygame.image.load("./Veggies/lettuce.png")
onion = pygame.image.load("./Veggies/onion.png")
tomato = pygame.image.load("./Veggies/tomato.png")

pygame.display.set_icon(carrot)
game_FPS = 60

def main():
    clock = pygame.time.Clock()
    veggies = [broccoli, carrot, lettuce, onion, tomato] #vegetable array
    steps = [10, 80, 150, 220, 290, 360, 430, 500, 570]
    board_width, board_height = 9, 9
    board_matrix = [[0 for x in range(board_width)] for y in range(board_height)]
    def starter_veggies():
        for x in range(0,9):
                for y in range(0,9):
                    choice = random.randint(0,4) #gets random number from 0 to 4
                    WINDOW.blit(veggies[choice],(steps[x],steps[y])) #shows veggies
                    board_matrix[y][x] = choice #prints matrix (flipped because y-axis is up & down so it determines the row)
                    
    


    #loop for game
    playing = True
    first = True
    while playing:
        clock.tick(game_FPS) #makes game runs at 60 fps (wont impact gameplay)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                playing = False
            if (event.type == pygame.MOUSEBUTTONUP):
                x, y = event.pos #get mouse position when mouse button released
                
                


        if first == True: #handles the game setup to start
            starter_veggies()
            print(np.array(board_matrix))
            first = False

        pygame.display.update()
        
    pygame.quit()




if __name__ == '__main__':
    main()