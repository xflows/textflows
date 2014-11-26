
def get_new_color(colors):
    import random
    import math
    max_distance = 0
    similar_color = (0, 0, 0)  # init black color

    for t in range(100):
        min_distance = 1000
        new_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        for color in colors:
            distance = math.sqrt((color[0] - new_color[0])**2 +
                                 (color[1] - new_color[1])**2 +
                                 (color[2] - new_color[2])**2)

            if distance < min_distance:
                min_distance = distance

        if min_distance > max_distance:
            max_distance = min_distance
            similar_color = new_color
    return similar_color


def get_colors(n):
    colors = [(0, 0, 0), (255, 255, 255)]  # black, white
    for i in range(n):
        colors.append(get_new_color(colors))
    return ["#%02x%02x%02x" % color for color in colors[2:]]
