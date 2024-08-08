// junk library that can use to add two numbers
#include <stdio.h>
#include <stdlib.h>

int *add(int* a, int *b)
{
    int* ptr = (int*)malloc(sizeof(int));
    if (ptr != NULL)
    {
        *ptr = *a+*b;
    }
    return ptr;
}