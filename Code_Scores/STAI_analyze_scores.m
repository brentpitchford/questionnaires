function STAI_analyze_scores(mydatapath, subjs)

%Counting the # of files in the directory
%%
datafile = strcat(mydatapath, 'data_output\');
STAIfold = [mydatapath 'STAI/STAI'];
cd(datafile)
fid=fopen('STAIallscores.txt','wt');
fprintf(fid,[ 'part', 'STAI_score']);
fclose(fid);

cd(STAIfold)
FileList = dir('*.csv');
N = size(FileList,1);

%%
%creating loop 
	for N=1:length(subjs)
         cd(STAIfold)
         subj = subjs(N);
		%  reading the file.
		csvFileName = [ num2str(subj) '.csv'];
        disp('STAI')
        if exist(csvFileName, 'file')
  
		
			fid = fopen(csvFileName, 'rt');
			textData = fread(fid);

		    excelfile = xlsread(csvFileName);
             parID = excelfile(1,1);
            C = excelfile(:,3);
            D = C > 0;
            E = C(D);
            STAI = E; clear C D E;
            reverserows = [1, 3, 6, 7, 10, 13, 14, 16, 19];
            
            for i = reverserows
         
            STAI(i) = 5 - STAI(i);
            end
            BC = STAI;

            STAI_score = sum(BC);
            
            %%
            %Writing headers  
			A  = [parID, STAI_score];
			
            cd(datafile)
			fid=fopen('STAIallscores.txt','at');
            cd(datafile)
            if N == 1
                fprintf(fid,'\n%d, %d\n',A);
            else
                fprintf(fid,'%d, %d\n',A);
            end
              fclose(fid);


               
        else
             cd(datafile)
            fid=fopen('STAIallscores.txt','at');
           
        fprintf('File %s does not exist.\n', csvFileName);
        B = [999, 999]; 
         fprintf(fid,'%d, %d\n',B);
        
        end
    end
end