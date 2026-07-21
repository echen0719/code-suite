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

def worldToScreen(playerPosition, cameraPosition, pitch, yaw, roll, screenWidth, screenHeight, fov=60.0):
    vectorX = playerPosition['x'] - cameraPosition['x']
    vectorY = playerPosition['y'] - cameraPosition['y']
    vectorZ = playerPosition['z'] - cameraPosition['z']

    # angles are negated since if player turns right, the world turns left and vice versa
    pitch = -pitch # x
    sinPitch = math.sin(pitch)
    cosPitch = math.cos(pitch)

    yaw = -yaw # y
    sinYaw = math.sin(yaw)
    cosYaw = math.cos(yaw)

    roll = -roll # z
    sinRoll = math.sin(roll)
    cosRoll = math.cos(roll)

    # rotate pitch --> yaw and roll calc
    y, z = (
        vectorY * cosPitch - vectorZ * sinPitch,
        vectorY * sinPitch + vectorZ * cosPitch
    )

    # rotate yaw --> pitch and roll calc
    x, z = (
        vectorX * cosYaw + z * sinYaw,
        -vectorX * sinYaw + z * cosYaw
    )

    # rotate roll --> pitch and yaw calc
    x, y  = (
        x * cosRoll - y * sinRoll,
        x * sinRoll + y * cosRoll
    )

    # z=depth which is how far something is far from the camera
    if z <= 0:
        return None

    # POV draw a triangle
    focal = (screenWidth / 2) / math.tan(math.radians(fov) / 2)
    screenX = (x * focal) / z + screenWidth / 2
    screenY = screenHeight / 2 - (y * focal) / z

    return screenX, screenY