# Optimize

This is an implementation of the angle optimization algorithm that is based on distance comparisons. 

This differs from WPILIB's `SwerveDriveModule.Optimize` in that there is no assumptions on that if `angleDelta > 180`; the supplementary angle must give a smaller heading change. 

This implenmentation also allows direct output of the optimized angle to the motor without any additional continuous requirements/math. Any angle change should result in the encoder position changing to `currentPositionDegrees +- 90deg`; There will be no wrap around due to positive/negative suddent angle changes.

The everything is based on distance comparisons in this algorithm. We also ensure that all angle inputs are valid. Any input for the desired or current angle can be negative or positive up to infinity. 

WPILIB's implementation does have less math operations, but the performance hit should be negligible.

### Proof of Concept & test function in ./py also could work for python robots
### Java implementation example in Optimize.java 
### Don't have C++, but it should work if you copy over the java code and change some datatypes and namespaces.  

#### Special Thanks to Issac on the math StackExchange for the algorithm on finding the shortest rotation between 2 angles. [https://math.stackexchange.com/a/110236](https://math.stackexchange.com/a/110236)
