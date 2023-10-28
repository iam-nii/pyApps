import colorgram

rgb_colors = []

colors = colorgram.extract('my_image.jpg', 50)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

mylist = [(237, 231, 234), (221, 232, 225), (208, 160, 82), (55, 89, 132), (145, 91, 40), (139, 26, 48), (222, 207, 105), (132, 176, 203)]

print(rgb_colors)
