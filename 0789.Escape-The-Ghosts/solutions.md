#### 문제 풀이

[Escape The Ghosts](https://leetcode.com/problems/escape-the-ghosts/description/)

난이도 **Medium** 이다.

처음에는 시작 좌표 값을 queue 에 넣고 좌표를 키로 두어서 이동 거리 값을 갖는 딕셔너리를 따로 두려고 했다. 
그래서 타겟까지 가는 나의 이동 거리와, ghosts의 이동 거리를 비교하여 내가 더 오래 걸리면 false를 리턴하는 형식으로 하려고 하다가,
구현이 너무 까다로워서 포기.

깔끔하게 솔루션를 봤다.

그래서 본 것이 taxicab distance 이다. 이게 뭔 소리인가 싶어서 구글링을 열심히 하다가 [이 글](http://bbs.nicklib.com/algorithm/1697)을 보고 나서야,
솔루션의 답이 이해가 갔다.

저 방식을 보니, 문제가 쉬워졌다.

ghosts의 이동 거리와 나의 이동 거리의 대소를 비교해서 리턴해주면 되는 것이다.

ghosts의 이동 거리가 더 길다면, 내가 먼저 도착 할 수 있으므로 넘어가고, 나의 이동 거리가 더 크거나 같다면 ghosts한테 잡히기 때문에 False를 리턴한다.

알고나면 별 거 아닌데, 솔루션 안봤으면 절대로 이렇게 생각 못했을 것 같다.
