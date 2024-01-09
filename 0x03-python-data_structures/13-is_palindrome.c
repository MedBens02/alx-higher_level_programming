#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *tortoise = *head, *hare = *head;
	listint_t *half2, *tmp;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (hare != NULL && hare->next != NULL)
	{
		hare = hare->next->next;
		tmp = tortoise;
		tortoise = tortoise->next;
	}

	if (hare != NULL)
		tortoise = tortoise->next;

	half2 = reverse_listint(&tortoise);

	while (*head != NULL && half2 != NULL)
	{
		if ((*head)->n != half2->n)
			return 0;
		
		*head = (*head)->next;
		half2 = half2->next;
	}

	return 1;
}

/**
 * reverse_listint - Reverses a listint_t linked list.
 * @head: Pointer to the head of the list.
 * Return: A pointer to the first node of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *next = NULL, *ptr = NULL;

	while (*head != NULL)
	{
		next = (*head)->next;
		(*head)->next = ptr;
		ptr = *head;
		*head = next;
	}
	*head = ptr;

	return (*head);
}
