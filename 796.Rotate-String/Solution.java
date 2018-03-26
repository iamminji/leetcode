/*
    796. Rotate String
    https://leetcode.com/problems/rotate-string/description/
*/


class Solution {
    public boolean rotateString(String A, String B) {

        int lengthA = A.length();
        int lengthB = B.length();

        if (lengthA != lengthB) {
            return false;
        }

        int cnt = 0;
        for (int p = 0; p < A.length(); ++p) {
            for (int i = 0; i < A.length(); ++i) {
                if (A.charAt((p + i) % lengthA) != B.charAt(i)) {
                    cnt = 0;
                    break;
                } else {
                    cnt += 1;
                }
            }
            if (cnt == lengthA) {
                return true;
            }
        }
        return cnt == lengthA;
    }
}
