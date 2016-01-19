import turtle
def tree(f_length, spray=90., branches=2, f_scale=0.5, f_scale_friction=1.4, min_length=10):
    """
    Draws a tree with 2 branches using recursion
    """
    step = float(spray / (branches - 1))
    f_scale /= f_scale_friction
    turtle.forward(f_length)
    if f_length > min_length:
        turtle.left(spray / 2)
        tree(f_scale * f_length, spray, branches, f_scale, f_scale_friction, min_length)
        for counter in range(branches - 1):
            turtle.right(step)
            tree(f_scale * f_length, spray, branches, f_scale, f_scale_friction, min_length)
        turtle.left(spray / 2)
    turtle.back(f_length)

turtle.left(90)
tree(80, spray=120, branches=4)
turtle.exitonclick()