#ifndef LIST_H
#define LIST_H

#include <stddef.h>
#include <stdlib.h>

#define DECLARE_LIST(name, valtype)                     \
struct name                                             \
{                                                       \
  valtype val;                                          \
  struct name *next;                                    \
};                                                      \
                                                        \
inline struct name *                                    \
name ## _init()                                         \
{                                                       \
  return NULL;                                          \
}                                                       \
                                                        \
struct name *                                           \
name ## _insert_sort(valtype newval, struct name *head) \
{                                                       \
  struct name *newelem = malloc(sizeof(struct name));   \
  newelem->val = newval;                                \
  newelem->next = NULL;                                 \
  if (head == NULL)                                     \
    return newelem;                                     \
  if (newval <= head->val)                              \
  {                                                     \
    newelem->next = head;                               \
    return newelem;                                     \
  }                                                     \
  struct name *cur = head;                              \
  while(cur->next)                                      \
  {                                                     \
    if (newval <= cur->next->val)                       \
    {                                                   \
      newelem->next = cur->next;                        \
      break;                                            \
    }                                                   \
    cur = cur->next;                                    \
  }                                                     \
  cur->next = newelem;                                  \
  return head;                                          \
}                                                       \
                                                        \
void                                                    \
name ## _free(struct name *head)                        \
{                                                       \
  struct name *cur = head;                              \
  while (cur)                                           \
  {                                                     \
    struct name *tofree = cur;                          \
    cur = cur->next;                                    \
    free(tofree);                                       \
  }                                                     \
}

#endif /* !LIST_H */
