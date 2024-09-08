import pygame
import random
import math
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
shipX = 250
xAcceleration = 0
xSpeed = 0
pygame.init()
left = False
right = False
score = 0
difficulty = 1
waveX = 0
waveSpeed = 5
# Set the width and height of the screen [width, height]
size = (500, 700)
screen = pygame.display.set_mode(size)
background = pygame.image.load("background.png").convert()
shipSprite = pygame.image.load("ship.png.png").convert()
asteroidSprite = pygame.image.load("asteroidsprite.png").convert()
asteroidSprite.set_colorkey(BLACK)
pygame.display.set_caption("My Game")

def drawShip(X):
        screen.blit(shipSprite, [int(X - 25), 600])#pygame.draw.rect(screen, WHITE, [int(X - 25), 600, 50, 50], 5)
def drawBoulders(BOULDERS):
        for i in range(len(BOULDERS)):
                if BOULDERS[i] == 1:
                        screen.blit(asteroidSprite, [0, waveX-50])
                if BOULDERS[i] == 2:
                        screen.blit(asteroidSprite, [100, waveX-50])
                if BOULDERS[i] == 3:
                        screen.blit(asteroidSprite, [200, waveX-50])
                if BOULDERS[i] == 4:
                        screen.blit(asteroidSprite, [300, waveX-50])
                if BOULDERS[i] == 5:
                        screen.blit(asteroidSprite, [400, waveX-50])
       
def generateBoulders():
        boulders1 = [1, 2, 3, 4, 5]
        boulders2 = []
        boulder1 = False
        boulder2 = False
        boulder3 = False
        boulder4 = False
        boulder5 = False
        for i in range(difficulty):
                rng = random.randint(0, 4-i)
                boulder = boulders1[rng]
                del boulders1[rng]
                boulders2.append(boulder)
        return boulders2
def checkCollision(BOULDERS):
        for i in range(difficulty):
                if BOULDERS[i] == 1 and shipX > -20 and shipX < 120:
                        return True
                if BOULDERS[i] == 2 and shipX > 80 and shipX < 220:
                        return True
                if BOULDERS[i] == 3 and shipX > 180 and shipX < 320:
                        return True
                if BOULDERS[i] == 4 and shipX > 280 and shipX < 420:
                        return True
                if BOULDERS[i] == 5 and shipX > 380 and shipX < 520:
                        return True
                
                        
# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
countdown = 3
while countdown > 0:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
        screen.fill(BLACK)
        font = pygame.font.SysFont('Calibri', 50, True, False)
        text = font.render("Starting in: "+str(int(countdown+1)),True,WHITE)
        countdown -= .1
        screen.blit(text, [100, 350])
        pygame.display.flip()
        clock.tick(10)
newBoulders = generateBoulders()
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True

        if event.type == pygame.KEYUP:      
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False

    # --- Game logic should go here
    # --- SHIP MOVEMENT ------------------>
    xAcceleration = 0
    if left:
            xAcceleration -= 4
    if right:
            xAcceleration += 4
    xSpeed += xAcceleration
    xSpeed *= .7
    shipX += xSpeed
    if shipX <= 0:
            shipX += 500
    if shipX >= 500:
            shipX -= 500
    # --- END OF SHIP MOVEMENT
    # --- WAVE AND SCORE
    if waveX >= 700:
            waveX -= 700
            score += 1
            # --- DIFFICULTY
            if score <= 50:
                    waveSpeed = 10
            if score <= 40:
                    difficulty = 4
            if score <= 30:
                    difficulty = 3
            if score <= 20:
                    difficulty = 2
            if score <= 10:
                    difficulty = 1
            if difficulty == 1:
                    waveSpeed = 5
            elif difficulty == 2:
                    waveSpeed = 6
            elif difficulty == 3:
                    waveSpeed = 7
            elif difficulty == 4:
                    waveSpeed = 8
            # --- END OF DIFFICULTY
            newBoulders = generateBoulders()
    waveX += waveSpeed
    # --- END OF WAVE AND SCORE
    
    # --- DEATH COLLISION
    if waveX > 570 and waveX < 640:
            done = checkCollision(newBoulders)
    # --- END OF DEATH COLLISION
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.blit(background, [0,0])

    # --- Drawing code should go here
    drawShip(shipX)
    drawBoulders(newBoulders)

    scoreText = font.render("Score: " + str(score),True,WHITE)
    screen.blit(scoreText, [0,0])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    pygame.display.update()
    # --- Limit to 60 frames per second
    clock.tick(60)

done = False
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(BLACK)
    scoreText = font.render("Your Final Score Is: " + str(score),True,WHITE)
    screen.blit(scoreText, [20,350])
    pygame.display.flip()
    pygame.display.update()
    clock.tick(10)
# Close the window and quit.
pygame.quit()

