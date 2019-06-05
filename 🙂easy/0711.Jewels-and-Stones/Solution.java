package com.leetcode.minji;

import java.util.HashSet;
import java.util.Set;

/**
 * 771. Jewels and Stones
 * https://leetcode.com/problems/jewels-and-stones/
 */

public class Solution {
    public int numJewelsInStones(String J, String S) {

        Set<Character> jewels = new HashSet<>();
        for (char j : J.toCharArray()) {
            jewels.add(j);
        }
        int types = 0;
        for (char s : S.toCharArray()) {
            if (jewels.contains(s)) {
                types += 1;
            }
        }
        return types;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int res = solution.numJewelsInStones("aA", "aAAbbbb");
        System.out.println(res);
        res = solution.numJewelsInStones("z", "ZZ");
        System.out.println(res);

    }
}

