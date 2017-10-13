import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt
import numpy as np
import os
import tables
from mpl_toolkits.axes_grid.inset_locator import(inset_axes,InsetPosition,mark_inset)
from matplotlib.ticker import FormatStrFormatter


mks=['.','x','v','None']
h=[0.02,0.01,0.005]
# one in h, one in p
width=8.5
height=5
fsize=18

#exact=np.loadtxt("e1rpex.out",usecols=(0,2)) # u
exact=np.loadtxt("e1rpex.out",usecols=(0,1)) # rho

p=8
plt.figure()#figsize=(width,height))
main=plt.axes() # FIDELIUM ANIMAE de whoever gave this SANE DEFAULrhoS!!!!
for k,K in enumerate(h):
   case='h'+str(K)+'/p'+str(p).zfill(2)
   zefile=case+'/profiles/prof035000.h5'
   print zefile
   if os.access(zefile,os.F_OK):
      if (os.stat(zefile).st_size>0):
         fid=tables.open_file(zefile,'r')
         prof=fid.root.profiles
         x=fid.root.x.read()
         x=x+0.4
         hdr=prof._v_attrs
         print p-(hdr.nx1-1)

# there has got to be a better way of doing this. dictionary view?
#           if hdr.__contains__('time'):
#              t=hdr.time
      
         param=prof.cmt._v_attrs
         if param.__contains__('isc'):
            ipr=param.isc
         else:
            ipr=1

#        u=prof.cmt.u.read()
         rho=prof.cmt.d.read()
#        mumax=prof.cmt.mumax.read()
#        nus=prof.cmt.artdiff.read()
#        mu=nus/ipr
#        zelab='p ='+str(N)+', t='+t+step+cmax+ce+isc
         zelab='h ='+str(K)
#        main.plot(x,u,label=zelab)
         main.plot(x,rho,label=zelab)
         main.set_xlabel(r'$x$',fontsize=fsize)
#        main.set_ylabel(r'$u$',fontsize=fsize)
         main.set_ylabel(r'$\rho$',fontsize=fsize)
#        main.set_xlim((0.35,1.0)) # need to start storing and
# need to change legend size?
         main.set_xlim((0.35,1.05)) # need to start storing and
         main.set_ylim((0.0,35.0)) # need to start storing and
         fid.close()

main.plot(exact[:,0],exact[:,1],label="exact",ls='--')
#main.legend(loc='lower left') #u
main.legend(loc='upper right') #u

pname='shock2_rho_t35_p'+str(p)+'noinset.pdf'
#pname='shock2_u_t35_p'+str(p)+'noinset.pdf'
plt.savefig(pname)
plt.close()
#plt.show()
