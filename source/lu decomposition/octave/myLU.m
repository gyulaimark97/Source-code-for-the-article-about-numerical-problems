function myLU(size)
A = SPDMatrixGenerator(size);
tic
[L,U] = lu(A);
time = toc;

time;
s1= "result";
file=strcat(s1, num2str(size), ".txt");

fileID = fopen(file,'a');
fprintf(fileID,'%f\n',time);
fclose(fileID);