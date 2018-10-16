```c  
#include <stdio.h>
#include <unistd.h>
#include <windows.h>

#if defined(WIN32) || defined(WIN64)
#include <windows.h>
#define sleep(n) Sleep(1000 * (n))
#else
#include <unistd.h>
#endif

int main()
{
    for (int i = 0; i<=100; i++)
    {
        printf("\rPercent complete: %d%%",i);
        fflush(stdout);
        sleep(1);
    }
    printf("\n");

}
/*gcc -ggdb -std=c99 -Wall -Werror -Wformat=0 progress2.c  -o progress2*/
```
