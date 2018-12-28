#### 문제 풀이

[Counting Bits](https://leetcode.com/problems/counting-bits/description/)
라는 문제다.

난이도는 **Easy** 이지만,
O(n*sizeof(integer)) 로 하면 너무 쉬우니 O(n)으로 하는 조건이 붙었다.

다시 말하면, bit를 counting 하지 말고 풀라는 문제였다.

예전에 다른 문제에서 power of 2가 맞는지에 대하여 풀었던 경험이 있어서,
<pre> n & (n - 1) </pre> 공식을 통하여 해당 값이 0 이면 power of 2라는 의미이니 이럴 경우
비트는 무조건 1이라고 생각했다.

그리고 이에 해당하지 않는 수는 다른 수의 비트와 합산한 수이니 그에 해당하는 연산도 분기문에 추가하였다.

(7 & 6은 6이고 7은 결국 6 + 1 이면서 해당 값의 비트와 동일하기 때문)