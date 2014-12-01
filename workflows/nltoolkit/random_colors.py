
def get_new_color(colors):
    """
    function takes list of colors and it calculates new color, which is similar to others.

    :param colors: list of colors that are used as basis for calculating similarity.
    :return: color in a tuple, that has 3 values for RGB. Example: (200, 100, 200)
    """
    import random
    import math
    max_distance = 0

    for t in range(100):
        min_distance = 1000
        # randomly creates new color (R, G, B)
        new_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        for color in colors:  # for each color calculate distances
            distance = math.sqrt((color[0] - new_color[0])**2 +
                                 (color[1] - new_color[1])**2 +
                                 (color[2] - new_color[2])**2)

            if distance < min_distance:
                min_distance = distance

        if min_distance > max_distance:
            max_distance = min_distance
            similar_color = new_color  # new color is the one with the minimal distance from others
    return similar_color


def get_colors(n):
    """
    function randomly creates n colors that are similar
    :param n: number of colors
    :return: list of html color codes
    """

    colors = [(0, 0, 0), (255, 255, 255)]  # init black, white
    for i in range(n):
        colors.append(get_new_color(colors))

    #create html color codes without init colors
    return ["#%02x%02x%02x" % color for color in colors[2:]]
