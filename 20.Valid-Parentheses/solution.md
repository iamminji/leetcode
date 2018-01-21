#### 문제 풀이

[Valid Parentheses](https://leetcode.com/problems/valid-parentheses/description/) 라는 문제다
난이도는 **Easy** 이다.

괄호 짝 맞추기 문제로, 비슷한 유형의 문제가 온라인 저지 사이트에 대부분 있을 만큼 유명한 문제다.

스택을 이용하는 문제로, 여는 괄호가 나올 때 닫는 괄호를 스택에 넣어주고, 닫는 괄호가 나올 때 스택에서 pop 해주어 비교해주면 된다.

시간 복잡도는 O(n) 이고 공간 복잡도도 O(n) 이다.
