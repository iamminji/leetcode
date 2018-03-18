#### 문제 풀이

[Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/)

난이도 **Easy** 구현 문제이다.

굉장히 유명한, 연속적으로 가장 긴 증가하는 부분 수열 길이? 를 리턴하는 문제이다.
easy라서 잉? 스러웠는데, 문제에서 주어진 것이 연속적으로 증가하는 부분만이어야 한다는 것을 보고 납득이 갔다.

```[1,3,5,4,7] 에서 답이 4가 아닌 것 처럼.```

그냥 예전에 풀었던, 방식에서 연속이 아니면 dp라는 배열을 다시 1로 초기화 해주는 형식으로 답을 구했다.
이렇게 안하고 그냥 O(N)번으로 이전 값과 현재 값을 비교해가면서 max값을 할당해주어도 될 것 같기도 하다.
