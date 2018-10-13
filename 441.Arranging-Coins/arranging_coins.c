/* 441. Arranging Coins */
/* https://leetcode.com/problems/arranging-coins/ */


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