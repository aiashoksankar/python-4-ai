data a;
input name $ sno;
datalines;
a 1
b 2
;
run;
proc print data=a;
run;
