from canvas import Canvas
from shapes import Rectangle, Square

# canvas = Canvas(height=20, width=30, color=(255, 255, 255))
# r1 = Rectangle(x=2, y=4, height=8, width=10, color=(100, 0, 0))
# r1.draw(canvas)
#
# s1 = Square(x=5, y=7, side=4, color=(200, 200, 0))
# s1.draw(canvas)
# canvas.make('canvas.png')

canvas_height = int(input("Enter canvas height: "))
canvas_width = int(input("Enter canvas width: "))

colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color (white or black): ")

canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    shape_type = input("What kind of shape would u like to draw? Enter quit to quit. ")

    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_width = int(input("Enter the width fo the rectangle: "))
        rec_height = int(input("Enter the height fo the rectangle: "))
        red = int(input("How much red should the rectangle have? "))
        green = int(input("How much green? "))
        blue = int(input("How much blue? "))

        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red, green, blue))
        r1.draw(canvas)

    if shape_type.lower() == "square":
        square_x = int(input("Enter x of the square: "))
        square_y = int(input("Enter y of the square: "))
        square_side = int(input("Enter the side for the square: "))
        red = int(input("How much red should the square have? "))
        green = int(input("How much green? "))
        blue = int(input("How much blue? "))

        s1 = Square(x=square_x, y=square_y, side=square_side, color=(red, green, blue))
        s1.draw(canvas)

    if shape_type.lower() == "quit":
        break

canvas.make('canvas.png')