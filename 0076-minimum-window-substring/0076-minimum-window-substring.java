import java.util.*;

class Solution {
    public String minWindow(String s, String t) {

        if(s.length() < t.length()) return "";

        int[] map = new int[128];

        // store frequency of t
        for(char c : t.toCharArray()) {
            map[c]++;
        }

        int left = 0, right = 0;
        int count = t.length();
        int minLen = Integer.MAX_VALUE;
        int start = 0;

        while(right < s.length()) {

            // include character
            if(map[s.charAt(right)] > 0) {
                count--;
            }
            map[s.charAt(right)]--;
            right++;

            // when valid window found
            while(count == 0) {

                if(right - left < minLen) {
                    minLen = right - left;
                    start = left;
                }

                // shrink window
                map[s.charAt(left)]++;
                if(map[s.charAt(left)] > 0) {
                    count++;
                }
                left++;
            }
        }

        return minLen == Integer.MAX_VALUE ? "" :
               s.substring(start, start + minLen);
    }
}