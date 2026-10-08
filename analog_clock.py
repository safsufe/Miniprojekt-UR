# Import libaries
import pygame
import datetime
import math

# Initialize Pygame
pygame.init()

# Load and resize clock image
clock_image = pygame.image.load("safsufe.png")
clock_image = pygame.transform.scale(clock_image,(420,420))

# Create window
screen=pygame.display.set_mode((600,600))

# Define clock center, markings and font variables
center = (300, 300)
start_line = 180
end_line = 160
angle_offset = 360 / 12
font = pygame.font.Font(None, 30)

# Main loop for continuously updating and displaying the clock
while True:

    # Handle window events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Draw background and clock image
    screen.fill((255,255,255))
    pygame.draw.circle(screen,(0,0,0),center,200,3)
    screen.blit(clock_image,(center[0]-210,center[1]-210))

    # Draw the 12 hour markings 
    for i in range(12):
            
            angle = i * angle_offset

            start_point = (center[0] + math.cos(math.radians(angle)) * start_line,
                                center[1] + math.sin(math.radians(angle)) * start_line)
            
            end_point = (center[0] + math.cos(math.radians(angle)) * end_line,
                            center[1] + math.sin(math.radians(angle)) * end_line)
            
            pygame.draw.line(screen,(250,250,250),start_point,end_point,5)

    # Draw numbers around the clock
    for number in range(1, 13):
     number_angle = (number * 30) - 90

     number_x = center[0] + math.cos(math.radians(number_angle)) * 140
     number_y = center[1] + math.sin(math.radians(number_angle)) * 140

     number_text = font.render(str(number), True, (255,255,255))
     number_rect = number_text.get_rect(center=(number_x, number_y))

     screen.blit(number_text, number_rect)
    
    # Get current time 
    current_time = datetime.datetime.now()

    # Calculate and draw second hand
    second = current_time.second

    second_angle_offset = 360/60
    second_angle = (second * second_angle_offset) - 90

    second_end_point = (center[0] + math.cos(math.radians(second_angle)) * end_line,
                    center[1] + math.sin(math.radians(second_angle)) * end_line)
    
    pygame.draw.line(screen,(250,250,250),center,second_end_point,1)

    # Calculate and draw minute hand
    minute = current_time.minute

    minute_angle_offset = 360 / 60
    minute_angle = (minute * minute_angle_offset) - 90
    minute_line = 150

    minute_end_point = (center[0] + math.cos(math.radians(minute_angle)) * minute_line,
                    center[1] + math.sin(math.radians(minute_angle)) * minute_line)
    
    pygame.draw.line(screen,(250,250,250),center,minute_end_point,3)

    # Calculate and draw hour hand
    hour = current_time.hour % 12

    hour_angle_offset = 360 / 12
    minute_adjustment = hour_angle_offset / 60

    hour_angle = (hour*hour_angle_offset) + (minute * minute_adjustment) - 90
    hour_line = 110

    hour_end_point = (center[0] + math.cos(math.radians(hour_angle)) * hour_line,
                    center[1] + math.sin(math.radians(hour_angle)) * hour_line)
    
    pygame.draw.line(screen,(250,250,250),center,hour_end_point,3)

    # Update display
    pygame.display.flip()