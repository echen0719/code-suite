import math
import psutil

def getTargetPID(target_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == target_name:
            return proc.info['pid']
    return None

''' Euler's angles
- find the difference in all coordinate axes, giving a vector
- rotate the vector as needed using pitch, yaw, roll
- scale to prespective by getting distance
'''

# Unity = Left-handed, Y-up, Z-forward
def worldToScreen(playerPosition, cameraPosition, pitch, yaw, roll, screenWidth, screenHeight, fov=90.0):
    vectorX = playerPosition['x'] - cameraPosition['x']
    vectorY = playerPosition['y'] - cameraPosition['y']
    vectorZ = playerPosition['z'] - cameraPosition['z']

    # y, rotate yaw --> pitch and roll calc
    sinYaw = math.sin(-yaw)
    cosYaw = math.cos(-yaw)

    x1 = vectorX * cosYaw + vectorZ * sinYaw
    y1 = vectorY
    z1 = -vectorX * sinYaw + vectorZ * cosYaw

    # x, rotate pitch --> yaw and roll calc
    sinPitch = math.sin(-pitch)
    cosPitch = math.cos(-pitch)

    x2 = x1
    y2 = y1 * cosPitch - z1 * sinPitch
    z2 = y1 * sinPitch + z1 * cosPitch

    # z, rotate roll --> pitch and yaw calc
    sinRoll = math.sin(-roll)
    cosRoll = math.cos(-roll)

    x3 = x2 * cosRoll - y2 * sinRoll
    y3 = x2 * sinRoll + y2 * cosRoll
    z3 = z2

    # z=depth which is how far something is far from the camera
    if z3 <= 0:
        return None

    # POV draw a triangle
    focal = (screenWidth / 2.0) / math.tan(math.radians(fov) / 2.0)
    screenX = screenWidth / 2.0 + (x3 * focal) / z3
    screenY = screenHeight / 2.0 - (y3 * focal) / z3

    return screenX, screenY, z3 # return pixel and depth