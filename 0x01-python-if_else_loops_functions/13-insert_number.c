#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert node in ascending order.
 * Return: returns node
 */

listint_t *insert_node(listint_t **head, int number){
    listint_t *ptr = head, *tmp = malloc(sizeof(listint_t));
    listint_t *prev, *next;
    tmp->n = number;
    tmp->next = NULL;
    
    if (ptr == NULL){
        head = tmp
        return head;
    }
    else if (head->next == NULL &&  tmp->n <= head->n){
        tmp->next = head;
        head = tmp;
        return head;
    }

    while(ptr != NULL){
        
        prev = ptr;
        next = ptr->next;
        if(tmp->n <= ptr){
            tmp->next = ptr

        }
    }
}