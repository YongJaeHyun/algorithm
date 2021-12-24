#include <stdio.h>

int main(void)
{
    int a,b,c,d,e;
    int size = 0;
    int ans;
    scanf("%d",&a);
    if (a<=9)
    {
        a*=10;
    }
    b = a/10;
    c = a%10;
    d = b+c;
    e = d%10;
    ans = c*10+e;
    size++;
     while(a != ans)
    {
         b = ans/10;
         c = ans%10;
         d = b+c;
         e = d%10;
         ans = c*10+e;
         size++;
    }
    printf("%d",size);
    return 0;
}