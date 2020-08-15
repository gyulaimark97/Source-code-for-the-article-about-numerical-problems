function mysum(x)
A1 = rand(x, x);
A2 = rand(x, x);

tic;
A3 = A1+A2;
time = toc;

s1= "result";
file=strcat(s1, mat2str(x), ".txt");
fileID = fopen(file,'a');
fprintf(fileID,'%f\n',time);
fclose(fileID);