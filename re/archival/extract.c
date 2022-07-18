#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

typedef struct fblk_t {
    char *name;
    char *data;
    int length;
} fblk_t;

#define INLINE static inline __attribute__((always_inline))

INLINE char *read_file(char *fname, long *sz) {
    FILE *fp = fopen(fname, "rb");

    if (!fp) return NULL;

    fseek(fp, 0L, SEEK_END);
    *sz = ftell(fp);
    rewind(fp);

    char *buff = malloc(*sz);

    if (!buff) {
        fclose(fp);
        return NULL;
    }

    if (fread(buff, 1, *sz, fp) != (size_t) *sz) {
        fclose(fp);
        return NULL;
    }

    fclose(fp);
    return buff;
}

INLINE int parse_fblk(char *buff, long sz, int off, fblk_t *out) {
    if (off >= sz) return -1;

    char *blk = buff + off;
    int bsz = *(int *) blk;

    if (bsz + off > sz) return -1;

    char k1 = blk[4], k2 = blk[5];
    char *name = blk + 6;
    int namelen = (int) strnlen(name, bsz-6);
    if (namelen >= bsz-6) return -1;

    for (int i = namelen + 7; i < bsz; i += 2) {
        if (i+1 < bsz) {
            char tmp = blk[i];
            blk[i] = blk[i+1] ^ k1;
            blk[i+1] = tmp ^ k2;
        } else {
            blk[i] ^= k1;
        }
    }

    out->name = name;
    out->data = name + namelen + 1;
    out->length = bsz - namelen - 7;

    return 0;
}

int main(int argc, char **argv) {
    if (argc < 3) {
        printf("Usage: %s <archive> <output directory>\n", argv[0]);
        return 1;
    }

    long sz = 0;
    char *buff = read_file(argv[1], &sz);

    if (!buff) {
        puts("Error reading file");
        return 1;
    }

    if (sz < 4) {
        puts("Error parsing file");
        free(buff);
        return 1;
    }

    int filecnt = *(int *) buff;
    int *fileoffs = ((int *) buff) + 1;

    if (filecnt * 4 + 4 > sz) {
        puts("Error parsing file");
        free(buff);
        return 1;
    }

    if (chdir(argv[2])) {
        puts("Error changing directory");
        free(buff);
        return 1;
    }

    for (int i = 0; i < filecnt; i++) {
        fblk_t blk;
        if (parse_fblk(buff, sz, fileoffs[i], &blk)) {
            puts("Error parsing file");
            free(buff);
            return 1;
        }

        FILE *fp = fopen(blk.name, "wb");

        if (!fp) {
            puts("Error opening output file");
            free(buff);
            return 1;
        }

        if (fwrite(blk.data, 1, blk.length, fp) != (size_t) blk.length) {
            puts("Error writing output file");
            free(buff);
            return 1;
        }

        fclose(fp);
    }

    free(buff);
}
