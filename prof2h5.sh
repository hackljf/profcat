#!/bin/sh
orders="4 8 12 16"
nelms="50 100 200"
prof2h5src="/home/local/UFAD/jason.hackl/Work/run_nek_examples/shocktube/data4paper/sod_profiles_logs/prof2h5.py"

for p in $orders
do
   np=`expr $p + 1`
   nxd=`expr 3 \* $p \/ 2`
   for k in $nelms
   do
      dir=N${k}_p$p
      cd $dir
#       grep "<u" *log* > umax
      cp $prof2h5src .
      spat='s/Np=[0-9]*/Np='$np'/'
      spat2='s/nxd=[0-9]*/nxd='$nxd'/'
      sed -i -e $spat -e $spat2 prof2h5.py
      cd ..
   done
done
