
import math
import time
from optimize import optimize


print("starting test 1: predefined test cases")
# cur, desired, expected angle, expected direction
cases = [
    [-180, 10, -170, "reverse"],
    [-180, 70, -110, "reverse"],
    [-180, 100,-260, "forward"],
    [-90,  75, -65,  "reverse"], 
    [-90, -20, -20,  "forward"], 
    [-90, 210, -150, "forward"],
    [3000, -1800, 3060, "reverse"],
    [3000, 1800, 3060, "reverse"],
    [-3000, -1800, -3060, "reverse"],
    [-3000, 1800, -3060, "reverse"]
]
for case in cases:
    angle, direction = optimize(case[1], case[0])
    
    assert angle == case[2] or direction == case[3], f"TEST FAILED: case {case} failed with return val: {angle}, {direction}" 

print(f"test 1 with all {len(cases)} cases passed!")

print("starting test 2: All possible cases over rotate 90deg check, all values from -400 deg to 400 deg with increment of 1, this will take some time")
startTime = time.monotonic_ns()
current = -400.0
while current < 400.0:
    desired = -400.0
    while desired < 400.0:
        angle, direction = optimize(desired, current)

        assert abs(current - angle) < 91, f"TEST FAILED: res rotation > 90+1 deg with desired {desired}, current {current}. Res: {angle} {direction}"
        desired += 1
    current += 1
endTime = time.monotonic_ns()
print("test 2 passed!")

print("All tests passed successfully!")