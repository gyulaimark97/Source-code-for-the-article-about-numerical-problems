disp('starting');
for i=1 : 200
    myLU();
    x = sprintf('%f%%.',i/2);
    disp(x)
end
disp('end')