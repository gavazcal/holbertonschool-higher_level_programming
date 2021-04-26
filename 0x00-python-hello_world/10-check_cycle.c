#include "lists.h"
/**
 * check_cycle - checks for a cycle in a linked list
 * @list: the list
 * Return: 0 if no cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *hare = list;
	listint_t *tortoise = list;

	while ((hare != NULL) && (tortoise != NULL) && (hare->next != NULL))
	{
		tortoise = tortoise->next;
		hare = hare->next->next;

		if (tortoise == hare)
		{
			return (1);
		}
	}
	return (0);
}
