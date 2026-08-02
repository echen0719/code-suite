import math
import psutil

def getTargetPID(targetName):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == targetName:
            print("PID: {}".format(proc.info['pid']))
            return proc.info['pid']
    return None

''' Euler's angles
- find the difference in all coordinate axes, giving a vector
- rotate the vector as needed using pitch, yaw, roll
- scale to prespective by getting distance
'''

position3DHistory = {}

# 100ms seems resonable
def smooth3D(playerID, x, y, z, currentTime, maxRate=0.1):
    if playerID not in position3DHistory: # create new on join
        position3DHistory[playerID] = {
            'thisX': x, 'thisY': y, 'thisZ': z,
            'lastX': x, 'lastY': y, 'lastZ': z,
            'time': currentTime,
            'velocityX': 0.0, 'velocityY': 0.0, 'velocityZ': 0.0 # velocities
        }
        return x, y, z

    history = position3DHistory[playerID]
    elapsed = currentTime - history['time']

    if x != history['thisX'] or y != history['thisY'] or z != history['thisZ']:
        dt = currentTime - history['time']

        if dt > 0.001:
            history['velocityX'] = (x - history['thisX']) / dt
            history['velocityY'] = (y - history['thisY']) / dt
            history['velocityZ'] = (z - history['thisZ']) / dt

        # prepare for next iteration
        history['lastX'], history['lastY'], history['lastZ'] = history['thisX'], history['thisY'], history['thisZ']
        history['thisX'], history['thisY'], history['thisZ'] = x, y, z
        history['time'] = currentTime

        elapsed = 0.0

    # interpolation
    if elapsed <= maxRate:
        time = elapsed / maxRate
        return ( # standard lerping formula
            history['lastX'] + (history['thisX'] - history['lastX']) * time,
            history['lastY'] + (history['thisY'] - history['lastY']) * time,
            history['lastZ'] + (history['thisZ'] - history['lastZ']) * time
        )
    else: # extrapolation
        extra = elapsed - maxRate
        return (
            history['thisX'] + history['velocityX'] * extra,
            history['thisY'] + history['velocityY'] * extra,
            history['thisZ'] + history['velocityZ'] * extra
        )

position2DHistory = {}

def smooth2D(playerID, x, y, currentTime, maxRate=0.1):
    if playerID not in position2DHistory:
        position2DHistory[playerID] = {
            'thisX': x, 'thisY': y,
            'lastX': x, 'lastY': y,
            'time': currentTime,
            'velocityX': 0.0, 'velocityY': 0.0
        }
        return x, y

    history = position2DHistory[playerID]
    elapsed = currentTime - history['time']

    if x != history['thisX'] or y != history['thisY']:
        dt = currentTime - history['time']
        if dt > 0.001:
            history['velocityX'] = (x - history['thisX']) / dt
            history['velocityY'] = (y - history['thisY']) / dt

        history['lastX'], history['lastY'] = history['thisX'], history['thisY']
        history['thisX'], history['thisY'] = x, y
        history['time'] = currentTime

        elapsed = 0.0

    if elapsed <= maxRate:
        time = elapsed / maxRate
        return (
            history['lastX'] + (history['thisX'] - history['lastX']) * time,
            history['lastY'] + (history['thisY'] - history['lastY']) * time
        )
    else:
        extra = elapsed - maxRate
        return (
            history['thisX'] + history['velocityX'] * extra,
            history['thisY'] + history['velocityY'] * extra
        )

# Unity = Left-handed, Y-up, Z-forward
def worldToScreen(playerPosition, cameraInfo, screenWidth, screenHeight, fov=90):
    vectorX = playerPosition['x'] - cameraInfo['x']
    vectorY = playerPosition['y'] - cameraInfo['y']
    vectorZ = playerPosition['z'] - cameraInfo['z']

    pitch = cameraInfo['pitch']
    yaw = cameraInfo['yaw']
    roll = cameraInfo['roll']

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
    focalY = (screenHeight / 2.0) / math.tan(math.radians(fov) / 2.0)
    focalX = focalY * (screenWidth / screenHeight)

    screenX = screenWidth / 2.0 + (x3 * focalX) / z3
    screenY = screenHeight / 2.0 - (y3 * focalY) / z3

    return screenX, screenY, z3 # return pixel and depth