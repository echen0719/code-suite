commonValues = {
    "arrayLengthOffset": 0x18, # gets the length of the array
    "arrayStartOffset": 0x20
}

CGameStateValues = {
    # pointer chain
    "staticRVA": 0x35F4968,
    "offsets": [0xB8, 0x10, 0x3B0],

    # positions
    "positionOffset": 0x78,

    # camera attributes
    "cameraPositionOffset": 0x18,
    "cameraOrientationOffset": 0x24,
}

webguyValues = {
     # pointer chain
    "staticRVA": 0x35F4968,
    "offsets": [0xB8, 0x10],

    "visibleListOffset": 0x560
}