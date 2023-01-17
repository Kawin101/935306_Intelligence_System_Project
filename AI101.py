import numpy as np
import matplotlib.pyplot as plt

# Define

# ** Point 2 **
# Route 1 (km.)
A = 0
B = 0
C = 0
AtoB = 10
BtoE = 8
BtoF = 6

AtoC = 8
CtoG = 4
CtoH = 2

# Route 2 (lane.)
LAtoB = 4
LBtoE = 2
LBtoF = 2

LAtoC = 4
LCtoG = 2
LCtoH = 4

# Set vule to fine min of position (หาตำแหน่งที่ใกล้ที่สุด)
kmMin01 = min(AtoB, AtoC)
kmMin02 = min(BtoE, BtoF, CtoG, CtoH)
print(' ** The Shortest Path is :  ** ')
print('A -> C =', kmMin01 , 'km.')
print('C -> H =', kmMin02 , 'km.')
print('Total: [A -> C -> H] =',kmMin01+kmMin02, 'km.')

# Max lane size find
laneMin01 = max(LAtoB, LAtoC)
laneMin02 = max(LBtoE, LBtoF, LCtoG, LCtoH)
print(' ** The Big lane size is : **')

if AtoB > AtoC:
  print('Max size Lane = A -> C', laneMin01, 'lane.')
else:
  print('going to A -> B')

if CtoG > CtoH:
  print('Max size Lane = C -> H', laneMin02, 'lane.')
else:
  print('goint to C -> G')

if AtoB > AtoC:
  if CtoG > CtoH:
    print('Total: [A -> C -> H] =', laneMin01+laneMin02, 'lane.')

# ** Point 3 **
# Define
SH01 = (60/100)
SH02 = (40/100)

# Route 1 (Fine best result)
math01 = AtoB * SH01 + LAtoB * SH02
math02 = AtoC * SH01 + LAtoC * SH02
math03 = BtoE * SH01 + LBtoE * SH02
math04 = BtoF * SH01 + LBtoF * SH02
math05 = CtoG * SH01 + LCtoG * SH02
math06 = CtoH * SH01 + LCtoH * SH02

print(' ** The best road is : **')
if math01 > math02: 
  print('A -> B =', math01)
else:
  print('A -> C =', math02)

if math03 > math04:
  print('B -> E =', math03)
else:
  print('B -> F =', math04)

#if math05 > math06:
  #print('C -> G =', math05, )
#else:
  #print('C -> H =', math06)

if math01 > math02:
  if math03 > math04:
    print('Total : [A -> B -> E] =',math01+math03)

# ** Point 1 **
# Output
plt.subplot(121), plt.plot([0,kmMin01], [0,laneMin01])
plt.subplot(121), plt.plot([0,kmMin02], [0,laneMin02])
plt.xlabel('x - km.')
plt.ylabel('y - lane.')

plt.title('The Shortest Path App AI101')
plt.show