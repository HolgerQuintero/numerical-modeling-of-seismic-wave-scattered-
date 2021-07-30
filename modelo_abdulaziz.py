# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:28:37 2021

@author: USUARIO
"""

## MODELO ARTICULO ABDULAZIZ
##Vmin=1000,f=30, then dh=1.

import math as m
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d



Vmin=1000; Fq=30; Nl=30; Vmax=3000; 
dh=Vmin/(Fq*Nl)
vR=0.92*Vmin;
LR=vR/Fq;
dh=1;
dt=(dh/Vmax)*m.sqrt(3/8)
dt=2e-4;
Lx=round((0.5*Vmax)/(Fq))
Dx=1000; Dz=500;
dx=dh;  dz=dh;
x=np.arange(0,Dx+1,dh); z=np.arange(0,Dz+1,dh);
Nx=np.size(x); Nz=np.size(z);
top=round(50/dx);
model_vp=np.zeros((Nz,Nx));
model_vs=np.zeros((Nz,Nx));
model_rho=np.zeros((Nz,Nx));
VP=1000; VS=400; RHO=2500;
vp=VP*np.ones((Nz,Nx));
vs=VS*np.ones((Nz,Nx));
rho=RHO*np.ones((Nz,Nx));

#%%TOPOGRAFY
mean=0
SD=15
IGS = np.random.normal(mean, SD, Nx)
IGS=IGS/(np.max(IGS)/SD) #IRREGULAR GAUSSIAN SURFACE
IGS=np.round(IGS)

IGS=gaussian_filter(IGS, sigma=5) #FILTRO GAUSSIANO


mask1=np.zeros((Nz,Nx))
for i in np.arange(Nx):
   for j in  np.arange(Nz):
       if j <= 65+IGS[i] and j>=top:
           mask1[j,i]=1

#%%Estratos 
#horizontales
#mask1=np.zeros((Nz,Nx))
#for i in np.arange(top,100):
 #  for j in  np.arange(Nx):
  #     mask1[i,j]=1
#       if np.sqrt(np.power(i-65,2)+np.power(j-360,2)) <= 10:
 #           mask1[i,j]=0
  #     if np.sqrt(np.power(i-65,2)+np.power(j-720,2)) <= 10:
   #         mask1[i,j]=0


mask2=np.zeros((Nz,Nx))
for i in np.arange(Nx):
   for j in  np.arange(Nz):
       if j > 65+IGS[i] and j<250:
           mask2[j,i]=1
       
mask3=np.zeros((Nz,Nx))
for i in np.arange(250,Nz):
   for j in  np.arange(Nx):
       mask3[i,j]=1
#%%Cuerpo incrustado
#circulo
#mask2=np.zeros((Nz,Nx))
#for i in np.arange(Nz):
 #   for j in np.arange(Nx):
  #      if np.sqrt(np.power(i-65,2)+np.power(j-360,2)) <= 10:
   #         mask2[i,j]=1
                 
#for i in np.arange(Nz):
 #   for j in np.arange(Nx):
  #      if np.sqrt(np.power(i-65,2)+np.power(j-720,2)) <= 10:
   #         mask2[i,j]=1
   
#mask3=np.zeros((Nz,Nx))   
#for i in np.arange(top,100):
 #  for j in  np.arange(Nx):
  #     mask3[i,j]=1



#%% Modelo

model_vp=1800*mask1+3000*mask2+5000*mask3
model_vs=1000*mask1+1500*mask2+2250*mask3
model_rho=1750*mask1+2250*mask2+2750*mask3

#%%Guardado de datos
np.save('model_vp',model_vp)  
np.save('model_vs',model_vs)  
np.save('model_rho',model_rho)  
#PARA LEER ARCHIVOS. dat 
#Vp=np.loadtxt('model_vp.dat')  

#%%Gráficas

plt.figure(1)
ax1 = plt.subplot(131)     
plt.imshow(model_vp,cmap='gray')
plt.ylabel('Profundidad [Km]')
plt.xlabel('Distancia [m]')
plt.colorbar()

ax2 = plt.subplot(132)     
plt.imshow(model_vs,cmap='gray')
plt.ylabel('Profundidad [Km]')
plt.xlabel('Distancia [m]')
plt.colorbar()

ax3 = plt.subplot(133)     
plt.imshow(model_rho,cmap='gray')
plt.ylabel('Profundidad [m]')
plt.xlabel('Distancia [m]')
plt.colorbar()
plt.plot(150,60, marker='*', color='black')
plt.title('Modelo de Densidad [Kg/m^3]')

plt.show()
#save model_vp model_vp
#save model_vs model_vs 
#save model_rho model_rho
    