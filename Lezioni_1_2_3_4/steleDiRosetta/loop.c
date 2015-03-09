#include <stdio.h>
#include <math.h>
#include <time.h>

int main ()
{
	int NLOOP=100000;
        long p2,p3;
        double sq;
        clock_t start, stop;
        double time_spent;

        printf("Begin loop\n");
        start = clock();
 
	for (int i=0; i<NLOOP; i++){
           p2 = (long) pow((double) i,2);
           p3 = (long) pow((double) i,3);
           sq = sqrt((double) i);
           printf( "%d\t%ld\t%ld\t%5.3lf\n",i,p2,p3,sq); 
        }

        printf("End loop\n");
        stop = clock();
        time_spent = (double)(stop - start) / CLOCKS_PER_SEC;
        printf("Done in %lf seconds\n", time_spent );
   
   return(0);
}
