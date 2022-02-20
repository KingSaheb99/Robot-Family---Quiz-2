#Resources:
    # https://www.youtube.com/watch?v=RSl87lqOXDE&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=4
    # https://www.youtube.com/watch?v=3ohzBxoFHAY
    # https://www.youtube.com/watch?v=uYu4hCjYDhY
    # https://www.w3schools.com/python/python_inheritance.asp
    # https://www.geeksforgeeks.org/types-of-inheritance-python/?ref=lbp
    # https://py.processing.org/reference/

numRobots = 1;
robots = [0] * numRobots;
currentRobot = 0;

shapeSize = 25;

def setup():
    size(1980, 1240);
    smooth();
    global numRobots, robots;
    for i in range(numRobots):
        robots[i] = Robot(1, 1, 1, True, width/2, height/4);
    
def draw():
    global numRobots, robots;
    background(255, 255, 255);
    
    for i in range(numRobots):
        robots[i].display();
        
    progenitorBot = oldBot(1, "c", 1, "The Old One", 1, 1);
    progenitorBot.start(width/2, height/8 * progenitorBot.genNum);
    progenitorBot.display();
        
def mousePressed():
    global numRobots, currentRobot;
    robots[currentRobot].start(mouseX, mouseY);
    currentRobot += 1;
    if(currentRobot >= numRobots):
        currentRobot = 0;
        
class Robot(object): 
    def __init__(self, genNum, shapeType, colourType, botName, x, y):
        self.genNum = genNum;
        self.shapeType = shapeType;
        self.colourType = colourType;
        self.botName = botName;
        self.x = x;
        self.y = y;
                
    def start(self, posX, posY):
        self.x = posX;
        self.y = posY;
        
    def display(self):
        fill(0, 0, 255);
        if (self.genNum % 2 == 0):
            strokeWeight(0);
        else:
            strokeWeight(5);
        stroke(0, 0, 0);
        
        rectMode(CENTER);
        ellipseMode(CENTER);
        
        if(self.shapeType == "a"):
            ellipse(self.x, self.y, shapeSize, shapeSize)
        elif(self.shapeType == "b"):
            rect(self.x, self.y, shapeSize, shapeSize);
        elif(self.shapeType == "c"):
            ellipse(self.x, self.y, shapeSize, shapeSize);
            #triangle(self.x, self.y, (self.x) + 10, (self.y) + 10, (self.x) - 10, (self.y) - 10);
        
class oldBot(Robot):
    def __init__(self, genNum, shapeType, colourType, botName, x, y):
        Robot.__init__(self, genNum, shapeType, colourType, botName, x, y);
        
    def display(self):
        fill(127);
        if (self.genNum % 2 == 0):
            strokeWeight(0);
        else:
            strokeWeight(3);
        stroke(0, 0, 0);
        
        rectMode(CENTER);
        ellipseMode(CENTER);
        
        if(self.shapeType == "a"):
            ellipse(self.x, self.y, shapeSize, shapeSize)
        elif(self.shapeType == "b"):
            rect(self.x, self.y, shapeSize, shapeSize);
        elif(self.shapeType == "c"):
            ellipse(self.x, self.y, shapeSize, shapeSize);
            #triangle(self.x, self.y, (self.x) + 10, (self.y) + 10, (self.x) - 10, (self.y) - 10);
        
class Child(Robot):
    def __init__(self, genNum, shapeType, colourType, botName, x, y):
        Robot.__init__(self, genNum, shapeType, colourType, botName, x, y);
