#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: points to the start of the list
 * @number: the number to insert
 * Return: the address of the new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *iterator, *add_node;

	add_node = malloc(sizeof(listint_t));

	if (add_node == NULL)
	{
		return (NULL);
	}
	add_node->n = number;
	iterator = *head;

	if (iterator->n >= number || iterator == NULL)
	{
		add_node->next = iterator;
		*head = add_node;
		return (add_node);
	}

	while (iterator && iterator->next && iterator->next->n < number)
	{
		iterator = iterator->next;
	}
	add_node->next = iterator->next;
	iterator->next = add_node;
	return (add_node);

}
