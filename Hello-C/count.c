/*********************************************************************
count.c
use standard I/O
*********************************************************************/
#include <stdio.h>
#include <stdlib.h>  //exit()
//#include <console.h>  //ccommand()

int main(int argc, char *argv[])
{
    int ch;  //temporary storage
    FILE *fp;  //file pointer
    long count = 0;

    if (argc != 2)
    {
        printf ("Usage: %s filename\n",argv[0]);
        exit(1);
    }
    if ((fp = fopen(argv[1], "r")) == NULL)
    {
        printf ("Can't open %s\n", argv[1]);
        exit(1);
    }
    while ((ch = getc(fp)) != EOF)
    {
        putc (ch, stdout);
        count++;
    }
    fclose (fp);
    printf ("\nFile %s has %ld characters\n", argv[1], count);

    //getchar();

    return 0;
}
