#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/*
 * is_palindrome - this function checks if there's some repeated sequence.
 * @**head: this is the top of the node
 * output:1 or 0
 */


int is_palindrome(listint_t **head)
{
	listint_t *ptr = *head;
	int list[];
	int count = 0;

	while (ptr != NULL)
	{
		list[count] = ptr->data;
		count = count + 1
		ptr = ptr->next;
	}

	if (count % 2 != 0)
	{
		return (0);
	}

	int half = (count / 2) - 1
	int result = 1
	int i = 0

	while (i <= half)
	{
		if (some[i] == some[half + i])
		{
			result = 1
			i = i + 1
		}
		else
		{
			free(some);

			return (0);
		}
	}

	free(some);
	return (result);
}
