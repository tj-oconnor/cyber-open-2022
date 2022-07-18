#include <assert.h>

#include "util.h"

#define GTESTCASE(s, c, n, exp) assert(nth_occurrence((s), (c), (n)) == (exp))
#define NTESTCASE(s, c, n) GTESTCASE(s, c, n, NULL)
#define TESTCASE(s, c, n, ind) GTESTCASE(s, c, n, s+ind)

#define NTESTLOOP(s, c, nstart) for (int i = nstart; i < 255; i++) NTESTCASE(s, c, i)

int main() {
    char *test1 = "The quick brown fox jumped over the lazy dog.";

    TESTCASE(test1, 'T', 0, 0);
    TESTCASE(test1, 'h', 0, 1);
    TESTCASE(test1, 'e', 0, 2);
    TESTCASE(test1, ' ', 0, 3);
    TESTCASE(test1, 'q', 0, 4);
    TESTCASE(test1, 'u', 0, 5);
    TESTCASE(test1, 'i', 0, 6);
    TESTCASE(test1, 'c', 0, 7);
    TESTCASE(test1, 'k', 0, 8);
    TESTCASE(test1, ' ', 1, 9);
    TESTCASE(test1, 'b', 0, 10);
    TESTCASE(test1, 'r', 0, 11);
    TESTCASE(test1, 'o', 0, 12);
    TESTCASE(test1, 'w', 0, 13);
    TESTCASE(test1, 'n', 0, 14);
    TESTCASE(test1, ' ', 2, 15);
    TESTCASE(test1, 'f', 0, 16);
    TESTCASE(test1, 'o', 1, 17);
    TESTCASE(test1, 'x', 0, 18);
    TESTCASE(test1, ' ', 3, 19);
    TESTCASE(test1, 'j', 0, 20);
    TESTCASE(test1, 'u', 1, 21);
    TESTCASE(test1, 'm', 0, 22);
    TESTCASE(test1, 'p', 0, 23);
    TESTCASE(test1, 'e', 1, 24);
    TESTCASE(test1, 'd', 0, 25);
    TESTCASE(test1, ' ', 4, 26);
    TESTCASE(test1, 'o', 2, 27);
    TESTCASE(test1, 'v', 0, 28);
    TESTCASE(test1, 'e', 2, 29);
    TESTCASE(test1, 'r', 1, 30);
    TESTCASE(test1, ' ', 5, 31);
    TESTCASE(test1, 't', 0, 32);
    TESTCASE(test1, 'h', 1, 33);
    TESTCASE(test1, 'e', 3, 34);
    TESTCASE(test1, ' ', 6, 35);
    TESTCASE(test1, 'l', 0, 36);
    TESTCASE(test1, 'a', 0, 37);
    TESTCASE(test1, 'z', 0, 38);
    TESTCASE(test1, 'y', 0, 39);
    TESTCASE(test1, ' ', 7, 40);
    TESTCASE(test1, 'd', 1, 41);
    TESTCASE(test1, 'o', 3, 42);
    TESTCASE(test1, 'g', 0, 43);
    TESTCASE(test1, '.', 0, 44);

    NTESTLOOP(test1, '0', 0);
    NTESTLOOP(test1, '1', 0);
    NTESTLOOP(test1, '2', 0);
    NTESTLOOP(test1, '3', 0);
    NTESTLOOP(test1, '4', 0);
    NTESTLOOP(test1, '5', 0);
    NTESTLOOP(test1, '6', 0);
    NTESTLOOP(test1, '7', 0);
    NTESTLOOP(test1, '8', 0);
    NTESTLOOP(test1, '9', 0);

    NTESTLOOP(test1, 'A', 0);
    NTESTLOOP(test1, 'B', 0);
    NTESTLOOP(test1, 'C', 0);
    NTESTLOOP(test1, 'D', 0);
    NTESTLOOP(test1, 'E', 0);
    NTESTLOOP(test1, 'F', 0);
    NTESTLOOP(test1, 'G', 0);
    NTESTLOOP(test1, 'H', 0);
    NTESTLOOP(test1, 'I', 0);
    NTESTLOOP(test1, 'J', 0);
    NTESTLOOP(test1, 'K', 0);
    NTESTLOOP(test1, 'L', 0);
    NTESTLOOP(test1, 'M', 0);
    NTESTLOOP(test1, 'N', 0);
    NTESTLOOP(test1, 'O', 0);
    NTESTLOOP(test1, 'P', 0);
    NTESTLOOP(test1, 'Q', 0);
    NTESTLOOP(test1, 'R', 0);
    NTESTLOOP(test1, 'S', 0);
    NTESTLOOP(test1, 'T', 1);
    NTESTLOOP(test1, 'U', 0);
    NTESTLOOP(test1, 'V', 0);
    NTESTLOOP(test1, 'W', 0);
    NTESTLOOP(test1, 'X', 0);
    NTESTLOOP(test1, 'Y', 0);
    NTESTLOOP(test1, 'Z', 0);

    NTESTLOOP(test1, 'a', 1);
    NTESTLOOP(test1, 'b', 1);
    NTESTLOOP(test1, 'c', 1);
    NTESTLOOP(test1, 'd', 2);
    NTESTLOOP(test1, 'e', 4);
    NTESTLOOP(test1, 'f', 1);
    NTESTLOOP(test1, 'g', 1);
    NTESTLOOP(test1, 'h', 2);
    NTESTLOOP(test1, 'i', 1);
    NTESTLOOP(test1, 'j', 1);
    NTESTLOOP(test1, 'k', 1);
    NTESTLOOP(test1, 'l', 1);
    NTESTLOOP(test1, 'm', 1);
    NTESTLOOP(test1, 'n', 1);
    NTESTLOOP(test1, 'o', 4);
    NTESTLOOP(test1, 'p', 1);
    NTESTLOOP(test1, 'q', 1);
    NTESTLOOP(test1, 'r', 2);
    NTESTLOOP(test1, 's', 0);
    NTESTLOOP(test1, 't', 1);
    NTESTLOOP(test1, 'u', 2);
    NTESTLOOP(test1, 'v', 1);
    NTESTLOOP(test1, 'w', 1);
    NTESTLOOP(test1, 'x', 1);
    NTESTLOOP(test1, 'y', 1);
    NTESTLOOP(test1, 'z', 1);

    NTESTLOOP(test1, '.', 1);
    NTESTLOOP(test1, ' ', 8);

    puts("All OK");
}
