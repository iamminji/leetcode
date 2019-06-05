// 344. Reverse String
// https://leetcode.com/problems/reverse-string/


class ReverseString {

    public void recursive(char[] s, int i, int j) {

        if (i >= j) {
            return;
        }

        char tmp = s[j];
        s[j] = s[i];
        s[i] = tmp;
        recursive(s, i + 1, j - 1);

    }

    public void reverseString(char[] s) {

        // # 1 iterator
        int length = s.length;
        int mid = length / 2;
        for (int i = length - 1, j = 0; i >= mid; i--, j++) {
            char tmp = s[j];
            s[j] = s[i];
            s[i] = tmp;
        }

        // # 2
        // recursive
        recursive(s, 0, s.length - 1);
    }
}