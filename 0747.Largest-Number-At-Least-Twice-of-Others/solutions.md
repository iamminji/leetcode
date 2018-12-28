#### 문제 풀이

[Largest Number At Least Twice of Others](https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/) 라는 문제다
난이도는 **Easy** 이다.

주어진 숫자 리스트에서 가장 큰 값이 나머지 값들의 두배 이상일 떄, 가장 큰 값의 인덱스를 리턴하는 문제다.
나머지 각각 값들의 두 배를 하였을 경우 가장 큰 값 보다 크다면 -1을 리턴한다.

리스트에서 가장 큰 값을 먼저 구해놓고, for loop를 돌면서 * 2 씩 해주어 인덱스 값을 바꿔쳐주었다.

시간 복잡도는 O(n)이고 공간 복잡도는 O(1)이다.

별로 어렵진 않지만, 더 짧게 할 수도 있을 것 같다.