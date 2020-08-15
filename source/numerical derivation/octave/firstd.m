function res = firstd(d, x, step)
    res = (d(x + step) - d(x - step))/(2*step); 
end