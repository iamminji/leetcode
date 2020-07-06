## 문제

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

```
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
```


Example 2:
```
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
```

### 솔루션
리스트의 가장 마지막 값에 1을 더하는 문제다. list 를 string 으로 join 해서 다시 이걸 integer 로 변경 후 1을 더하고 다시 list 로 바꾸는 방법도 있겠지만..
문제에서 원한 것은 그게 아니였을 것이다.


리스트의 가장 마지막 값에 1을 더하고, 그 값이 10을 넘는 경우는 값을 올려야 하기 때문에 10으로 나눈 몫과 나머지를 각각 구한다.
나머지 값은 다시 리스트에 넣고 몫은 다음 번 계산 때 사용한다.

마지막 몫이 0이 아닐 경우 리스트에 넣어주고 이 리스트를 뒤집어 주면 된다.

코드는 아래와 같다.

```python3
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = list()
        n = 1
        for i in range(len(digits) - 1, -1, -1):
            num = digits[i] + n
            p, q = num // 10, num % 10
            result.append(q)
            n = p

        if n != 0:
            result.append(n)

        return result[::-1]
```

#### 복잡도
시간 복잡도는 O(n) 이고 공간 복잡도도 O(n) 이다.