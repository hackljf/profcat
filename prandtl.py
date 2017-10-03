import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid.inset_locator import(inset_axes,InsetPosition,mark_inset)
from matplotlib.ticker import FormatStrFormatter

ncases=3

tmp=np.loadtxt("./ce40cmax0.3meshh/1smoothed/profiles/uprof20000")
dims=tmp.shape
nx=dims[0]
x=tmp[:,0]
T=np.zeros((nx,ncases))
Texact=np.zeros((nx,ncases))
u=np.zeros((nx,ncases))
uexact=np.zeros((nx,ncases))
rho=np.zeros((nx,ncases))
rhoexact=np.zeros((nx,ncases))
nus=np.zeros((nx,ncases))
numax=np.zeros((nx,ncases))
resid=np.zeros((nx,ncases))

#nums=["10000","20000"]
num="20000"
cases=["ce40cmax0.3meshh/1smoothed/profiles/","ce40cmax0.3meshh/1smoothed/profiles_pr0.75/","ce40cmax0.3meshh/1smoothed/profiles_pr0.4/"]
ipr=["1","0.75","0.4"]

for (j,case) in enumerate(cases):
   fname=case+"Tprof"+num
   tmp=np.loadtxt(fname,usecols=(1,2))
   T[:,j]       =tmp[:,0]
   Texact[:,j]  =tmp[:,1]
   fname=case+"rhoprof"+num
   tmp=np.loadtxt(fname,usecols=(1,2))
   rho[:,j]     =tmp[:,0]
   rhoexact[:,j]=tmp[:,1]
   fname=case+"uprof"+num
   tmp=np.loadtxt(fname,usecols=(1,2))
   u[:,j]       =tmp[:,0]
   uexact[:,j]  =tmp[:,1]
#     fname=case+"viscprof"+num
#     tmp=np.loadtxt(fname,usecols=(1,2,3))
#     nus[:,i,j]     =tmp[:,0]
#     numax[:,i,j]   =tmp[:,1]
#     resid[:,i,j]   =tmp[:,2]

width=8.5
height=5
fsize=18

plt.figure(figsize=(width,height))
plt.plot(x,Texact[:,0],'k-',label='exact')
for j in range(ncases):
   plt.plot(x,T[:,j],label=r'$\mathcal{P}=$'+ipr[j])
plt.legend(loc='upper left')
plt.xlim((0.0,0.35))
plt.ylim((0.7,1.2))
plt.xlabel(r'$x$',fontsize=fsize)
plt.ylabel(r'$T$',fontsize=fsize)

i1=plt.axes([0.215,0.21,0.25,0.4])
plt.plot(x,Texact[:,0],'k-')
for j in range(ncases):
   plt.plot(x,T[:,j])
plt.xlim((0.0,0.15))
plt.xticks([0,0.05,0.1,0.15])
plt.ylim((0.7105,0.7115))
plt.yticks((0.7105,0.711,0.7115))

i2=plt.axes([0.63,0.20,0.25,0.4])
plt.plot(x,Texact[:,0],'k-')
for j in range(ncases):
   plt.plot(x,T[:,j])
plt.xlim((0.18,0.36))
plt.xticks([0.2,0.25,0.3,0.35])
plt.ylim((1.14,1.145))
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.3f')) 
#plt.ytick((0.7105,0.711,0.7115))

plt.savefig('Tprandtl.pdf')

plt.figure(figsize=(width,height))
plt.plot(x,uexact[:,0],'k-',label='exact')
for j in range(ncases):
   plt.plot(x,u[:,j],label=r'$\mathcal{P}=$'+ipr[j])
plt.legend(loc="upper left")
plt.xlim((-0.25,0.4))
#plt.title(r'Sod shock tube, $p=8, c_E=40, c_{max}=0.3, t=$'+str(times[i]))
plt.xlabel(r'$x$',fontsize=fsize)
plt.ylabel(r'$u$',fontsize=fsize)

mkstr=['-','-','--']
i1=plt.axes([0.42,0.175,0.39,0.5])
plt.plot(x,uexact[:,0],'k-')
for j in range(ncases):
   plt.plot(x,u[:,j],mkstr[j])
plt.xlim((-0.05,0.35))
plt.xticks([0.0,0.1,0.2,0.3])
plt.ylim((0.926,0.93))
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.3f')) 
plt.yticks((0.926,0.927,0.928,0.929,0.93))

plt.savefig('uprandtl.pdf')

# make a function out of this
plt.figure(figsize=(width,height))
plt.plot(x,rhoexact[:,0],'k-',label='exact')
for j in range(ncases):
   plt.plot(x,rho[:,j],label=r'$\mathcal{P}=$'+ipr[j])
plt.legend(loc='lower left',ncol=4)
plt.xlim((-0.1,0.4))
plt.ylim((0.1,0.5))
plt.xlabel(r'$x$',fontsize=fsize)
plt.ylabel(r'$\rho$',fontsize=fsize)

i1=plt.axes([0.215,0.25,0.32,0.45])
plt.plot(x,rhoexact[:,0],'k-')
for j in range(ncases):
   plt.plot(x,rho[:,j])
plt.xlim((0.0,0.15))
plt.xticks([0.0,0.05,0.1,0.15])
plt.ylim((0.4255,0.427))
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.4f')) 
plt.yticks((0.4255,0.426,0.4265,0.427))

i2=plt.axes([0.66,0.5,0.23,0.36])
plt.plot(x,rhoexact[:,0],'k-')
for j in range(ncases):
   plt.plot(x,rho[:,j])
plt.xlim((0.2,0.35))
plt.xticks([0.2,0.25,0.3])
plt.ylim((0.265,0.266))
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.4f')) 
plt.yticks((0.265,0.2655,0.266))
plt.savefig('rhoprandtl.pdf')
