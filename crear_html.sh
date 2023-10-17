
for j in ??_*
do 
  cd $j; 
  for i in $(ls *ipynb | grep -v SOL | grep -v Eje); 
  do 
    jupyter nbconvert --to html $i
  done
  cd ..
done


