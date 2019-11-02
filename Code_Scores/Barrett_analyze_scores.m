function Barrett_analyze_scores(mydatapath, subjs)

datafile = strcat(mydatapath, 'data\');
barrettfold = [mydatapath 'Barret''s Impulsivity/Barretsimpuls'];
cd(datafile)
fid=fopen('Barrettallscores.txt','wt');
fprintf(fid,[ 'part', ' A_attention_score, ', ' A_cognitive_score, ', '  M_motor_score, ', ' M_perseverence_score, ', ' N_self_control_score, ', ' N_cognitive_score, ', ' Attention_score, ', ' Motor_score, ', ' Self_control_score, ', ' BIS_total ']);
fclose(fid);
              


cd(barrettfold)
FileList = dir('*.csv');

%%
%creating loop 
	for N = 1:length(subjs)
         cd(barrettfold)
		%  reading the file.
        subj = subjs(N);
		csvFileName = [ num2str(subj) '_Barretsimpuls.csv'];
        if exist(csvFileName, 'file')
  
		
			fid = fopen(csvFileName, 'rt');
			textData = fread(fid);

		    excelfile = xlsread(csvFileName);
             parID = excelfile(1,1);
             disp('Barrett')
            C = excelfile(:,3);
            D = C > 0;
            E = C(D);
            BARRETT = E; clear C D E;
    
            reverserows = [1, 7, 8, 9, 10, 11, 12, 13, 15, 20, 29, 30];
            for i = reverserows
         
            BARRETT(i) = 5 - BARRETT(i);
            end
            BC = BARRETT;	


			%Calculating BIS scores
			A_attention_score = BC(5) + BC(9) + BC (11) + BC (20) + BC(28); 
			A_cognitive_score = BC(6) + BC(24) + BC(26);
			M_motor_score = BC(2) + BC(3) + BC(4) + BC(17) + BC(19) + BC(22) + BC(25);
			M_perseverence_score = BC(16) + BC(21) + BC(23) + BC(30);
			N_self_control_score = BC(1) + BC(7) + BC(8) + BC(12) + BC(13) + BC(14);
      N_cognitive_score = BC(10) + BC(15) + BC(18) + BC(27) + BC(29); 
      Attention_score = A_attention_score + A_cognitive_score;
      Motor_score = M_motor_score + M_perseverence_score;
      Self_control_score = N_self_control_score + N_cognitive_score;
      BIS_total = Attention_score + Motor_score + Self_control_score;

			%Writing headers  
			A  = [parID, A_attention_score, A_cognitive_score, M_motor_score, M_perseverence_score, N_self_control_score, N_cognitive_score, Attention_score, Motor_score, Self_control_score, BIS_total];
		
            cd(datafile)
			fid=fopen('Barrettallscores.txt','at');
            
            if N == 1
                fprintf(fid,'\n%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d\n',A);
            else
                fprintf(fid,'%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d\n',A);
            end
            fclose(fid);



% 		else
% 		fprintf('File %s does not exist.\n', csvFileName);
            
        else
             cd(datafile)
        fprintf('File %s does not exist.\n', csvFileName);
        fid=fopen('Barrettallscores.txt','at');
        B = [999, 999, 999, 999, 999, 999, 999, 999, 999. 999, 999]
        fprintf(fid,'%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d\n',B);
    end
    end
end