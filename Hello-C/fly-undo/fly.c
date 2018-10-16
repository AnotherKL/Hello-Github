#include<stdio.h>
#include<stdlib.h>
#include<conio.h>

int main(void)
{
    startup();//数据初始化
    while(1)
    {
        show();//显示画面
        updateWithoutInput();//与用户输入无关的更新
        updateWithInput();//与用户有关的更新
    }
}
