class Solution {
    public int reverse(int x) {
        int reversed = 0;
        int original = x;
        
        // Handle negative numbers
        boolean isNegative = x < 0;
        if (isNegative) {
            x = -x;  // Work with absolute value
        }
        
        while (x > 0) {
            // Check for overflow before adding next digit
            if (reversed > Integer.MAX_VALUE / 10) {
                return 0;  // Will overflow
            }
            
            reversed = reversed * 10 + x % 10;
            x /= 10;
        }
        
        // Apply sign back if original was negative
        if (isNegative) {
            // Check for INT_MIN overflow (-2147483648 reversed would overflow)
            if (reversed > Integer.MAX_VALUE) {
                return 0;
            }
            reversed = -reversed;
        }
        
        return reversed;
    }
}