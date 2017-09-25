from matplotlib import pyplot as plt
import tables
files=["ce45cmax0.5messh/profiles/prof99999.h5",
"p12/ce40cmax1isc0.75/prof350000.h5",
"p12/profiles/prof350000.h5",
"ce60cmax1isc75meshh/prof035000.h5",
"ce60cmax1isc75meshh/oops/prof035000.h5"]
# t<0.035 "ce40cmax0.3meshh/profiles/prof33611.h5",
# t=0.05, not 0.035 "ce40cmax0.5meshh/profiles/prof99999.h5",

plt.figure()
for fname in files:
   fid=tables.open_file(fname,'r')
   g=[];
   for group in fid.walk_groups():
      g.append(group)

   root=g[0]
   prof=root.profiles
   x=root.x.read()

   hdr=prof._v_attrs
   N=hdr.nx1-1

# there has got to be a better way of doing this. dictionary view?
   if hdr.__contains__('time'):
      t='%.2e' % hdr.time
   else:
      t='???'

   param=prof.cmt._v_attrs
   if param.__contains__('CFL'):
      step=', CFL= %.1f' % param.cfl
   elif param.__contains__('dt'):
      step=', $\Delta t$= %.1e' % param.dt
   else:
      step=''
   if param.__contains__('cmax'):
      cmax=', $c_{max}$= %.1e' % param.cmax
   else:
      cmax=''
   if param.__contains__('ce'):
      ce=', $c_{E}$= %.1e' % param.ce
   else:
      ce=''
   if param.__contains__('isc'):
      ipr=param.isc
      isc=', $\mathscr{P}$= %.1e' % ipr
   else:
      isc=''
      ipr=1

   u=prof.cmt.u.read()
   T=prof.cmt.T.read()
   mumax=prof.cmt.mumax.read()
   nus=prof.cmt.artdiff.read()
   mu=nus/ipr

   zelab='N ='+str(N)+', t='+t+step+cmax+ce+isc
   plt.subplot(221)
   plt.plot(x,u,label=zelab)
   plt.subplot(222)
   plt.plot(x,T,label=zelab)
   plt.subplot(223)
   plt.plot(x,mumax,label=zelab)
   plt.subplot(224)
   plt.plot(x,mu,label=zelab)
   fid.close()

plt.legend()
plt.show()
