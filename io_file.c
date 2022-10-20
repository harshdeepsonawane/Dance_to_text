
#include <stdio.h>
#include <string.h>
#define BUFSIZE 1000

int main(int argc, char *argv[])
{
	printf("there is %d arguments.\n",argc);
	if(argc == 1){
		printf("No Arguments\n");
		return 0;
	}
	for(int i =1;i!=argc;++i)
	{
		printf("%s\n",argv[i]);
	}
	//char in_file[]="read_text.txt";
	char *in_file = argv[1];
	FILE *input_file=fopen(in_file,"r");

	char out_file[25];
	strcpy(out_file,argv[1]);
	strcat(out_file,".out");
	FILE *output_file=fopen(out_file,"w");

	char line[25];
	for(int line_no =1; fgets(line,sizeof(line),input_file) !=NULL;++line_no);{
		//printf("LINE %d: %s",line_no,line);
		//fprintf(output_file,"LINE %d:%s",line_no,line);
		fputs(line,stdout);
		fputs(line, output_file);
	}
	if(input_file)
	{
		fclose(input_file);
		fclose(output_file);
	}
	// getchar();
	return 0;
}
