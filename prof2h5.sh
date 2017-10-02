#!/bin/sh
orders="4 8 12 16"
nelms="50 100 200"

for p in $orders
do
   np=`expr $p + 1`
   nxd=`expr 3 \* $p \/ 2`
   for k in $nelms
   do
      dir=N${k}_p$p
      cd $dir
#       grep "<u" *log* > umax
      cp ../prof2h5.py .
      spat='s/Np=[0-9]*/Np='$np'/'
      spat2='s/nxd=[0-9]*/nxd='$nxd'/'
      sed -i -e "'"$spat"'" prof2h5.py
      cd ..
   done
done
