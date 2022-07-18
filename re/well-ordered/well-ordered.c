#include "util.h"

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("Wrong!!\n");
        exit(1);
    }
    size_t l = strlen(argv[1]);    if (l != 40) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], 'm', 0, '4', 0)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], '3', 1, '_', 1)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], '5', 1, '2', 0)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], 'F', 0, '3', 2)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], '_', 3, '1', 1)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], '3', 2, '_', 3)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], '_', 0, '5', 0)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], 'y', 0, '0', 0)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], '0', 2, 'e', 0)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], 'R', 0, '_', 2)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], 'r', 0, '3', 1)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], 'c', 0, '5', 1)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], 's', 0, '_', 4)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], 'k', 0, '3', 0)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], 'a', 0, '8', 0)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], 'N', 0, '_', 5)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], '1', 0, 'F', 0)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], '_', 1, 'y', 0)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], '8', 0, 'c', 0)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], 'R', 1, '_', 6)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], '1', 1, 's', 0)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], 'l', 0, '1', 0)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], '3', 0, '_', 0)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], 'e', 0, 'e', 1)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], '2', 0, '0', 2)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], '0', 1, 'r', 1)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], '_', 5, '0', 1)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], 'd', 0, '3', 3)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], '_', 2, 'l', 0)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], '5', 0, 'U', 0)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], 'i', 0, 'N', 0)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], '_', 6, 'a', 0)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], '0', 0, 'u', 0)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], '3', 3, 'R', 1)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], '4', 0, 'k', 0)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], '_', 4, 'i', 0)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], 'U', 0, 'r', 0)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], 'r', 1, 'd', 0)) {
        printf("Wrong!!\n");
        exit(1);
    }
    if (!before(argv[1], 'u', 0, 'R', 0)) {
        printf("Wrong!!\n");
        exit(1);
    }
    printf("Correct!!\n");}
