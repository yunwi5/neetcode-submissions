class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums: number[]): number[][] {
        /**
         * Var A, B, C
         * Set A = 0, do two sum with B and C on the remaining array
         * 
         * Set middle target t = target - nums[A];
         * 
         * Remaining array K
         * B at index 0, C at index K.length - 1
         * while B < C, 
         * if B + C < target, B++;
         * if B + C > target, C--;
         * else add to result, B++; (either B or C should be fine)
         * 
         * Time: O(n^2)
         * Space: O(1)
         * 
         * 
         * 
         * [-4. -1, -1, 0, 1, 2]
         */

        nums.sort((a, b) => a - b);

        const results: number[][] = [];
        for (let indexA = 0; indexA < nums.length - 2; indexA++) {
            if (indexA > 0 && nums[indexA] === nums[indexA - 1]) {
                continue;
            }
            let indexB = indexA + 1;
            let indexC = nums.length - 1;

            const remainingTarget = 0 - nums[indexA];

            while (indexB < indexC) {
                if (nums[indexB] + nums[indexC] < remainingTarget) {
                    indexB++;
                    continue;
                } 
                if (nums[indexB] + nums[indexC] > remainingTarget) {
                    indexC--;
                    continue;
                }
                if (results.length > 0) {
                    const prevResult = results.at(-1);
                    const newResult = [nums[indexA], nums[indexB], nums[indexC]];
                    if (prevResult[0] === newResult[0] && prevResult[1] === newResult[1] && prevResult[2] === newResult[2]) {
                        indexB++;
                        continue;
                    }
                }
                results.push([nums[indexA], nums[indexB], nums[indexC]])
                indexB++;
            }
        }

        return results;
    }
}
