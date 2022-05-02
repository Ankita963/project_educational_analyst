#include <stdio.h>
#include <math.h>
void DiaCircumArea(int r)
{
    printf("\nEnter the radius of circle: ");
    // scanf("%d",&r);
    printf("\nDiameter of circle is %d ",(2*r));
    printf("\nCircumference of circle is %f ",(2*(3.14)*r));
    printf("\nArea of circle is %f ",(3.14)*r*r);
}
int main()
{
    DiaCircumArea(5);
    return 0;
}