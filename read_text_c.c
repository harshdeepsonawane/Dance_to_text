#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc,char*argv[])
{
    FILE* ptr;
   int ch;
    ptr = fopen("read_text.txt", "r+");
 
    if (NULL == ptr) {
        printf("file can't be opened \n");
    }
 	printf("Content of this file are \n");
    do {
        ch = fgetc(ptr);
        printf("%c", ch);
    } while (ch != EOF);
    fclose(ptr);
    return 0;
}
