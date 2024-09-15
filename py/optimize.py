
import math

# find shortest path of rotation, assuming angles are from 0 to 360
# Isaac (https://math.stackexchange.com/users/72/isaac), Shortest way to achieve target angle, URL (version: 2012-02-17): https://math.stackexchange.com/q/110236
def calcShortestDistanceBetweenAngles(target: float, current: float):
    alpha = target - current
    beta = target - current + 360.0
    gamma = target - current - 360.0 

    alphaAbs = abs(alpha)
    betaAbs = abs(beta)
    gammaAbs = abs(gamma)
    if alphaAbs < betaAbs and alphaAbs < gammaAbs: 
        return alpha
    
    # code will not reach here unless: betaAbs < alphaAbs and gammaAbs < alphaAbs 
    elif betaAbs < gammaAbs:
        return beta
    
    # code will not reach here unless: gammaAbs < betaAbs and gammaAbs < alphaAbs 
    else:
        return gamma

def optimize(desiredAngle:float, currentMotorAnglePos:float) -> tuple[float, str]:
    # convert any negative angles to positive angle equivalents 
    while desiredAngle < 0: desiredAngle += 360.0
    desiredAngle = desiredAngle % 360.0

    currentAngle = currentMotorAnglePos
    while currentAngle < 0: currentAngle += 360.0
    currentAngle = currentAngle % 360.0

    # calculate the other supplementary angle 
    altAngle = (desiredAngle + 180.0) % 360.0

    # find how to get to those 2 angles
    transToDesired = calcShortestDistanceBetweenAngles(desiredAngle, currentAngle)
    transToAlt = calcShortestDistanceBetweenAngles(altAngle, currentAngle)
    
    # find which of the 2 possible angles have a shorter travel distance
    resTransform = transToDesired
    resDirection = "forward"
    # compares distance of transformation between the 2 possible angles
    if abs(transToAlt) < abs(transToDesired):  
        resTransform = transToAlt
        resDirection = "reverse"

    return currentMotorAnglePos + resTransform, resDirection

