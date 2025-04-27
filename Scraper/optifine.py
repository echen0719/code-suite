import requests

recommended = [
    "OptiFine_1.21.4_HD_U_J3",
    "OptiFine_1.21.3_HD_U_J2",
    "OptiFine_1.21.1_HD_U_J1",
    "OptiFine_1.20.4_HD_U_I7",
    "OptiFine_1.20.1_HD_U_I6",
    "OptiFine_1.19.4_HD_U_I4",
    "OptiFine_1.19.3_HD_U_I3",
    "OptiFine_1.19.2_HD_U_I2",
    "OptiFine_1.19.1_HD_U_H9",
    "OptiFine_1.19_HD_U_H9",
    "OptiFine_1.18.2_HD_U_H9",
    "OptiFine_1.18.1_HD_U_H6",
    "OptiFine_1.18_HD_U_H3",
    "OptiFine_1.17.1_HD_U_H1",
    "OptiFine_1.16.5_HD_U_G8",
    "OptiFine_1.16.4_HD_U_G7",
    "OptiFine_1.16.3_HD_U_G5",
    "OptiFine_1.16.2_HD_U_G5",
    "OptiFine_1.16.1_HD_U_G2",
    "OptiFine_1.15.2_HD_U_G6",
    "OptiFine_1.14.4_HD_U_G5",
    "OptiFine_1.14.3_HD_U_F2",
    "OptiFine_1.14.2_HD_U_F1",
    "OptiFine_1.13.2_HD_U_G5",
    "OptiFine_1.13.1_HD_U_E4",
    "OptiFine_1.13_HD_U_E4",
    "OptiFine_1.12.2_HD_U_G5",
    "OptiFine_1.12.1_HD_U_G5",
    "OptiFine_1.12_HD_U_G5",
    "OptiFine_1.11.2_HD_U_G5",
    "OptiFine_1.11_HD_U_G5",
    "OptiFine_1.10.2_HD_U_I5",
    "OptiFine_1.10_HD_U_I5",
    "OptiFine_1.9.4_HD_U_I5",
    "OptiFine_1.9.2_HD_U_E3",
    "OptiFine_1.9.0_HD_U_I5",
    "OptiFine_1.8.9_HD_U_M5",
    "OptiFine_1.8.8_HD_U_I7",
    "OptiFine_1.8.0_HD_U_I7",
    "OptiFine_1.7.10_HD_U_E7",
    "OptiFine_1.7.2_HD_U_F7"
]

