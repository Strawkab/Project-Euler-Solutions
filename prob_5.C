#include <stdio.h>

int numberFinder(int max_divisor) {
    int dividend = 1;
    while (1) {
        int is_divisible = 1;
        for (int i = 2; i < max_divisor; i++) {
            if (dividend % i != 0) {
                is_divisible = 0;
                break;
            }
        }
        if (is_divisible) {
            return dividend;
        }
        dividend++;
        printf("%d\n", dividend);
    }
}

int main() {
    printf("%d\n", numberFinder(10));
    return 0;
}
