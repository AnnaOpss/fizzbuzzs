#include <stdio.h>
#define MAX 100
int main (int argc, char* argv[])
{
	int i;
	for (i=1; i<=MAX; i++) {
		if (i%3 == 0 && i%5==0)
			printf ("FizzBuzz\n");
		else
			if (i%3 == 0)
				printf ("Fizz\n");
			else
				if (i%5 == 0)
					printf ("Buzz\n");
				else
					printf ("%d\n", i);
	}
	return 0;
}