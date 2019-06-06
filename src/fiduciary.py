import cv2
import numpy as np
import imageio

fid = cv2.imread('/mnt/finkbeinernas/robodata/Sina/Robo6_fiduciary_troubleshooting/JAK-AD-NPC4/PID20190423_JAK-AD'
                 '-NPC4_T0_0-0_A1_Fiducial_MONTAGE-Brightfield_0_0_0.tif', cv2.IMREAD_ANYDEPTH)
fid2 = cv2.imread('/mnt/finkbeinernas/robodata/Sina/Robo6_fiduciary_troubleshooting/JAK-AD-NPC4/PID20190423_JAK-AD-NPC4_T1_4-0_A1_Fiducial_MONTAGE-Brightfield_0_0_0.tif', cv2.IMREAD_ANYDEPTH)

img1 = np.array(fid)
img2 = np.array(fid2)
print(img1.shape)
print(img2.shape)

stack = np.dstack((img1, img2))
# print(stack)

_ones = np.ones_like(stack)

_zeros = np.zeros_like(stack)
zeros = np.where(stack < 1000, 1, 0)

print(zeros.shape)
Xzeros = np.sum(zeros, axis=0)
Yzeros = np.sum(zeros, axis=1)
Xsort = np.sort(Xzeros)
Ysort = np.sort(Yzeros)

Xcenter = np.median(Xsort)
Ycenter = np.median(Ysort)
print('The center is: ', Xcenter, Ycenter)
xBin = 5
yBin = 5

xSign = -1
ySign = 1

Xoffset = xBin * Xcenter * xSign * 0.645
Yoffset = yBin * Ycenter * ySign * 0.645

print('The offset is: ', round(Xoffset), round(Yoffset))

# print(Xsort)
# print(Ysort)

