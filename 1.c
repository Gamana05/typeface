#include <stdio.h>
#include <math.h>
int main()
{
    int n;
    scanf("%d",&n);
    int res=0;
    int t=0;
    while(n>0)
    {
        res+=(n%3)*pow(10,t);
        t+=1;
        n=n/3;
    }
    printf("%d",res);
}