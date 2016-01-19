from PIL import Image
import random

#Generates the seed for a tree
def makeSeed(y):
    random.seed()
    seed_x = random.randint(10, 590)
    seed_y = y
    width = random.randint(5, 10)
    height = random.randint(width*5, width*30)

    return (seed_x, seed_y, width, height)

#Grows the vertical components
def growStems(seed_data, pixel_field):
    seed_x = seed_data[0]
    seed_y = seed_data[1]
    width = seed_data[2]
    height = seed_data[3]
    for x in range(seed_x, seed_x+width):
        for y in range(seed_y-height, seed_y):
            pixel_field[x][y] = (0, 0, 0)
            #Dithering
            if seed_y > 300 and seed_y < 320:
                if (x+y)%2==0:
                    pixel_field[x][y] = (255, 255, 255)
            elif seed_y >= 320 and seed_y < 340:
                if (x+y)%4==0:
                    pixel_field[x][y] = (255, 255, 255)
            elif seed_y >= 340 and seed_y < 360:
                if (x+y)%8==0:
                    pixel_field[x][y] = (255, 255, 255)

    return pixel_field

#Grows the horizontal components
def growBranches(seed_data, pixel_field):
    seed_x = seed_data[0]
    seed_y = seed_data[1]
    width = seed_data[2]
    height = seed_data[3]
    branch_height = seed_y-height
    branch_width = width
    branch_length = 2
    max_prev = branch_length
    branches = []
    while(branch_height >= seed_y-height and branch_height < seed_y-(3*width) and branch_length < height/3):
        branches.append((branch_height, branch_width, branch_length))
        branch_height+= 4
        branch_length+=2
        #Gives the conifer unevenness to make it look more organic
        if random.randint(0,110) > 100 and branch_length > max_prev:
            max_prev = branch_length
            branch_length -= branch_length/4
    max_length = height/3


    for x in range(seed_x-max_length, seed_x+max_length):
        for y in range(seed_y-height, seed_y):
            for branch in branches:
                bh = branch[0]
                bw = branch[1]
                bl = branch[2]
                #Establishing whether a point is "in" a branch
                if x >= seed_x-bl+(width/2) and x <= seed_x+bl+(width/2):
                    if x > 1 and x < 599:
                        if y >= bh-(bw/2) and y <= bh+(bw/2):
                            if y < 400 and y > 0:
                                pixel_field[x][y] = (0, 0, 0)
                                #Dithering
                                if seed_y > 300 and seed_y < 320:
                                    if (x+y)%2==0:
                                        pixel_field[x][y] = (255, 255, 255)
                                elif seed_y >= 320 and seed_y < 340:
                                    if (x+y)%4==0:
                                        pixel_field[x][y] = (255, 255, 255)
                                elif seed_y >= 340 and seed_y < 360:
                                    if (x+y)%8==0:
                                        pixel_field[x][y] = (255, 255, 255)

    return pixel_field


def growTrees(n):
    pixel_field = [[(255, 255, 255) for y in range(400)] for x in range(600)]
    #Create the ground
    for i in range(600):    
        for j in range(400):
            if pixel_field[i][j]==(255,255,255) and j > 300:
                if (i+j)%2 == 0:
                    pixel_field[i][j]=(0,0,0)
    seed_ys=[]
    #Generates seeds for the trees and orders them back to front to make the dithering work
    for t in range(n):
        seed_ys.append(random.randint(300,390))
    seed_ys.sort()

    for s in range(len(seed_ys)):
        seed= makeSeed(seed_ys[s])
        pixel_field = growStems(seed, pixel_field)
        pixel_field = growBranches(seed, pixel_field)
    return pixel_field

def makeForest():
    forest = growTrees(25)
    img = Image.new( 'RGB', (600,400), "white") # create a new black image
    pixels = img.load() # create the pixel map
    for i in range(img.size[0]):    # for every pixel:
        for j in range(img.size[1]):
            if pixels[i,j]==(255,255,255) and j > 300:
                if (i+j)%2 == 0:
                    pixels[i,j]=(0,0,0)
            pixels[i,j] = forest[i][j] # set the colour accordingly

    img.save("Forest25.jpg")

if __name__ == '__main__':
    makeForest()
