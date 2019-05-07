// 344. Reverse String
// https://leetcode.com/problems/reverse-string/


class ReverseString {
    public void reverseString(char[] s) {
        int length = s.length;
        int mid = length / 2;
        for (int i = length - 1, j = 0; i >= mid; i--, j++) {
            char tmp = s[j];
            s[j] = s[i];
            s[i] = tmp;
        }
    }
}