alternatives = [
    "OptiFine_1.20.1_HD_U_I5",
    "OptiFine_1.19.4_HD_U_I3",
    "OptiFine_1.19.2_HD_U_I1", "OptiFine_1.19.2_HD_U_H9",
    "OptiFine_1.19_HD_U_H8",
    "OptiFine_1.18.2_HD_U_H7", "OptiFine_1.18.2_HD_U_H6",
    "OptiFine_1.18.1_HD_U_H5", "OptiFine_1.18.1_HD_U_H4",
    "OptiFine_1.16.5_HD_U_G7", "OptiFine_1.16.5_HD_U_G6",
    "OptiFine_1.16.4_HD_U_G6", "OptiFine_1.16.4_HD_U_G5",
    "OptiFine_1.16.3_HD_U_G4", "OptiFine_1.16.3_HD_U_G3",
    "OptiFine_1.16.2_HD_U_G3",
    "OptiFine_1.14.4_HD_U_F5", "OptiFine_1.14.4_HD_U_F4", "OptiFine_1.14.4_HD_U_F3", "OptiFine_1.14.4_HD_U_F2",
    "OptiFine_1.14.3_HD_U_F1",
    "OptiFine_1.13.2_HD_U_F5", "OptiFine_1.13.2_HD_U_E7", "OptiFine_1.13.2_HD_U_E6", "OptiFine_1.13.2_HD_U_E5", "OptiFine_1.13.2_HD_U_E4",
    "OptiFine_1.13.1_HD_U_E3",
    "OptiFine_1.12.2_HD_U_F5", "OptiFine_1.12.2_HD_U_F4", "OptiFine_1.12.2_HD_U_E3", "OptiFine_1.12.2_HD_U_E2", "OptiFine_1.12.2_HD_U_E1", "OptiFine_1.12.2_HD_U_D3", "OptiFine_1.12.2_HD_U_D2", "OptiFine_1.12.2_HD_U_D1", "OptiFine_1.12.2_HD_U_C9", "OptiFine_1.12.2_HD_U_C8", "OptiFine_1.12.2_HD_U_C7", "OptiFine_1.12.2_HD_U_C6", "OptiFine_1.12.2_HD_U_C5",
    "OptiFine_1.12.1_HD_U_F5", "OptiFine_1.12.1_HD_U_C7", "OptiFine_1.12.1_HD_U_C6", "OptiFine_1.12.1_HD_U_C5",
    "OptiFine_1.12_HD_U_F5", "OptiFine_1.12_HD_U_C7", "OptiFine_1.12_HD_U_C5", "OptiFine_1.12_HD_U_C4", "OptiFine_1.12_HD_U_C3", "OptiFine_1.12_HD_U_C2",
    "OptiFine_1.11.2_HD_U_F5", "OptiFine_1.11.2_HD_U_C7", "OptiFine_1.11.2_HD_U_C3", "OptiFine_1.11.2_HD_U_C2", "OptiFine_1.11.2_HD_U_C1", "OptiFine_1.11.2_HD_U_B9", "OptiFine_1.11.2_HD_U_B8", "OptiFine_1.11.2_HD_U_B7", "OptiFine_1.11.2_HD_U_B6", "OptiFine_1.11.2_HD_U_B5",
    "OptiFine_1.11_HD_U_F5", "OptiFine_1.11_HD_U_C7", "OptiFine_1.11_HD_U_C3", "OptiFine_1.11_HD_U_B8", "OptiFine_1.11_HD_U_B7", "OptiFine_1.11_HD_U_B6", "OptiFine_1.11_HD_U_B5", "OptiFine_1.11_HD_U_B3", "OptiFine_1.11_HD_U_B2", "OptiFine_1.11_HD_U_B1",
    "OptiFine_1.10.2_HD_U_H5", "OptiFine_1.10.2_HD_U_E7", "OptiFine_1.10.2_HD_U_E3", "OptiFine_1.10.2_HD_U_D8", "OptiFine_1.10.2_HD_U_D7", "OptiFine_1.10.2_HD_U_D6", "OptiFine_1.10.2_HD_U_D4", "OptiFine_1.10.2_HD_U_D3", "OptiFine_1.10.2_HD_U_D2", "OptiFine_1.10.2_HD_U_D1", "OptiFine_1.10.2_HD_U_C3", "OptiFine_1.10.2_HD_U_C2", "OptiFine_1.10.2_HD_U_C1",
    "OptiFine_1.10_HD_U_H5", "OptiFine_1.10_HD_U_E7", "OptiFine_1.10_HD_U_E3", "OptiFine_1.10_HD_U_D8", "OptiFine_1.10_HD_U_D7", "OptiFine_1.10_HD_U_C1", "OptiFine_1.10_HD_U_B7", "OptiFine_1.10_HD_U_B6",
    "OptiFine_1.9.4_HD_U_H5", "OptiFine_1.9.4_HD_U_E7", "OptiFine_1.9.4_HD_U_E3", "OptiFine_1.9.4_HD_U_D8", "OptiFine_1.9.4_HD_U_D7", "OptiFine_1.9.4_HD_U_B6", "OptiFine_1.9.4_HD_U_B5", "OptiFine_1.9.4_HD_U_B4",
    "OptiFine_1.9.2_HD_U_D8", "OptiFine_1.9.2_HD_U_D7", "OptiFine_1.9.2_HD_U_B3", "OptiFine_1.9.2_HD_U_B2", "OptiFine_1.9.2_HD_U_B1",
    "OptiFine_1.9.0_HD_U_H5", "OptiFine_1.9.0_HD_U_E7", "OptiFine_1.9.0_HD_U_E3", "OptiFine_1.9.0_HD_U_D8", "OptiFine_1.9.0_HD_U_D7", "OptiFine_1.9.0_HD_U_B5", "OptiFine_1.9.0_HD_U_B3", "OptiFine_1.9.0_HD_U_B2", "OptiFine_1.9.0_HD_U_B1",
    "OptiFine_1.8.9_HD_U_L5", "OptiFine_1.8.9_HD_U_I7", "OptiFine_1.8.9_HD_U_I3", "OptiFine_1.8.9_HD_U_H8", "OptiFine_1.8.9_HD_U_H7", "OptiFine_1.8.9_HD_U_H6", "OptiFine_1.8.9_HD_U_H5",
    "OptiFine_1.8.8_HD_U_I3", "OptiFine_1.8.8_HD_U_H8", "OptiFine_1.8.8_HD_U_H7", "OptiFine_1.8.8_HD_U_H6", "OptiFine_1.8.8_HD_U_H5",
    "OptiFine_1.8.0_HD_U_I3", "OptiFine_1.8.0_HD_U_H8", "OptiFine_1.8.0_HD_U_H7", "OptiFine_1.8.0_HD_U_H6", "OptiFine_1.8.0_HD_U_H5",
    "OptiFine_1.7.10_HD_U_E3", "OptiFine_1.7.10_HD_U_D8", "OptiFine_1.7.10_HD_U_D7", "OptiFine_1.7.10_HD_U_D6", "OptiFine_1.7.10_HD_U_D4", "OptiFine_1.7.10_HD_U_D3",
    "OptiFine_1.7.2_HD_U_F3", "OptiFine_1.7.2_HD_U_E8", "OptiFine_1.7.2_HD_U_E7", "OptiFine_1.7.2_HD_U_E4", "OptiFine_1.7.2_HD_U_E3"
]

