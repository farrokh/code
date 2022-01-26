// You are climbing a staircase. It takes n steps to reach the top.

// Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

// Example 1:

// Input: n = 2
// Output: 2
// Explanation: There are two ways to climb to the top.
// 1. 1 step + 1 step
// 2. 2 steps

// Example 2:

// Input: n = 3
// Output: 3
// Explanation: There are three ways to climb to the top.
// 1. 1 step + 1 step + 1 step
// 2. 1 step + 2 steps
// 3. 2 steps + 1 step

/**
 * @param {number} n
 * @return {number}
 */
function climbStairs() {
  let caches = {
    0: 0,
    1: 1,
    2: 2,
  };
  return function climbStairsR(n) {
    if (!caches[n]) {
      caches[n] = climbStairsR(n - 1) + climbStairsR(n - 2);
    }
    return caches[n];
  };
}
const climbing = climbStairs();
console.log(climbing(20));
