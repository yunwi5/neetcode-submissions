class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums: number[], target: number): number[] {
        const indexByNumberMap = new Map<number, number>();
        for (let i = 0; i < nums.length; i++) {
            const currentNum = nums[i];
            const remaining = target - currentNum;
            if (indexByNumberMap.has(remaining)) {
                return [i, indexByNumberMap.get(remaining)];
            }
            indexByNumberMap.set(currentNum, i);
        }
        throw Error('Solution has to exist!');
    }
}