previews = [
    "preview_OptiFine_1.21.4_HD_U_J4_pre2",
    "preview_OptiFine_1.21.4_HD_U_J4_pre1",
    "preview_OptiFine_1.21_HD_U_J1_pre9",
    "preview_OptiFine_1.21_HD_U_J1_pre8",
    "preview_OptiFine_1.21_HD_U_J1_pre6",
    "preview_OptiFine_1.20.6_HD_U_J1_pre18",
    "preview_OptiFine_1.20.6_HD_U_J1_pre17",
    "preview_OptiFine_1.20.6_HD_U_I9_pre1",
    "preview_OptiFine_1.20.4_HD_U_I8_pre4",
    "preview_OptiFine_1.20.4_HD_U_I8_pre3",
    "preview_OptiFine_1.20.4_HD_U_I8_pre2",
    "preview_OptiFine_1.20.2_HD_U_I7_pre1",
    "preview_OptiFine_1.20_HD_U_I5_pre5",
    "preview_OptiFine_1.20_HD_U_I5_pre4",
    "preview_OptiFine_1.17.1_HD_U_H2_pre1",
    "preview_OptiFine_1.17_HD_U_G9_pre26",
    "preview_OptiFine_1.17_HD_U_G9_pre25",
    "preview_OptiFine_1.12.2_HD_U_G6_pre1",
    "preview_OptiFine_1.8.9_HD_U_M6_pre2",
    "preview_OptiFine_1.8.9_HD_U_M6_pre1"
]

total = recommended + alternatives + previews

for i in range(0, len(total)):
    link = 'https://optifine.net/download?f={}.jar'.format(total[i])
    request = requests.get(link)
    if request.status_code == 200:
        with open('{}.jar'.format(total[i]), 'wb') as file:
            file.write(request.content)
    else:
        print('Failed to download file. Status code: {}'.format(request.status_code))
        print(total[i])
        exit