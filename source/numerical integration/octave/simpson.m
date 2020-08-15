function res = simpson(d, x, size)
res=0;
for i=1:size-1 
    temp = ((d(x(i+1)) - d(x(i))) /6) * (d(x(i))+4*d((x(i)+x(i+1))/2)+d(x(i+1)));
    res = res + temp;
end