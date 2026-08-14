class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s: string): boolean {
        /**
         * Two pointers.
         * PointerA: start from index 0
         * PointerB: start from index n - 1 (n is a string length)
         * While s[pointerA] == s[pointerB]:
         * if PointerA >= PointerB, it is palindrome
         * pointerA++; pointerB++;
         */ 

        let pointerA = 0;
        let pointerB = s.length - 1;
        while (pointerA <= pointerB) {
            if (Solution.isAlphanumeric(s[pointerA]) === false) {   
                pointerA++;
                continue;
            }
            if (Solution.isAlphanumeric(s[pointerB]) === false) {
                pointerB--;
                continue;
            }
            if (s[pointerA].toLowerCase() != s[pointerB].toLowerCase()) {
                return false;
            }
            pointerA++;
            pointerB--;
        }

        return true;
    }

    static isAlphanumeric(s: string): boolean {
        return /^[a-z0-9]+$/i.test(s);
    }
}
