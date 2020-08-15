function int()
times =[0, 0, 0, 0];

x = 0:0.1:100; 
length=1001;
int1=0;
int2=0;
int3=0;
int4=0;

    tic;
    for j=1:length-1 
        temp = (((x(j+1)) - (x(j))) /6) * (f(x(j))+4*f((x(j)+x(j+1))/2)+f(x(j+1)));
        int1 = int1 + temp;
    end
    times(1) = toc;
    
    tic;
    for j=1:length-1 
        temp = (((x(j+1)) - (x(j))) /6) * (g(x(j))+4*g((x(j)+x(j+1))/2)+g(x(j+1)));
        int2 = int2 + temp;
    end
    times(2) = toc;
    
    tic;
    for j=1:length-1 
        temp = (((x(j+1)) - (x(j))) /6) * (h(x(j))+4*h((x(j)+x(j+1))/2)+h(x(j+1)));
        int3 = int3 + temp;
    end
    times(3) = toc;
    
    tic;
    for j=1:length-1 
        temp = (((x(j+1)) - (x(j))) /6) * (t(x(j))+4*t((x(j)+x(j+1))/2)+t(x(j+1)));
        int4 = int4 + temp;
    end
    times(4) = toc;

file="result.csv";

fileID = fopen(file,'a');
for i = 1 : 4
    fprintf(fileID,'%f;',times(i));
end
fprintf(fileID,'\n');
fclose(fileID);