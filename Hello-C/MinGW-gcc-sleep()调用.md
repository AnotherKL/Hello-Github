特别注意:在Codeblocks环境下是无法使用sleep函数的  
因为在windows上Codeblocks采用mingw(Gnu在Window环境下的编译器，可以充分使用WindowsApi)作为编译器，  
而在stdlib.h中sleep的说明如下：_CRTIMP void __cdecl __MINGW_NOTHROW _sleep (unsigned long) __MINGW_ATTRIB_DEPRECATED;  
可以认为mingw舍弃了sleep函数，建议用Sleep实现sleep。  
[处理办法来自reillie的笔记](http://blog.csdn.net/reille/article/details/7027701):  
```c
#if defined(WIN32) || defined(WIN64)  
#include <windows.h>  
#define sleep(n) Sleep(1000 * (n))  
#else  
#include <unistd.h>  
#endif  
```
