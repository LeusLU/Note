#include<stdio.h>
int main(void)
{
    int seed=0;
    srand(seed);
    for (int i=0;i<50;i++)
    {
        printf("%d\n",rand()%6+1);
    }
    return 0;
}