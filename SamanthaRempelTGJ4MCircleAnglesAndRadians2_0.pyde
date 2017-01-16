from processing import *
from math import sin
from fractions import Fraction


pic = loadImage("Pi-symbol.png")
angles = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360]

def setup():
    '''
    This creates the screen size
    '''
    size(750,525)
    
    
  
def angle(angleList, ADT):
    '''
    ADT: The rounded version of the angle to mouse is currently at
    angleList: The list of relevant angles that can be snapped to within the mouses quadrant
    return: The closest angle to the mouse's position
    '''
    diffs = []
    if ADT in angleList: #Checks to make sure that the angle isn't already a snap angle
        newAngle = ADT
    else:
        for i in angleList: #Goes through the relevant angles
            diff = abs(i - ADT) #Takes the absolute value of the difference because we don't care which direction we are snapping in
            diffs.append(diff)
        indx = diffs.index(min(diffs)) #Finds the index of the smallest difference, which becomes the index of the closest snap angle
        newAngle = angleList[indx]
    return newAngle
    

def draw():
    '''
    This function takes care of the actual drawing process and calculating angle values
    '''

    background(255) #Sets the background colour
    fill(0)
    ellipse(200, 250, 350, 350) #Draws the circle

    global X, Y, angles #Allows these variable to be used in this function

    text("Circle Trainer", 50, 50)
    text("by Samantha Rempel", 50, 50)

    '''
    Loading & Displaying
    image()
    imageMode()
    loadImage()
    noTint()
    requestImage()
    tint()
    '''
    #Image
    
    image(pic, 10, 10, 50, 50)

    delay = 1 #How long it takes the line to respond to mouse motion, higher the delay the slower the line moves 
    
    X += (mouseX - X)/delay #Changes the x-coord as the mouse moves
    Y += (mouseY - Y)/ delay #changes the y-coord as the mouse moves
    
    if mouseY != 250 and mouseX != 200 :
        #Calcualting angle based on mouse coords, as long as the mouse isn't at a zero point
        a = abs(mouseX - 200) # Change in x coords
        b = abs(mouseY - 250) # Change in y coords
        c = sqrt(a**2 + b**2) # The overall difference between the two points
        
        if c != 0: #Making sure that there is an angle to be found
            angleRadian = acos((c**2 + a**2 - b**2)/(2*a*c)) #Finding the angle in radians
            angleDegree = degrees(angleRadian) #Converting the angle to degrees
            angleDegreeTen = int(round(angleDegree)) #Getting rid of the decimal points
            
            #Getting the nearest 5 or 10 of each angle
            if str(angleDegreeTen)[-1] == '5':
                angleDegreeTen = angleDegreeTen    
            else:
                angleDegreeTen = int(round(float(angleDegree/10))) * 10 #Rounds the angle to the nearest ten value
                
            '''
            So that the function only gets the angles that are necessary to compare
            '''
            #Quadrant One
            if mouseX > 200 and mouseY < 250:
                angleList = angles[0:5] #Only passes up the necessary angles from the angle list
            #Quadrant Two
            elif mouseX < 200 and mouseY < 250:
                angleDegreeTen = 180 - angleDegreeTen
                angleList = angles[4:9] #Only passes up the necessary angles from the angle list
            #Quadrant Three
            elif mouseX < 200 and mouseY > 250:
                angleDegreeTen += 180
                angleList = angles[8:13] #Only passes up the necessary angles from the angle list
            #Quadrant Four
            elif mouseX > 200 and mouseY > 250:
                angleDegreeTen = 360 - angleDegreeTen
                angleList = angles[12:] #Only passes up the necessary angles from the angle list
                
            newAngle = angle(angleList, angleDegreeTen) #Passes the list of angles that are in the same quadrant as the mouse and the rounded angle and returns the snapped angle
            angleRadianTen = radians(newAngle) #Gets the radian value of the new snapped angle
            
            '''Finding x and y values if the hypotenuse was 200 pixels'''
            c2 = 200
            a2 = abs(cos(angleRadianTen) * c2) #Has to be abs because the calculations are automatically done for Quadrant One
            b2 = sqrt(c2**2 - a2**2)
            
            '''
            Fixing the x and y values to match the quadrant that the mouse is in
            '''
            #Quadrant One
            if mouseX > 200 and mouseY < 250:
                realX = a2 + 200 #Increases a because the x value is on the 'positive' side
                realY = 250 - b2 #Decreases b because the y value is on the 'negative' side
            #Quadrant Two
            elif mouseX < 200 and mouseY < 250:
                realX = 200 - a2 #Decreases a because the x value is on the 'negative' side
                realY = 250 - b2 #Decreases b because the y value is on the 'negative' side
            #Quadrant Three
            elif mouseX < 200 and mouseY > 250:
                realX = 200 - a2 #Decreases a because the x value is on the 'negative' side
                realY = b2 + 250 #Increases b because the y value is on the 'positive' side
            #Quadrant Four
            elif mouseX > 200 and mouseY > 250:
                realX = a2 + 200 #Increases a because the x value is on the 'positive' side
                realY = b2 + 250 #Increases b because the y value is on the 'positive' side
        
        line(200, 250, realX, realY) #Draws the line with the shortened line length
        textSize(50) #Makes the text larger
        
        '''Fixes formatting so that things are centred'''
        if len(str(newAngle)) == 1: 
            text(str(newAngle) + '°', 600, 200) #Prints the snapped to angle value
        elif len(str(newAngle)) == 2:
            text(str(newAngle) + '°', 595, 200) #Prints the snapped to angle value
        elif len(str(newAngle)) == 3:
            text(str(newAngle) + '°', 585, 200) #Prints the snapped to angle value
        
        text('or', 500, 250)
        
        numberValueRadians = str(round(angleRadianTen, 2)) 

        whole = [0, 360, 180] #List of angles with whole radian values
        if newAngle not in whole:
            decimal = float((PI/angleRadianTen)) #Finds the decimal value of the radian value
            frat = str(Fraction.from_float(decimal)) #Converts the decimal value to a fraction, some are awful fractions
            frat = frat.split("/") #Splits the fraction into the numerator and denominator
            
            #All fractions need to be the inverse
            if len(frat) == 1:
                #If the length is one then its a whole number so the top value should be one
                top = 1
                bottom = frat[0]
            elif newAngle > 120: #All angles above 120, aka with a fraction with a number other than 1 on top, glitches, so it has to be hard coded
                if newAngle == 135:
                    top = 3
                    bottom = 4
                elif newAngle == 150:
                    top = 5
                    bottom = 6
                elif newAngle == 210:
                    top = 7
                    bottom = 6
                elif newAngle == 225:
                    top = 5
                    bottom = 4
                elif newAngle == 240:
                    top = 4
                    bottom = 3
                elif newAngle == 270:
                    top = 3
                    bottom = 2
                elif newAngle == 300:
                    top = 5
                    bottom = 3
                elif newAngle == 315:
                    top = 7
                    bottom = 4
                else:
                    top = 11
                    bottom = 6                                      
            else:
                #If the fraction is actually a fraction, and it isn't in the hard coded part
                top = str(frat[-1])
                bottom = frat[0]
            if top == 11: #The top number is larger so the formatting is switched around
                text(top, 445, 280)
                text("-", 444, 300)
                text("-", 465, 300)
                text("-", 486, 300)
                text(bottom, 462, 330)
                text(" radians", 560, 300)
            elif top == 1: #One is smaller than the other digits so it needs its own formatting
                text(top, 477, 280)
                text("-", 475, 300)
                text("-", 485, 300)
                text(bottom, 480, 327)
                text(" radians", 500, 300)
            else: #For the rest of the numbers that are all around the same size
                text(top, 480, 280)
                text("-", 485, 300)
                text("-", 485, 300)
                text(bottom, 480, 327)
                text(" radians", 500, 300)
        elif newAngle == 360:
            text('2', 525, 300)
            text(" radians", 500, 300)
        elif newAngle == 180:
            text('1', 475, 300)
            text(" radians", 500, 300)
        else:
            text('0', 475, 300)
            text(" radians", 500, 300)   
    
    stroke(0, 255, 0) #The colour of the line and the perimeter of the circle
    strokeWeight (3) #The thickness of the line

def keyPressed():
    '''
    Exits the program when a key is pressed
    '''
    exit()



