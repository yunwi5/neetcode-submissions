class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const dupCheckMap = new Set();
        for (let num of nums) {
            if (dupCheckMap.has(num)) {
                return true;
            }
            dupCheckMap.add(num);
        }
        return false;
    }
}
