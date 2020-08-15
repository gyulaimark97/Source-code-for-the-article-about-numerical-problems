function mymult(x)
A1 = rand(x, x);
A2 = rand(x, x);

tic;
A3 = A1*A2;
time = toc;

time;
s1= "result";
file=strcat(s1 + x+ ".txt");

fileID = fopen(file,'a');
fprintf(fileID,'%f\n',time);
fclose(fileID);