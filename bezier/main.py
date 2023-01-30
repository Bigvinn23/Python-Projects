import pygame
import bezier_visualization

from sys import exit

def plot_point(line):
        current_x = line[0][0] + int(-(line[0][0] - line[1][0]) * (frame_count / reset_frame))
        current_y = line[0][1] + int(-(line[0][1] - line[1][1]) * (frame_count / reset_frame))
        pygame.draw.circle(screen, "black", (current_x, current_y), 2)

def get_point(line, percent):
    current_x = line[0][0] + int(-(line[0][0] - line[1][0]) * percent)
    current_y = line[0][1] + int(-(line[0][1] - line[1][1]) * percent)
    return (current_x, current_y)

def bezier(points, bezier_progress):
    sub_points = []

    if len(points) >= 2:
        for i in range(len(points)-1):
            sub_points.append(get_point((points[i], points[i+1]), bezier_progress))
            pygame.draw.line(screen, "black", points[i], points[i+1])
            pygame.draw.circle(screen, "black", sub_points[-1], 3)

        return bezier(sub_points, bezier_progress)
    
    else:
        return points[0]

pygame.init()

screen = pygame.display.set_mode((1000, 600))

pygame.display.set_caption("Bezier Visualization")

clock = pygame.time.Clock()

screen.fill('grey')

line_color = "#404040"

points = []
lines = []
plotted_points = []
frame_count = 0
reset_frame = 1000
bezier_plots = []

# Event Loop
while True:
    screen.fill("grey")
    
    if frame_count == 0:
        bezier_plots = []

    frame_count += 1
    frame_count = frame_count % reset_frame

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            points.append(event.pos)
            if len(points) >= 2:
                lines.append((points[-2], points[-1]))


    # draw the points
    for point in points:
        pygame.draw.circle(screen, "black", point, 3, 1)

    # draw the lines
    for line in lines:
        pygame.draw.line(screen, line_color, line[0], line[1], 1)

        #plot_point(line)

    if len(points) >= 2:
        bezier_plots.append(bezier(points, frame_count / reset_frame))

    # draw the plotted points
    for point in bezier_plots:
        pygame.draw.circle(screen, "red", point, 2)
        

    pygame.display.update()
    clock.tick(240)

    