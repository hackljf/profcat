import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
import os
import tables
from mpl_toolkits.axes_grid.inset_locator import(inset_axes,InsetPosition,mark_inset)
from matplotlib.ticker import FormatStrFormatter

#def plotalot(ax,x,y,xlim,ylim,xlabel,ylabel,xticks,yticks,lab,fsize):
def plotalot(ax,x,y,xlim,ylim,xticks=None,yticks=None,lab=None,zecol=None,linestyle='-',markerstyle=None):#,fsize)
   if zecol is not None:
      ax.plot(x,y,label=lab,ls=linestyle,marker=markerstyle,color=zecol)
   else:
      ax.plot(x,y,label=lab,ls=linestyle,marker=markerstyle)
   ax.set_xlim(xlim)
   ax.set_ylim(ylim)
   if xticks is not None:
      ax.set_xticks(xticks)
   if yticks is not None:
      ax.set_yticks(yticks)
#  if xlabel is not None:
#     ax.set_xlabel(r'$x$',fontsize=fsize)
#  if ylabel is not None:
#     ax.set_ylabel(r'$x$',fontsize=fsize)


mks=['.','x','v','None']
lines=[' ','-','-','--','-','-','-','-']
mks=['o',None,None,'.','x',None,None,None]
colors=['red','blue','green','orange','magenta']
width=8.5
height=5
fsize=18

exact=np.loadtxt("../../e1rpex.out",usecols=(0,2)) # u
#exact=np.loadtxt("../../e1rpex.out",usecols=(0,1)) # rho

plt.figure(figsize=(width,height))
main=plt.axes() # FIDELIUM ANIMAE de whoever gave this SANE DEFAULTS!!!!
#i1=plt.axes([0.20,0.2,0.45,0.35]) #rho, contact
#i1=plt.axes([0.3,0.17,0.32,0.22]) #rho, slow-shock
#i2=plt.axes([0.20,0.5,0.25,0.32]) #rho, contact
i1=plt.axes([0.35,0.55,0.5,0.3]) #u

files=['prof035000.h5','smalldt/restart/prof034002.h5']
for i,zefile in enumerate(files):
   print zefile
   if os.access(zefile,os.F_OK):
      if (os.stat(zefile).st_size>0):
         fid=tables.open_file(zefile,'r')
         prof=fid.root.profiles
         x=fid.root.x.read()
         x=x+0.4 # diaphragm
         hdr=prof._v_attrs
#
# there has got to be a better way of doing this. dictionary view?
#           if hdr.__contains__('time'):
#              t=hdr.time
      
         param=prof.cmt._v_attrs
         if param.__contains__('isc'):
            ipr=param.isc
         else:
            ipr=1

         u=prof.cmt.u.read()
         T=prof.cmt.T.read()
         rho=prof.cmt.d.read()
         mumax=prof.cmt.mumax.read()
         nus=prof.cmt.artdiff.read()
         mu=nus/ipr
         plotalot(main,x,u,(0.35,1.05),(-10.0,35.0),lab=zefile,zecol=colors[i])
#        plotalot(main,x,rho,(0.35,1.05),(0.0,35.0),lab=zefile,zecol=colors[i])
         plotalot(i1,x,u,(0.4,0.85),(8.66,8.72),xticks=[0.4,0.5,0.6,0.7,0.8],yticks=[8.66,8.68,8.70,8.72],zecol=colors[i])
#        plotalot(i1,x,rho,(0.4,0.75),(14.2,14.4),xticks=[0.4,0.5,0.6,0.7],yticks=[14.2,14.3,14.4],zecol=colors[i])
#        plotalot(i2,x,rho,(0.7,0.85),(30.9,31.1),xticks=[0.7,0.75,0.8,0.85],yticks=[30.9,31.0,31.1],zecol=colors[i])
         zelab=zefile.split("/")[0]
         main.set_xlabel(r'$x$',fontsize=fsize)
#        main.set_ylabel(r'$\rho$',fontsize=fsize)
         main.set_ylabel(r'$u$',fontsize=fsize)
         fid.close()

main.plot(exact[:,0],exact[:,1],label="exact",ls='--')
i1.plot(exact[:,0],exact[:,1],ls='--')
#i2.plot(exact[:,0],exact[:,1],ls='--')
#main.legend(loc='upper right') #rho
main.legend(loc='lower left') # u

#pname='sod2case.pdf'
#pname='shock2_d_t35_smalldt.pdf'
pname='shock2_u_t35_smalldt.pdf'
plt.savefig(pname)
plt.close()
