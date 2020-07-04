## 문제
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)


``` 
Example 1:

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:

Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]
```

Note:
- cells.length == 8
- cells[i] is in {0, 1}
- 1 <= N <= 10^9

### 솔루션
양 쪽 값이 다르면 0, 같으면 1이라는 말을 문제에서 길게 설명하고 있다.
우선 맨 끝 값들 cells[0], cells[7] 은 참고할 값이 한 개 밖에 없으므로 무조건 0이 들어간다.

그리고 나머지 cell 들은 좌우 값을 비교해서 넣어주면 되는데, 그냥 계산하면 Time Limit Exceeded 이 뜬다. (cell 비교가 6번 밖에 일어나지 않지만, 주어진 N 최대 값이 10^9 이다.)

N 값이 크기 때문에 규칙을 찾아야 하는 문제였다. 좌/우 비교 시 값이 변경 되기 때문에, 어느 순간 같은 패턴만 등장할 것이라고 추측 했다.
그래서 100개 씩 돌려보니 14번마다 같은 값이 나오더라. (공식은 모르겠음...)

문제에서 Day 라고 주어진 부분을 키로 쓰고, 값을 cell 을 넣었다. 그 후 N 으로 들어오는 값을 14로 나누어 (모듈러 연산) 리턴했더니 풀렸다(????)

> IDE 로 했으니 찾았지, 손으로 했으면.. 패턴을 찾을 수 있었을까..?

