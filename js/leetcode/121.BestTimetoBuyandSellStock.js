// You are given an array prices where prices[i] is the price of a given stock on the ith day.

// You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

// Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

// Example 1:

// Input: prices = [7,1,5,3,6,4]
// Output: 5
// Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
// Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

// Example 2:

// Input: prices = [7,6,4,3,1]
// Output: 0
// Explanation: In this case, no transactions are done and the max profit = 0.

// my naive solution
// var maxProfit = function (prices) {
//   let profit = 0;
//   let hash = {};
//   if (prices.length < 2) {
//     return 0;
//   }
//   for (i = 0; i < prices.length; i++) {
//     for (j = i + 1; j < prices.length; j++) {
//         if (!hash[`${prices[j]}-${prices[i]}`]) {
//             hash[`${prices[j]}-${prices[i]}`] = prices[j] - prices[i];
//         }
//       if (hash[`${prices[j]}-${prices[i]}`] > profit) {
//         profit = hash[`${prices[j]}-${prices[i]}`];
//       }
//     }
//   }
//   return profit;
// };

// best solution
var maxProfit = function (prices) {
  var min = Number.MAX_SAFE_INTEGER;
  var max = 0;
  for (var i = 0; i < prices.length; i++) {
    min = Math.min(min, prices[i]);
    max = Math.max(max, prices[i] - min);
  }
  return max;
};

// second best solution
var maxProfitv2 = function (prices) {
  let maxProf = 0,
    curr = prices[0];

  for (let x of prices) {
    if (curr < x) maxProf = Math.max(maxProf, x - curr);
    else curr = x;
  }
  return maxProf;
};

console.log(maxProfit([7, 1, 5, 3, 6, 4]));
