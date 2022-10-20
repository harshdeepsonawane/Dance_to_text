#include<stdio.h>
int main(int argc,char *argv[])
{
	FILE *ptr=NULL;
	
	ptr =fopen("read_text.txt","r");
	/*char c=fgets(ptr);*/
	char str[50];
	fgets(str,40,ptr);
	printf("The containt of the file are-:%s\n",str);
	fclose(ptr);
return 0;
}
