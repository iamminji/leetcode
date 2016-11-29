/*
Arranging Coins (https://leetcode.com/problems/arranging-coins/)
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
Given n, find the total number of full staircase rows that can be formed.
n is a non-negative integer and fits within the range of a 32-bit signed integer.*/

#include <math.h>
int arrangeCoins(long n) {
    if(n < 2){
    	return n;
    }
    long  k = 1;
    while (k < pow(2, 17)){
    	if((k*k + k) <= 2*n) {
    		k += 1;
    	} else {
    		k -=1;
    		break;
    	}
    }
    return k;
}