#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/*
check_cycle: this  function takes a linked list of data type int
ouput: it checked whether a function is a cycle by returning 1 or not by returning 0.
 */

int check_cycle(listint_t *list){
    listint_t *ptr, *shead;
    ptr = list;

    shead = ptr;
    while(ptr != NULL){
        ptr = ptr->next;
        if(shead == ptr){
            return (1);
        }
    }
    return (0);
}