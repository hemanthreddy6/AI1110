import numpy as np
import pygame
import sys

pygame.init()

print("Software Implementation of Music Player")

# Creating the Interface
font=pygame.font.SysFont("Arial",30)
length=841
height=520
screen=pygame.display.set_mode((length,height))
pygame.display.set_caption("My Song Player")

# Setting volume at max
pygame.mixer.music.set_volume(1.0)

# Defining the button class
class button:
    def __init__(self,length,height,text,position):
        self.top_color="#F6E0B5"
        self.top_rect=pygame.Rect(position,(length,height))
        self.click=False
        self.text_surf=font.render(text,True,"#6D363E")
        self.text_rect=self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        pygame.draw.rect(screen,self.top_color,self.top_rect)
        screen.blit(self.text_surf,self.text_rect)
        return self.click_check()

    def click_check(self):
        mouse_position=pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_position):
            self.top_color="#FF7F50"
            if(pygame.mouse.get_pressed()[0]):
                self.click=True
                self.top_color="#F0F7DA"
            else:
                if self.click==True:
                    self.click=False
                    return True
        else:
            self.top_color="#F6E0B5"
            return False


# Creating the buttons
Pause=button(120,70,"Pause",(300,360))
Next=button(140,60,"Play Next",(450,360))
Resume=button(120,70,"Resume",(300,360))

# This denotes the state of music player
running =True
current_state="Play"

# Variables for storing songs data
totalCount=20
count=np.zeros(20)

while running:

    # Generating random number
    a=np.random.randint(1,21)

    if(count[a-1]==1):
        continue
    song_number=str(a)

    # Printing the song file name
    print(song_number+".mp3")

    # Marking it as played
    count[a-1]=1
    totalCount-=1

    Text=button(300,50,"Playing Now: "+song_number+".mp3",(250,50))

    # Loading the song and playing it
    pygame.mixer.music.load("songs/"+song_number+".mp3")
    pygame.mixer.music.play()

    screen.fill((53,70,87))
    Text.draw()
    
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                current_state="End"
                running=False
                print("Exiting the music player")
                sys.exit()

        # Playing next song if user clicks 'Next' or resume
        if (pygame.mixer.music.get_busy() and not current_state == "Play") or Next.draw():

            # Getting the song number to be played
            a=-1
            while running:
                if totalCount==0:
                    totalCount=20
                    count=np.zeros(20)
                a=np.random.randint(1,21)
                if(count[a-1]==1):
                    continue
                else:
                    break

            song_number=str(a)
            print(song_number+".mp3")

            # Marking it as played
            count[a-1]=1
            totalCount-=1

            Text=button(300,50,"Playing Now: "+song_number+".mp3",(250,50))

            # Loading the song and playing it
            pygame.mixer.music.load("songs/"+song_number+".mp3")
            pygame.mixer.music.play()


            screen.fill((53,70,87))
            Text.draw()
            Next.draw()

        # Pausing the song
        if current_state=="Play":
            if Pause.draw():
                current_state="Pause"
                pygame.mixer.music.pause()
        # Resuming the song
        else:
            if Resume.draw():
                current_state="Play"
                pygame.mixer.music.unpause()

        pygame.display.update()