## Weekly Contest 307

https://leetcode.com/contest/weekly-contest-307

### 2383. Minimum Hours of Training to Win a Competition
문제 이해 하는데 오랜 시간이 걸렸다.

O(N) 으로 energy, experience 리스트를 순회하면서 현재의 energy, experience 값을 바꿔주면 되는 문제였다.

헤맸던 부분은 예를 들면 현재 에너지 4일 때 4의 적을 무찌를 수 있는지 (?) 가 문제에 명확하게 나와있지 않아서 헷갈렸다.
그래서 감으로 0이 될 때는 경쟁할 수 없다고 생각해서 +1 을 더해주었고 이후에 계산 실수를 해서 시도 1번을 날려먹었다.

### 2384. Largest Palindromic Number
이런 문제는 여러번 풀어봤다고 생각했는데.... leading zero 에서 실패해서 못풀었다.
우선순위 큐를 써서 내림차순 숫자의 문자열로 순회했는데, 예외 케이스에 걸려서 실패함

### 2385. Amount of Time for Binary Tree to Be Infected
트리는 자신 있었는데 1번에서 시간을 너무 잡아먹어서 3번 근처도 가지 못했다 ㅜ
start 에 해당하는 노드까지의 depth 와 전체 depth 를 더하면 된다고 생각했는데 역시 예외 케이스(한쪽으로만 확장된 트리일 때)에 걸려 실패하였다.

## 결과
1번 1개 풀어서 3점이다 흑흑
오늘 문제가 좀 어려웠던 듯...