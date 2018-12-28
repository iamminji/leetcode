#### 문제 풀이

[Array Nesting](https://leetcode.com/problems/array-nesting/) 

난이도는 `medium` 이다.

어떤 배열이 들어오고, 해당 배열의 각 값들은 다시 그 배열의 인덱스가 되어서 최종적으로 가장 길게 연결되는 배열의 길이를 찾는 것이다.
단순하게 앞에서 부터 값을 확인하고 그 값을 인덱스로 바꿔 치기 해가면서 진행했다.

이미 확인하는 값 (즉 확인한 인덱스) 이면 skip 할 수 있게 <code>visited</code> 라는 배열을 하나 더 두었다.

결과 값을 위해선 <code>res</code> 라는 배열을 두었고, 다음 인덱스로 넘어갈 때마다 이전 값의 +1 을 해 주었다.

최종적으로 <code>res</code> 의 가장 큰 값을 리턴해주면 된다.


**submission**

2번 트라이 했다. 루프를 돌 때 증가시키는 변수를 잘못 썼다.
아래의 코드(가 WA 뜬거) 에선 <code>[0,2,1]</code>의 <code>res</code> 값이 <code>[1, 0, 0]</code>이 들어가 버린다.
그럴 수 밖에 없는게 <code>nums[0]</code>은 <code>0</code> 이기 때문에 jump 만 계속 증가하고 루프가 끝나버린다.

jump를 둔 건 최초에 값 확인을 위한 배열을 하나만 두려고 했다가, 나중에 두개로 바꾸면서 미쳐 생각 못해버리고 그대로 갖다 써서 그렇다.

<pre><code>for jump < len(nums) {
    if visited[i] {
        jump += 1
        continue
    }
    ...
}
</code></pre>
