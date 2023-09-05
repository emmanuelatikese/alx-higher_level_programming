#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert node in ascending order.
 * Return: returns node
 */

listint_t *insert_node(listint_t **head, int number){
    listint_t *ptr = *head;
    listint_t *prev, *next;
    listint_t *current = ptr;
    listint_t tmp;
    tmp->n = number;
    tmp->next = NULL;

    if (ptr == NULL || (ptr->next == NULL && tmp->n < ptr->n)){
        tmp->next = ptr;
        ptr = tmp
        return ptr;
    }
    while(ptr != NULL){
        ptr = ptr->next;
        prev = ptr
        next = ptr->next;

        if (tmp->n <= ptr->n){
            current->next = tmp;
            tmp->next = prev;
            return *head;
        }
        current = prev;
        if(tmp->n > ptr->n){
            prev->next = tmp;
            tmp->next = next;
            return *head;
        }
    }
}