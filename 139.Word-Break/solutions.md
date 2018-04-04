#### 문제 풀이

[Word Break](https://leetcode.com/problems/word-break/description/)

난이도 **Medium** 이다.

문자열 s가 주어지고 문자열 s를 임의로 나누었을 때 해당하는 모든 문자가 wordDict에 있는지에 대하여 리턴하는 문제다.

DP 문제 같은데, 어떤식으로 접근해야 될 지 몰라서 그냥 답을 봤다.

우선 주어진 문자열 s의 길이 + 1 만큼의 배열을 만든다.
해당 배열을 dp라고 보자면 dp에 들어갈 값은 다음과 같이 정의 내린다.

<pre>
    dp[i] => 0 부터 i 번째 까지 문자열이 Dictionary 에 포함되어 있는지 여부
</pre>

이렇게 정의 내릴 수 있는 이유는 예를 들어서,

주어진 문자열이 ```leetcode``` 면 값을 찾을 때 (임의로 함수 이름을 search라고 보면)

<pre>
search(l) && search(eetcode)
search(le) && search(eetcode)
search(lee) && search(tcode)
.
.
.
search(leetcod) && search(e)
</pre>

이렇게 앞에서 부터 한 글자 씩 딕셔너리에 있는지 (search) 에 찾아본다고 생각하는 것이다.

정리하자면 prefix를 먼저 찾고 그 다음 suffix를 찾는다고 생각하면 된다.

```leetcode``` 라는 문자열로 보면 ```leet``` 이 딕셔너리에 있으니까 dp[4] = True가 된다. 4번째 글자까지 딕셔너리에 있다는 의미다. 그러면 다음에 찾을 값은 leet 다음 글자인데 그 글자 시작 지점은 4다. (문자열 인덱스가 0부터 시작하니깐)

그럼 또 4부터 문자열 끝까지 있는지 돌면 된다.

결국 주어진 예제에서 dp 에는 ```[True, False, False, False, True, False, False, False, True]``` 이렇게 들어가게 되는 것이다.

답은 가장 마지막 값을 return 하면 된다.