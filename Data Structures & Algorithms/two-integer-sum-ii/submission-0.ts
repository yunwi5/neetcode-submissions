class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers: number[], target: number): number[] {
        let pointerA = 0;
        let pointerB = numbers.length - 1;

        while (pointerA < pointerB) {
            const sum = numbers[pointerA] + numbers[pointerB];
            if (sum === target) {
                return [pointerA + 1, pointerB + 1];
            }
            if (sum < target) {
                pointerA++;
            }
            if (sum > target) {
                pointerB--;
            }
        }

        throw new Error('Unexpected!');
    }
}
