#include<stdio.h>
void write(char fname[],char data[],int size){
FILE *pImage =fopen(fname,"wb");
fwrite(data,1,size,pImage);
fclose(pImage);


int main(){
		char buffer[]={ 255,0,0,
				0,255,255,
				0,0,255,
				255,0,255 };
				
				int size= sizeof(buffer)/sizeof(buffer[0]);
				write("box.ppm",buffer,size);
				system("convert box.ppm box.png");
			return 0;}
				
								
