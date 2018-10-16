```c  
//按要求输入大写字母打印成金字塔形式  
#include <stdio.h>

int main(void)
{
    char ch;
    char row,blank1,sd,jd,blank2;

    printf("please enter a capital letter: ");
    scanf("%c",&ch);

    for (row = 'A'; row <= ch; row++)
    {
        for(blank1 = row; blank1 < ch; blank1++)
            printf(" ");
        for(sd = 'A'; sd <= row; sd++)
            printf("%c",sd);
        for(jd = sd-2; jd >= 'A'; jd--)
            printf("%c",jd);
        for(blank2 = row; blank2 < ch; blank2++ )  //This for loop can be deleted.
            printf(" ");
        printf("\n");
    }
    return 0;
}  
```
