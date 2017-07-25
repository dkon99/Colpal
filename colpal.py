# -*- coding: utf-8 -*-
"""
Created on Sat May  6 07:51:06 2017

@author: dkon9
"""

import numpy as np
#from scipy.interpolate import NearestNDInterpolator


getnumcol = 9

num_col = np.arange(0,getnumcol,1)


color =[0,0,0]

pal = np.arange(0,256,1)

colpal=np.array([[196, 202, 206],     # 0) unknown grey
        [30, 144, 255],     # 1) carb dodger blue
        [240, 230, 140],    #2)sand,khaki
        [128, 128, 0],       # 3) shale olive
        [0, 0,0],        #4) coal black
        [162, 42, 42],      #5) oil  brown    
        [255, 0, 0],        #6) gas red
        [244,164,96],    #7) misc1 sandybrown
        [144, 238, 144]    #8) misc2  lightgreen
       ])  


num = np.round(np.arange(0,257,(256/8)))

lith=[]
lith.append(colpal[0].tolist())
x=1
for i in range(9):
    while (x<num[i]):
        lith.append(colpal[i].tolist())
        #print(i,x,colpal[i])
        x+=1
#print(lith)
    
# Define Data
RESULTS = lith

# Open File
resultFyle = open("c:\data\RGpal.pal",'w')

resultFyle.write("struct ColorPalette {" + '\n' +
    "    Name"  + '\n' +
    '    Colors [ N ] {' + '\n' +
        '        Red Green Blue' + '\n' +
    '    }'  + '\n' +
'}'  + '\n' +

'ColorPalette "RGsyn1" 256'+ '\n')

# Write data to file
for r in RESULTS:
    r_str = " ".join(str(x) for x in r)
    #print(r_str)
    resultFyle.write(r_str+'\n')
resultFyle.close()
        

print("success")
        
