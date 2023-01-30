import pygame

def get_point(line, percent):
    current_x = line[0][0] + int(-(line[0][0] - line[1][0]) * percent)
    current_y = line[0][1] + int(-(line[0][1] - line[1][1]) * percent)
    return (current_x, current_y)

def bezier(surface, points, bezier_progress):
    sub_points = []

    if len(points) >= 2:
        for i in range(len(points)-1):
            sub_points.append(get_point((points[i], points[i+1]), bezier_progress))
            pygame.draw.line(surface, "black", points[i], points[i+1])
            pygame.draw.circle(surface, "black", sub_points[-1], 3)

        return bezier(sub_points, bezier_progress)
    
    elif len(points) == 1:
        return points[0]
    
    else:
        return