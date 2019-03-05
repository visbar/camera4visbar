# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 17:24:13 2019

@author: kuwataakiyoshi
"""

import sys
import numpy as np

#Focal point
def FocalPoint(xmin,xmax,ymin,ymax,zmin,zmax):
    FPx = ((xmax - xmin) + ((xmax - xmin)*6) / 7.) / 2.
    FPy = ((ymax - ymin) + ((ymax - ymin)*6) / 7.) / 2.
    FPz = zmax + zmin
    FPtemp = ('FocalPoint %f %f %f\n' % (FPx,FPy,FPz))
    return FPtemp

#Camera position
def CameraPosition(xmin,xmax,ymin,ymax):
    x_len = xmax - xmin
    y_len = ymax - ymin
    CPx = (x_len + (x_len*6) / 7.) / 2.
    CPy = (y_len + (y_len*6) / 7.) / 2.
    CPz = np.sqrt(x_len**2 + y_len**2) * 4
    CPtemp = ('CameraPosition %f %f %f\n' % (CPx,CPy,CPz))
    return CPtemp

#How much to zoom
def ParallelScale(ymin,ymax):
    PSy = ((ymax - ymin) + ((ymax - ymin)*14) / 13.) / 2.
    PStemp = ('ParallelScale %f\n' % (PSy))
    return PStemp

#View up
def ViewUp():
    VUtemp = ('ViewUp %f %f %f\n' % (0., 1., 0.))
    return VUtemp

#setting of clipping range
def ClippingRange(xmin,xmax,ymin,ymax,zmin,zmax):
    x_len = xmax - xmin
    y_len = ymax - ymin
    FPz = zmax + zmin
    CR2 = np.sqrt(x_len**2 + y_len**2) * 4
    CR1 = CR2 - FPz
    CRtemp = ('ClippingRange %f %f\n' % (CR1, CR2))
    return CRtemp

if __name__ == '__main__':
    xyz = sys.argv[1]
    x = []
    y = []
    z = []
    with open(xyz, 'r') as fp:
        line = fp.readline() #atom_num cell_x cell_y cell_z
        atom_num = line.split()[0]
        cell_x, cell_y, cell_z = float(line.split()[1]), float(line.split()[2]), float(line.split()[3])
        line = fp.readline()
        for lin in range(int(atom_num)):
            lin = fp.readline()
            sp = lin.split()
            x.append(float(sp[1]))
            y.append(float(sp[2]))
            z.append(float(sp[3]))
    xmin, xmax = min(x), max(x)
    ymin, ymax = min(y), max(y)
    zmin, zmax = min(z), max(z)
    
    with open('CameraSetting.txt', 'w') as f:
        f.write(FocalPoint(xmin,xmax,ymin,ymax,zmin,zmax))
        f.write(CameraPosition(xmin,xmax,ymin,ymax))
        f.write(ParallelScale(ymin,ymax))
        f.write(ViewUp())
        f.write(ClippingRange(xmin,xmax,ymin,ymax,zmin,zmax))