#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle
 * @list: pointer to the head of the linked list
 * Return: 0 if no cycle, 1 else
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise = list, *hare = list;

	while (hare && hare->next && tortoise)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}
	return (0);
}
