#include <stdio.h>
#define MAX 100
int main (int argc, char* argv[])
{
	int i;
	for (i=1; i<=MAX; i++) {
		if (i%3 == 0)
			printf("Fizz");
		if (i%5 == 0)
			printf("Buzz");
		if (i%5 != 0 && i%3 != 0)
			printf("%d", i);
		printf("\n");
	}
	return 0;
}
