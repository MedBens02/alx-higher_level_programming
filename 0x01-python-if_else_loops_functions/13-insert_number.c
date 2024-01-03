#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a nbr into a sorted singly linked list
 * @head: ptr to ptr of the head of the list
 * @number: the nbr to be inserted
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (node == NULL || new->n < node->n)
	{
		new->next = node;
		return (*head = new);
	}
	while (node != NULL)
	{
		if (node->next == NULL || new->n < node->next->n)
		{
			new->next = node->next;
			node->next = new;
			return (node);
		}
		node = node->next;
	}
	return (NULL);
}
