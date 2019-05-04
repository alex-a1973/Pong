from graphics import*

def main():
    #'Gamewin' creates a window in which objects can be drawn, also with its coordinates
    Gamewin = GraphWin("Square", 800, 600)
    #'ballSpeed' is the velocity of the ball
    ballSpeedPlus = 0.1
    ballSpeedMinus = -0.1

    #draws a ball with black outline, filled with black, and set it's initial coordinate with the radius
    ball = Circle(Point(400, 300), 5)
    ball.setFill("black")
    ball.setOutline("black")
    ball.draw(Gamewin)

    #draws both rectangles with black outline, filled with black, set it's initial coordinate for the opposite corners
    leftRectangle = Rectangle(Point(10, 275), Point(17, 325))
    leftRectangle.setFill("black")
    leftRectangle.setOutline("black")
    leftRectangle.draw(Gamewin)

    rightRectangle = Rectangle(Point(783, 275), Point(790, 325))
    rightRectangle.setFill("black")
    rightRectangle.setOutline("black")
    rightRectangle.draw(Gamewin)

    #'rightRectangleMove' is the velocity of the rectangle
    rightRectangleMoveX = 0
    rightRectangleMoveY = 0.05

    #'ballMove' moves with the velocity set to it in 'ballSpeed' both in the 'x' and 'y' coordinate
    ballMoveX = ballSpeedPlus
    ballMoveY = ballSpeedPlus

    leftPlayer = 0
    rightPlayer = 0
    scoreboard = Text(Point(400, 10), "Score")
    scoreboard.draw(Gamewin)
    scoreboardLeft = Text(Point(200, 10), leftPlayer)
    scoreboardLeft.draw(Gamewin)
    scoreboardRight = Text(Point(600, 10), rightPlayer)
    scoreboardRight.draw(Gamewin)

    while True:
        UserInput = Gamewin.checkKey()
        #Variable for the top corner of the left rectangle
        leftRectanglePosition = leftRectangle.getP1()
        rightRectanglePosition = rightRectangle.getP1()

        if UserInput == "w" and leftRectanglePosition.getY() >= 9:
            leftRectangle.move(0, -10)
        if UserInput == "s" and leftRectanglePosition.getY() <= 560:
            leftRectangle.move(0, 10)

        if rightRectanglePosition.getY() > 570:
            rightRectangleMoveY = -0.05
        if rightRectanglePosition.getY() < 0:
            rightRectangleMoveY = 0.05

        ballPosition = ball.getCenter()

        if ballPosition.getX() > 800:
            ball.move(-400, 0)
            ballMoveX = ballSpeedMinus
            leftPlayer = leftPlayer + 1
            scoreboardLeft.setText(leftPlayer)
        if ballPosition.getX() < 0:
            ball.move(400, 0)
            ballMoveX = ballSpeedPlus
            rightPlayer = rightPlayer + 1
            scoreboardRight.setText(rightPlayer)

        if ballPosition.getY() > 595:
            ballMoveY = ballSpeedMinus
        if ballPosition.getY() < 5:
            ballMoveY = ballSpeedPlus

        #These nested "if" statements creates a barrier at which the ball bounces off of at the x-coord equal to the left rectangle's x-coord
        #And designate the surface area the ball bounces off of between trapped y-coords
        if ballPosition.getX() - 5 <= leftRectanglePosition.getX() + 7:
            if ballPosition.getY() > leftRectanglePosition.getY():
                if ballPosition.getY() < leftRectanglePosition.getY() + 50:
                    ballMoveX = ballSpeedPlus

        #These nested "if" statements creates a barrier at which the ball bounces off of at the x-coord equal to the right rectangle's x-coord
        if ballPosition.getX() + 5 >= rightRectanglePosition.getX():
            if ballPosition.getY() > rightRectanglePosition.getY():
                if ballPosition.getY() < rightRectanglePosition.getY() + 50:
                    ballMoveX = ballSpeedMinus

        
        ball.move(ballMoveX, ballMoveY)
        rightRectangle.move(rightRectangleMoveX, rightRectangleMoveY)

main()