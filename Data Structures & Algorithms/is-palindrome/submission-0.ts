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

        let alphanumericS = '';
        for (let c of s) {
            if (Solution.isAlphanumeric(c)) {
                alphanumericS = alphanumericS + c;
            }
        }

        let pointerA = 0;
        let pointerB = alphanumericS.length - 1;
        while (pointerA <= pointerB) {
            if (alphanumericS[pointerA].toLowerCase() != alphanumericS[pointerB].toLowerCase()) {
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
