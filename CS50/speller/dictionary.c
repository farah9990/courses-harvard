// Implements a dictionary's functionality

#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <strings.h>
#include <stdbool.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
int dictsize = 0 ;
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int value = hash(word);
    node *p = table[value];
    while (p != NULL)
    {
        if (strcasecmp(word, p-> word) == 0)
        {
            return true ;
        }
        p = p->next ;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    unsigned long hash = 5381 ;
    int letter ;
    while ((letter = tolower(*word++)))
    {
        hash = ((hash << 5) + hash) + letter ;
    }
    return hash % N ;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *dictfile = fopen(dictionary, "r");
    if (dictfile == NULL) // check for errors
    {
        return false;
    }
    char word[LENGTH + 1];
    while (fscanf(dictfile, "%s", word) != EOF) // scan until we hit EOF
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }
        strcpy(n->word, word);
        int value = hash(word);
        n->next = table[value];
        table[value] = n;
        dictsize++;
    }
    fclose(dictfile);

    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    if (dictsize > 0)
    {
        return dictsize ;
    }
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++) // iterate through buckets
    {
        node *p = table[i];

        while (p != NULL)
        {
            node *tmp = p;
            p = p->next;
            free(tmp);
        }

        if (p == NULL && i == N - 1) // check if the last node is null
        {
            return true;
        }
    }

    return false;
}
