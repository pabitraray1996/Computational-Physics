#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define N 10000

int main() {
    double lambda = 2.0; // Mean = 0.5, lambda = 2
    double exp_numbers[N];
    FILE *fptr;

    // Initialize random number generator
    srand(time(NULL));

    // Generate exponential random numbers
    for (int i = 0; i < N; i++) {
        double u = rand() / (RAND_MAX + 1.0);
        exp_numbers[i] = -log(1 - u) / lambda;
    }

    // Write the numbers to a file
    fptr = fopen("exp_numbers.txt", "w");
    if (fptr == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    for (int i = 0; i < N; i++) {
        fprintf(fptr, "%f\n", exp_numbers[i]);
    }
    fclose(fptr);

    printf("Exponential random numbers generated and saved to exp_numbers.txt\n");

    return 0;
}