'''import colorgram

colors = colorgram.extract('python_art.jpg', 40)
rgb_colors=[]
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color=(r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)
'''
import random
import turtle as T
T.colormode(255)
tim= T.Turtle()
color_list=[(249, 248, 244), (57, 7, 2), (150, 89, 24), (68, 6, 32), (65, 92, 154), (90, 117, 189), (14, 14, 48), (143, 18, 9), (190, 147, 201), (9, 16, 12), (129, 142, 208), (220, 162, 227), (211, 166, 96), (122, 69, 130), (109, 25, 73), (241, 230, 238), (199, 128, 23), (88, 81, 16), (244, 248, 245), (174, 170, 236), (240, 199, 91), (44, 52, 113), (160, 98, 174), (234, 235, 246), (77, 91, 84), (199, 91, 71), (213, 182, 175), (53, 70, 62), (138, 150, 143), (116, 137, 115), (49, 70, 74), (113, 132, 138), (189, 194, 187), (185, 195, 196)]

tim.speed(0)
tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(300)
tim.setheading(0)
num_of_dots=100
for dotcount in range(1,num_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.penup()
    tim.forward(50)
    if dotcount%10==0:
        tim.setheading(90)
        tim.penup()
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

T.exitonclick()