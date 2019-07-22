
/*
 * 5. Longest Palindromic Substring
 * https://leetcode.com/problems/longest-palindromic-substring/
 * */

class Solution {
    public String longestPalindrome(String s) {

        int maxLength = 0;
        String result = "";

        for (int i = 0; i < s.length(); i++) {

            int start = i;
            int end = i;

            while (end < s.length() && start >= 0 && s.charAt(start) == s.charAt(end)) {
                start -= 1;
                end += 1;
            }

            if (end - start > maxLength) {
                maxLength = end - start;
                result = s.substring(start + 1, end);
            }

            start = i;
            end = i + 1;

            while (end < s.length() && start >= 0 && s.charAt(start) == s.charAt(end)) {
                start -= 1;
                end += 1;
            }

            if (end - start > maxLength) {
                maxLength = end - start;
                result = s.substring(start + 1, end);
            }

        }
        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.longestPalindrome("babad"));
        System.out.println(solution.longestPalindrome("cbbd"));
    }
}
