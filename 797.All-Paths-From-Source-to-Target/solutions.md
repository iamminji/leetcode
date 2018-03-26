#### 문제 풀이

[All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/description/)

난이도 **Medium** 이다.

graph의 0번째 리스트 부터 순회하면서 path 라는 임의의 리스트에 해당 리스트의 아이템을 하나씩 넣어준다.
그 아이템은 path에 추가하는 값이자, 동시에 다음에 방문할 depth 가 된다.

그러면 그 depth에 있는 graph의 아이템을 다시 순회하면 된다.

이처럼 같은 루틴이 계속 반복되서, 위의 방식을 dfs로 구현할 수 있다.
리턴 조건은 해당 값이 전체 그래프의 길이와 같을 때로 하면 된다.

다시 되돌아오는? 양방향? 이 아니기 때문에 위의 방식대로 순차적으로 하면 답이 나온다.

