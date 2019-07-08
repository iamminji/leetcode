
/*
 * 3. Longest Substring Without Repeating Characters
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/
 * */

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.isEmpty()) {
            return 0;
        }
        int result = 1;
        int i = 0;
        int j = 1;

        Set<Character> set = new HashSet<>();
        while (i < s.length() && j < s.length()) {
            if (!set.contains(s.charAt(j)) && s.charAt(i) != s.charAt(j)) {
                set.add(s.charAt(j));
                result = Math.max(result, j - i + 1);
                j += 1;
            } else {
                set = new HashSet<>();
                i += 1;
                j = i + 1;
            }
        }
        return result;
    }
}