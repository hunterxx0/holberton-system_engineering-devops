#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - infinite loop
 * Return: (0)
 */

int infinite_while(void)
{
	while (1)
		sleep(1);
	return (0);
}

/**
 * main - 5 Zombies
 * Return: (0)
 */

int main(void)
{
	int pid = 0, i = 1;

	while (i <= 5)
	{
		pid = fork();
		if (pid > 0)
			sleep(0);
		else
		{
			printf("Zombie process created, PID: %d\n", getpid());
				exit(0);
		}
		i++;
	}
	infinite_while();
	return (0);
}
