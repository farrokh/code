// Write two functions that finds the factorial of any number. One should use recursive, the other should just use a for loop

function findFactorialRecursive(number) {
  if (number < 1) {
    return 1;
  }
  return number * findFactorialRecursive(number - 1);
}

function findFactorialIterative(number) {
  let answer = 1;
  while (number > 0) {
    answer = answer * number;
    number--;
  }
  return answer;
}

// const answer = findFactorialRecursive(3);
// console.log(answer);

// Given a number N return the index value of the Fibonacci sequence, where the sequence is:

// 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
// the pattern of the sequence is that each value is the sum of the 2 previous values, that means that for N=5 → 2+3

//For example: fibonacciRecursive(6) should return 8

function fibonacciIterative(n) {
  if (n == 0) {
    return 0;
  }
  if (n === 1) {
    return 1;
  }
  let i = 2;
  let fibA = 0;
  let fibB = 1;
  let fibC;
  while (i <= n) {
    fibC = fibB + fibA;
    i++;
    fibA = fibB;
    fibB = fibC;
  }
  return fibC;
  //code here;
}
// const fib = fibonacciIterative(6);

function fibonacciRecursive(n) {
  if (n < 0) {
    return 0;
  }
  if (n === 1) {
    return 1;
  }
  return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

const fib = fibonacciRecursive(6);
console.log(fib);
