 #### 문제 풀이

[Wiggle Sort II](https://leetcode.com/problems/wiggle-sort-ii/description/) 라는 문제다

난이도는 **Medium** 이다.

문제 조건인 시간 복잡도 O(n)과 공간 복잡도 O(1)을 지키기가 까다로워, 이 조건을 무시하고 우선 구현해 보기로 하였다.

가장 처음에 생각한 아이디어는 전체를 정렬하여 앞에서 부터 절반 까지 홀수 인덱스에 넣고, 그 절반 이후 나머지 것들을 짝수 인덱스에 넣는 것이였다.
그러나 <code>[4, 5, 5, 6]</code> 에서 예외가 발생하였다.

이 아이디어로 하면 5는 두개고 전체 개수는 4개라, 무조건 인접할 수 밖에 없었다.
뭔가 홀/짝 인덱스를 이용하면 될 것 같은데, 더 이상 생각이 나지 않아 Discuss를 보았다.

그래서 찾은 것이 바로 아래의 [코드](https://leetcode.com/problems/wiggle-sort-ii/discuss/77678/3-lines-Python-with-Explanation-Proof) 이다.

(파이썬이라서 헷갈릴 수 있지만, 리스트의 마지막은 step으로 그 만큼 점프? 하여 새로운 리스트를 만든다고 보면 된다. 마찬가지로 -1 step은 거꾸로 1 크기만큼 점프하는 것이다.)
<pre><code>
nums.sort()
half = len(nums[::2]) - 1
nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]
</code></pre>
    
처음에 내가 생각했던 것과 같은거가 아닌가 싶었는데, 위의 방식은 넣는 순서가 내 것과는 달랐다.
나는 앞에서 부터 작은건 0, 2, 4 ... 로 넣고 큰거는 같은 방향으로 1, 3, 5 ... 로 하였는데
위의 코드는 리스트의 중간 인덱스, mid 부터 처음 인덱스 까지 0, 2, 4 ... 로 넣고 마지막 인덱스부터 mid까지 1, 3, 5 ... 로 넣는 방식이다.

내가 넣는 방식은 아래와 같다. 첫 번째는 되지만, 두 번째는 안되는 것이다.
<pre>
Small half:  S . S . S . M      Small half:  S . S . M . M .
Large half:  . M . L . L .      Large half:  . M . M . L . L
--------------------------      --------------------------
Together:    S M S L S L M      Together:    S M S M M L M L
</pre>

두 번째는 <code>S M S M L M L M</code> 와 같은 답이 존재하기 때문이다.


Discuss의 코드에는 예외는 없는것인가 살펴보았는데 친절하게도 가장 하단에 작성자가 검증을 해놓았다.

<pre>
Small half:  M . S . S . S      Small half:  M . S . S . S .
Large half:  . L . L . M .      Large half:  . L . L . L . M
--------------------------      --------------------------
Together:    M L S L S M S      Together:    M L S L S L S M
</pre>

정렬된 상태에서 중간 부분 부터 시작 부분 까지 0, 2, 4 ... 인덱스에 넣을 때 그 값은 중간 값 부터 중간 값과 작거나 같은 값들의 연속이 된다.
마찬가지로 홀수 인덱스에 넣을 값은 가장 큰 값 부터 중간 값 까지 채워 넣는다면, 가장 큰 값은 최소한 중간 값 보다 크거나 같을 것이다.

그렇다면 두 리스트를 합친 값은 위의 그림 처럼 무조건 wiggle 될 수 밖에 없다. 

가장 큰 값의 양 옆은 무조건 중간 값이거나 중간 값 보다 작은 값이 되기 때문이다.

만약, 중복 되는 값들이 여러개 있다고 하여도 아래 처럼 보장이 가능하다.

<pre>
Small half:  M . M . S . S      Small half:  M . S . S . S .
Large half:  . L . L . M .      Large half:  . L . M . M . M
--------------------------      --------------------------
Together:    M L M L S M S      Together:    M L S M S M S M
</pre>

시간 복잡도는 정렬을 하였으므로 O(nlogn)이고 공간 복잡도는 내부 nums 리스트를 사용하여서 O(1)이다.

주어진 조건을 지키지는 못했다. 찾아보니, 3 way quicksort 개념을 사용하면 될 것 같은데, 그 개념이 결국 현재 값과 같은 값, 작은 값, 큰 값 을 이용하는.
위의 아이디어의 변형인데, 좀 더 공부해야 될 것 같다. 구현이 넘 힘들당.