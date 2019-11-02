function Circumplex_analyze_scores(mydatapath, subjs)

datafile = strcat(mydatapath, 'data_output\');
circumplexfold = [mydatapath 'Circumplex/Circumplex'];
cd(datafile)
fid=fopen('Circumplexallscores.txt','wt');
fprintf(fid,[ 'part,', ' PA, ', ' PD, ', '  UA, ', ' UD, ', ' MEAN_ACTIVATED, ', ' MEAN_DEACTIVATED, ', ' MEAN_PLEASANT, ', ' MEAN_UNPLEASANT ']);
fclose(fid);


cd(circumplexfold)
FileList = dir('*.csv');
N = size(FileList,1);

%% 
%%
%creating loop 
	for N=1:length(subjs)
         cd(circumplexfold)
         subj = subjs(N);
		%  reading the file.
		csvFileName = [ num2str(subj) '.csv'];
        
  
		 if exist(csvFileName, 'file')
			fid = fopen(csvFileName, 'rt');
			textData = fread(fid);

		    excelfile = xlsread(csvFileName);
             parID = excelfile(1,1);
             disp('Circumplex')
            C = excelfile(:,3);
            D = C > 0;
            E = C(D);
           CIRCUMPLEX = E; clear C D E;

           BC = CIRCUMPLEX;	

	%Calculating BIS scores
			PA = mean([BC(9); BC(10); BC(12); BC(17); BC(18); BC(21); BC(27); BC(28); BC(29); BC(31); BC(33); BC(34); BC(41); BC(62); BC(63); BC(69)]);
			PD = mean([BC(4);BC(7);BC(25);BC(26);BC(44);BC(45);BC(46);BC(47);BC(51);BC(56);BC(76)]);
			UA = mean([BC(1);BC(2);BC(3);BC(11);BC(15);BC(20);BC(22);BC(23);BC(24);BC(30);BC(36);BC(42);BC(43);BC(48);BC(64);BC(66)]);
			UD = mean([BC(13);BC(14);BC(16);BC(19);BC(32);BC(49);BC(54);BC(60);BC(65);BC(68);BC(75)]);
			MEAN_ACTIVATED = mean([BC(39); BC(50); BC(52); BC(53); BC(55); BC(57); BC(9); BC(10); BC(12); BC(17); BC(18); BC(21); BC(27); BC(28); BC(29); BC(31); BC(33); BC(34); BC(41); BC(62); BC(63); BC(69); BC(1);BC(2);BC(3);BC(11);BC(15);BC(20);BC(22);BC(23);BC(24);BC(30);BC(36); BC(42);BC(43);BC(48);BC(64);BC(66)]); 
          MEAN_DEACTIVATED = mean([BC(5); BC(35); BC(58); BC(59); BC(70); BC(71);BC(4);BC(7);BC(25);BC(26);BC(44);BC(45);BC(46);BC(47); BC(51);BC(56);BC(76);BC(13);BC(14);BC(16);BC(19);BC(32);BC(49);BC(54);BC(60);BC(65);BC(68);BC(75)]);
          MEAN_PLEASANT = mean([BC(8); BC(37); BC(38); BC(73); BC(74);BC(9); BC(10); BC(12); BC(17); BC(18); BC(21); BC(27); BC(28); BC(29); BC(31); BC(33); BC(34); BC(41); BC(62); BC(63); BC(69);BC(4);BC(7);BC(25);BC(26);BC(44);BC(45);BC(46);BC(47);BC(51);BC(56);BC(76)]);
          MEAN_UNPLEASANT = mean([BC(6); BC(40); BC(61); BC(67); BC(72); BC(77);BC(13);BC(14);BC(16);BC(19);BC(32);BC(49);BC(54);BC(60);BC(65);BC(68);BC(75);BC(1);BC(2);BC(3);BC(11);BC(15);BC(20);BC(22);BC(23);BC(24);BC(30);BC(36);BC(42);BC(43);BC(48);BC(64);BC(66)]);

           A  = [parID, PA, PD, UA, UD, MEAN_ACTIVATED, MEAN_DEACTIVATED, MEAN_PLEASANT, MEAN_UNPLEASANT];
             
			
                
                     
            cd(datafile)
             fid=fopen('Circumplexallscores.txt','at');
            
            
            if N == 1
                fprintf(fid,'\n%d, %.2f, %.2f, %.2f, %.2f, %.2f, %.2f, %.2f, %.2f\n',A);
            else
                fprintf(fid,'%d, %.2f, %.2f, %.2f, %.2f, %.2f, %.2f, %.2f, %.2f\n',A);
            end
            fclose(fid);



% 		else
% 		fprintf('File %s does not exist.\n', csvFileName);
         else
        cd(datafile)
        fprintf('File %s does not exist.\n', csvFileName);
        fid=fopen('Circumplexallscores.txt','at');
        B = [999, 999, 999, 999, 999, 999,999,999,999];
        fprintf(fid,'%d, %d, %d, %d, %d, %d, %d, %d, %d\n',B);
                     end
                        

    end
end
             
   

