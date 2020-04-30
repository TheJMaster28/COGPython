set boxwidth 0.9 relative
set style data histograms
set style fill solid 1.0 border -1
binwidth=0.1
bin(x,width)=width*floor(x/width)
set xlabel 'User%'
set ylabel 'Frequency'
String1 = sprintf('dat_files/%s.dat', file)
plot String1 using (bin($4,binwidth)):(1.0) smooth freq with boxes t file 

pause -1
