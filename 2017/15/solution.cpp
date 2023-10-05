#include <iostream>
#include <fstream>
#include <sstream>
#include <stdio.h>
using namespace std;

int main() {
    int a_start = 512;
    int b_start = 191;

    int a_factor = 16807;
    int b_factor = 48271;
    int divisor = 2147483647;

    unsigned long a = a_start;
    unsigned long b = b_start;
    unsigned short a_compare;
    unsigned short b_compare;

    int p1 = 0;
    for(int i = 0; i<40000000; i++){
        a = (a * a_factor) % divisor;
        b = (b * b_factor) % divisor;

        a_compare = (unsigned short) a;
        b_compare = (unsigned short) b;

        if (a_compare == b_compare)
            p1++;
    }
    
    printf("There are %d matching pairs\n", p1);

    a = a_start;
    b = b_start;

    int p2 = 0;
    for(int i = 0; i < 5000000; i++){
        do{
            a = (a * a_factor) % divisor;
        }while(a % 4 != 0);
        
        do{
            b = (b * b_factor) % divisor;
        }while(b % 8 != 0);

        a_compare = (unsigned short) a;
        b_compare = (unsigned short) b;
        if(a_compare == b_compare)
            p2++;

    }

    printf("Part 2: there are %d matching pairs\n", p2);



} 