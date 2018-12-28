#### 문제 풀이

[Sliding Puzzle](https://leetcode.com/problems/sliding-puzzle/description/)

난이도 **Hard** 이다.

Contest로 나왔을 때는 못 풀고, 스터디 시간 때 설명 듣고 나서야(Breadth-first search가 왜 되는지 몰랐었다.) 이해가 갔던 문제이다.

2 X 3 크기의 리스트가 주어지고, 0이 들어 있는 부분에서 상/하/좌/우 만 swap이 가능할 때
<code>[[1, 2, 3], [4, 5, 0]]</code> 를 만들 수 있는 최소한의 swap count(이하 move)를 구해야 한다.

board에서 0의 위치만 바꿔서 새로운 board를 만들고 그 board를 큐에 넣어서, 현재 상태가 종료 상태인지 확인 해 가면서 loop를 돌면 된다.
이 때 현재 move를 딕셔너리로 만들어서 이전 값 + 1로 갱신해주어 갔고, 리턴할 때 종료 조건 때문에 끝났는지 아닌지 확인하려고 get 을 사용했다.

새로운 board를 만들 때 그냥 갖다 썼더니, 얕은 복사가 되어서 상태가 바뀌지 않아서 에러가 났었다. 그래서 deepcopy로 바꿔서 했더니 되었다.

