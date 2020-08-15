function res = secondd(d, x, step)
    res = (d(x + step) - 2*d(x) + d(x-step))/(step^2); 
end