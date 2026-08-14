class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums: number[]): number[] {
        /**]
         * [1, 2, 4, 6]
         * [48, 24, 12, 8]
         * 
         * map
         * key  value
         * 0     1
         * 1     1
         * 2     2
         * 3     8
         * 
         * 
         * suffix map
         * key    value
         * 3        1
         * 2        6
         * 1        24
         * 0        48 
         */


        const prefixProductArray: number[] = Array(nums.length).fill(0);
        const suffixProductArray: number[] = Array(nums.length).fill(0);

        let prefixProduct = 1;
        for (let i=0; i<nums.length; i++) {
            const num = nums[i];
            prefixProductArray[i]=prefixProduct;
            prefixProduct *= num;
        }

        let suffixProduct = 1;
        for (let i = nums.length-1; i >=0; i--) {
            const num = nums[i];
            suffixProductArray[i] = suffixProduct;
            suffixProduct *= num;
        }

        for (let i = 0; i < prefixProductArray.length; i++) {
            prefixProductArray[i] = prefixProductArray[i] * suffixProductArray[i];
        }

        return prefixProductArray;
    }
}
