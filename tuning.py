from matplotlib import pyplot as plt
import tables
files=["ce40cmax0.3meshh/profiles/prof33611.h5",
"ce40cmax0.5meshh/profiles/prof99999.h5",
"ce45cmax0.5messh/profiles/prof99999.h5",
"p12/ce40cmax1isc0.75/prof350000.h5",
"p12/profiles/prof350000.h5",
"ce60cmax1isc75meshh/profiles/prof035000.h5"]

plt.figure()
for fname in files:
   fid=tables.open_file(fname,'r')
   g=[];
   for group in fid.walk_groups():
      g.append(group)
   profiles=g[0].profiles
   x=g[0].x.read()
   hdr=profiles._v_attrs
   u=profiles.cmt.u.read()
   T=profiles.cmt.T.read()
   plt.plot(x,u)

plt.show()
