#### 문제 풀이

[Max Area of Island](https://leetcode.com/problems/max-area-of-island/description/)

난이도 **Easy** 문제이다.

정답률이 50%가 넘을 만큼, 어렵지 않은 문제이고 실제로 금방 풀었는데 답을 틀렸다.
도저히 엣지 케이스를 찾을 수 없어서 솔루션을 봤음에도 내 답안과 뭐가 다른지 삽질을 엄청 하다가.

어이 없는 실수를 발견했다!

방문한 정점을 visited라는 dictionary 를 사용했고, 키로 현재 좌표 값을 문자열로 변환해서 썼는데,
생각해보니까 이러면 1행 11열과 11행 1열이 구분이 안되더라.

visited를 set으로 바꾸니까 답이 나왔다.
