function Self_cont_analyze_scores(mydatapath,subjs)

%Counting the # of files in the directory

datafile = [mydatapath 'data\'];
selfcontfold = [mydatapath 'Self-Control Scale/SelfCont'];
cd(datafile)
fid=fopen('Selfcontallscores.txt','wt');
fprintf(fid,[ 'part, ', 'Selfcon_score']);
fclose(fid);

cd(selfcontfold)
FileList = dir('*.csv');


for N=1:length(subjs)
         cd(selfcontfold)
         subj = subjs(N);
		%  reading the file.
		csvFileName = [ num2str(subj) '_SelfCont.csv'];
        if exist(csvFileName, 'file')
  
		
			fid = fopen(csvFileName, 'rt');
			textData = fread(fid);

	excelfile = xlsread(csvFileName);
            C = excelfile(:,3);
            D = C > 0;
            E = C(D);
            

		   excelfile = xlsread(csvFileName);
             parID = excelfile(1,1);
             disp('SelfCon')
            C = excelfile(:,3);
            D = C > 0;
            E = C(D);
            SELFCONT = E; clear C D E;
              
         reverserows = [2, 3, 4, 6, 8, 9, 10, 11, 12, 14, 16, 17, 19, 20, 21, 23, 25, 28, 29, 31, 32, 33, 34, 35];
         for i = reverserows
         
            SELFCONT(i) = 6 - SELFCONT(i);
         end
            BC = SELFCONT;	
            
            Selfcon_score = sum(BC);
            A  = [parID, Selfcon_score];
             
            cd(datafile)
            fid=fopen('Selfcontallscores.txt','at');
            cd(datafile)
            if N == 1
                fprintf(fid,'\n%d, %d\n',A);
            else
                fprintf(fid,'%d, %d\n',A);
            end
            fclose(fid);

        else
        cd(datafile)
        fid=fopen('Selfcontallscores.txt','at');
		fprintf('File %s does not exist.\n', csvFileName);
        B  = [999, 999];
         fprintf(fid,'%d, %d\n',B);
        end
end
end