#include <stdio.h>

#include "list.h"

DECLARE_LIST(div_list, unsigned char)

struct div_list *
get_factors(unsigned long long n)
{
  struct div_list *factors = div_list_init();
#define TRY_MOD(mod)                              \
  while (n % mod == 0)                            \
  {                                               \
    factors = div_list_insert_sort(mod, factors); \
    n /= mod;                                     \
  }
  TRY_MOD(9)
  TRY_MOD(8)
  TRY_MOD(7)
  TRY_MOD(6)
  TRY_MOD(5)
  TRY_MOD(4)
  TRY_MOD(3)
  TRY_MOD(2)
  if (n == 1) // All factors found
    return factors;
  // Some factors are >= 10, cannot represent n as a product of digits
  div_list_free(factors);
  return NULL;
}

int main(int argc, const char *argv[])
{
  if (argc == 1)
    return 1;
  struct div_list *factors = get_factors(atoll(argv[1]));
  for (struct div_list *cur = factors; cur; cur = cur->next)
    printf("%hhu\n", cur->val);
  div_list_free(factors);
  return 0;
}
