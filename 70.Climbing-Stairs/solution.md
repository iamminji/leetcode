#### 문제 풀이

[Climbing Stairs](https://leetcode.com/problems/climbing-stairs/description/) 라는 문제다
난이도는 **Easy** 이다.

계단 오르는 방법이 몇가지가 있는지 리턴하는 문제로, 계단을 오르는 방법은 1step과 2step 두 가지가 있다. 

전형적인 DP 문제로, 오르는 방법이 두 가지 밖에 없기 때문에 쉽게 풀 수 있는 문제다.

계단이 총 3개라면, 오르는 방법은 계단이 2개 일때와 계단이 1개일 때의 방법 수를 더 해주면 되는데, 그것이 가능한 이유는
계단이 2개 일때 방법에 1step 씩 더 해주면 3개가 되고, 1개 일때는 2step 을 더해 주면 되기 때문이다.

이를 풀어 쓰면


계단이 1개 일 때는
- 1step

계단이 2개 일 때는 
- 1step + 1step
- 2step

이라고 보면 3개 일때는
- 1step (1개 일 때) + 2step
- 1step + 1step (2개 일 때) + 1step
- 2step (2개 일 때) + 2step

이라는 의미이다.

식으로 풀어보면 다음과 같다.

<pre>
dp[i] = dp[i-1] + dp[i-2]
</pre>

시간 복잡도는 O(n)이고 공간 복잡도도 O(n)인 DP 문제였다.
