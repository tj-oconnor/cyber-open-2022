#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

char *nth_occurrence(const char *s, char c, int n) {
    if (n > 0) {
        s = nth_occurrence(s, c, n-1);
        if (!s) return NULL;
        s++;
    }

    return strchr(s, c);
}

bool before(const char *s, char c1, int n1, char c2, int n2) {
    char *o1 = nth_occurrence(s, c1, n1), *o2 = nth_occurrence(s, c2, n2);
    return o1 && o2 && o1 < o2;
}
