#### 문제 풀이

[Shortest Unsorted Continuous Subarray](https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/) 라는 문제다
난이도는 **Easy** 이지만 예외가 있어서, 꽤 틀렸다

주어진 배열을 오름차순으로 정렬하려고 하는데, 바꿔야할 연속적인 배열의 최소 크기를 구하는 문제다

미리 배열을 정렬하고, 정렬된 배열과 주어진 배열의 값을 앞에서 비교 하여 바꿔야할 인덱스(start) 위치를 구하고
반대로 뒤에서 부터 다시 비교하여 바꿔야할 인덱스(end)를 구해서 <code>end - start + 1</code> 을 해주면 된다. (길이이기 때문에 +1을 해준다.)

시간 복잡도는 O(n) 이고 공간 복잡도도 O(n)이다

