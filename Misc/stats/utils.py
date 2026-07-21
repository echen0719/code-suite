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
def worldToScreen(playerPosition, cameraPosition, pitch, yaw, roll, screenWidth, screenHeight, fov=60.0):
    vectorX = playerPosition['x'] - cameraPosition['x']
    vectorY = playerPosition['y'] - cameraPosition['y']
    vectorZ = playerPosition['z'] - cameraPosition['z']

    # x
    sinPitch = math.sin(pitch)
    cosPitch = math.cos(pitch)

    # y
    sinYaw = math.sin(yaw)
    cosYaw = math.cos(yaw)

    # rotate yaw --> pitch and roll calc
    x1 = vectorX * cosYaw + vectorZ * sinYaw
    z1 = -vectorX * sinYaw + vectorZ * cosYaw

    # rotate pitch --> yaw and roll calc
    y2 = vectorY * cosPitch - z1 * sinPitch
    z2 = vectorY * sinPitch + z1 * cosPitch

    # rotate roll --> pitch and yaw calc
    x3 = x1 * math.cos(roll) - y2 * math.sin(roll)
    y3 = x1 * math.sin(roll) + y2 * math.cos(roll)

    # z=depth which is how far something is far from the camera
    if z2 <= 0:
        return None

    # POV draw a triangle
    focal = (screenWidth / 2.0) / math.tan(math.radians(fov) / 2.0)
    screenX = screenWidth / 2.0 + (x3 * focal) / z2
    screenY = screenHeight / 2.0 - (y3 * focal) / z2

    return screenX, screenY, z2 # return pixel and depth