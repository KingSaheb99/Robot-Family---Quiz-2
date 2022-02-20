#Resources:
    # https://www.youtube.com/watch?v=RSl87lqOXDE&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=4
    # https://www.youtube.com/watch?v=3ohzBxoFHAY
    # https://www.youtube.com/watch?v=uYu4hCjYDhY
    # https://www.w3schools.com/python/python_inheritance.asp
    # https://www.geeksforgeeks.org/types-of-inheritance-python/?ref=lbp
    # https://py.processing.org/reference/

shapeSize = 25;

def setup():
    size(1980, 1240);
    background(255, 255, 255);
    smooth();
        
def draw():        
    progenitorBot = oldBot(1, "a", 0, "The Old One", 1, 1);
    progenitorBot.run();
        
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
        
    def strokeGen(self):
        if (self.genNum % 2 == 0):
            strokeWeight(0);
        else:
            strokeWeight(5);
        stroke(0, 0, 0);
        
    def shapeGen(self):
        rectMode(CENTER);
        ellipseMode(CENTER);
        
        if(self.shapeType == "a"):
            ellipse(self.x, self.y, shapeSize, shapeSize)
        elif(self.shapeType == "b"):
            rect(self.x, self.y, shapeSize, shapeSize);
        elif(self.shapeType == "c"):
            ellipse(self.x, self.y, shapeSize, shapeSize);
            #triangle(self.x, self.y, (self.x) + 10, (self.y) + 10, (self.x) - 10, (self.y) - 10);
            
    def colourGen(self):
        if(self.colourType == 0):
            fill(127);
        elif(self.colourType == 1):
            fill(255, 0, 0);
        elif(self.colourType == 2):
            fill(0, 0, 255);
        elif(self.colourType == 3):
            fill(0, 255, 0);
        elif(self.colourType == 4):
            fill(195, 3, 255);
        elif(self.colourType == 5):
            fill(254, 255, 18);
            
    def run(self):
        self.start(width/4 * self.genNum, height/4 * self.genNum);
        self.strokeGen();
        self.shapeGen();
        self.colourGen();
        
class oldBot(Robot):
    def __init__(self, genNum, shapeType, colourType, botName, x, y):
        Robot.__init__(self, genNum, shapeType, colourType, botName, x, y);
        
class childA(oldBot):
    def __init__(self, genNum, shapeType, colourType, botName, x, y):
        Robot.__init__(self, genNum, shapeType, colourType, botName, x, y);
