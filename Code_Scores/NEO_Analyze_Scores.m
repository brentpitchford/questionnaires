function NEO_Analyze_Scores(mydatapath, subjs)

%Counting the # of files in the directory

datafile = strcat(mydatapath, 'data_output\');
NEOfold = [mydatapath 'NEO Personality/NEO'];
cd(datafile)
fid=fopen('NEOallscores.txt','wt');
fprintf(fid,['part','O,','C,','E,','A,', 'N,']);
fclose(fid);
              


cd(NEOfold)
FileList = dir('*.csv');

%%
%creating loop 
	for N = 1:length(subjs)
         cd(NEOfold)
		%  reading the file.
        subj = subjs(N);
		csvFileName = [ num2str(subj) '.csv'];
        if exist(csvFileName, 'file')
  
		
			fid = fopen(csvFileName, 'rt');
			textData = fread(fid);

		    excelfile = xlsread(csvFileName);
             parID = excelfile(1,1);
             disp('NEO')
            C = excelfile(:,3);
            D = C > 0;
            E = C(D);
            NEO = E; clear C D E;
             reverserows = [2 , 3 , 6 ,  8 ,  10 , 12 , 14 ,  16 ,  18 , 20 , 22 ,  24 ,  26 , 28 , 30 ,  32 ,  34 , 36 , 38 ,  40 ,  42 , 44 , 46 ,  48 ,  50];
           
            for i = reverserows
         
            NEO(i) = 6 - NEO(i);
            end
            BC = NEO;
            
            %Calculating Factor scores
			O = BC(3) + BC(8) + BC (13) + BC (18) + BC(23) + BC(28) + BC(33)+ BC(38) + BC(43)+ BC(48);
			C = BC(5) + BC(10) + BC(15) + BC(20) + BC(25) + BC(30) + BC(35) + BC(40) + BC(45) + BC(50);
			E = BC(2) + BC(7) + BC(12) + BC(17) + BC(22) + BC(27) + BC(32) + BC(37) + BC(42) + BC(47);
			A = BC(4) + BC(9) + BC(14) + BC(19) + BC(24) + BC(29) + BC(34) + BC(39) + BC(44) + BC(49);
			N = BC(1) + BC(6) + BC(11) + BC(16) + BC(21) + BC(26) + BC(31) + BC(36) + BC(41) + BC(46); 

            A  = [parID, O, C, E, A, N];
          
             cd(datafile)
			fid=fopen('NEOallscores.txt','at');
            
            if N == 1
                fprintf(fid,'\n\n%d, %d, %d, %d, %d, %d\n',A);
            else
                fprintf(fid,'\n%d, %d, %d, %d, %d, %d\n',A);
            end
            fclose(fid);



% 		else
% 		fprintf('File %s does not exist.\n', csvFileName);
            
        else
             cd(datafile)
        fprintf('File %s does not exist.\n', csvFileName);
        B = [999, 999, 999, 999, 999, 999];
        fid=fopen('NEOallscores.txt','at');
        fprintf(fid,'%d, %d, %d, %d, %d, %d\n',B);
    end
    end
end