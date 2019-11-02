function Bisbas_analyze_scores(mydatapath, subjs)

datafile = strcat(mydatapath, 'data\');
BISBASfold = [mydatapath 'BIS BAS/BISBAS'];
cd(datafile)
fid=fopen('BisBasallscores.txt','wt');
fprintf(fid,[ 'part,', ' bis,', ' basf,', 'basd,', 'basr,', 'bast']);
fclose(fid);
              


cd(BISBASfold)
FileList = dir('*.csv');


fid=fopen('BisBasallscores.txt','wt');
fprintf(fid,[ 'part,', ' bis,', ' basf,', ' basd,', ' basr, ', ' bast' ]);
fclose(fid);
      %%
%creating loop 
	for N=1:length(subjs)
		%  reading the file.
        subj = subjs(N);
        cd(BISBASfold)
		csvFileName = [ num2str(subj) '_BISBAS.csv'];
		if exist(csvFileName, 'file')
			fid = fopen(csvFileName, 'rt');
			textData = fread(fid);

		
			
            excelfile = xlsread(csvFileName);
            parID = excelfile(1,1);
             disp('BISBAS')
            C = excelfile(:,3);
            D = C > 0;
            E = C(D);
            BISBAS = E; clear C D E;

             reverserows = [5,7];
            for i = reverserows
         
            BISBAS(i) = 5 - BISBAS(i);
            end
            BC = BISBAS;	

      
      

			%Calculating Bis and BAS scores
			Bis_score = BC(1) + BC(3) + BC (5) + BC (7) + BC(10) + BC(14) + BC(19);
			Bas_r_score = BC(4) + BC(8) + BC(11) + BC(12) + BC(18);
			Bas_d_score = BC(2) + BC(13) + BC(15) + BC(17);
			Bas_f_score = BC(6) + BC(9) + BC(16) + BC(20);
			Bas_t_score=Bas_d_score + Bas_f_score + Bas_r_score;


			A  = [parID, Bis_score, Bas_f_score, Bas_d_score, Bas_r_score, Bas_t_score];
            
            cd(datafile)
             fid=fopen('BisBasallscores.txt','at');
			 if N == 1
                fprintf(fid,'\n%d, %d, %d, %d, %d, %d\n',A);
            else
                fprintf(fid,'%d, %d, %d, %d, %d, %d\n',A);
            end
            fclose(fid);



        else
             cd(datafile)
		fprintf('File %s does not exist.\n', csvFileName);
        B = [999, 999, 999, 999, 999, 999];
        fid=fopen('BisBasallscores.txt','at');
        fprintf(fid,'%d, %d, %d, %d, %d, %d\n',B);
        end
    end
end