// Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

// Implement the MyQueue class:

// void push(int x) Pushes element x to the back of the queue.
// int pop() Removes the element from the front of the queue and returns it.
// int peek() Returns the element at the front of the queue.
// boolean empty() Returns true if the queue is empty, false otherwise.
// Notes:

// You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
// Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

// Example 1:

// Input
// ["MyQueue", "push", "push", "peek", "pop", "empty"]
// [[], [1], [2], [], [], []]
// Output
// [null, null, null, 1, 1, false]

// Explanation
// MyQueue myQueue = new MyQueue();
// myQueue.push(1); // queue is: [1]
// myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
// myQueue.peek(); // return 1
// myQueue.pop(); // return 1, queue is [2]
// myQueue.empty(); // return false

// class MyQueue {
//   constructor() {
//     this.stack1 = [];
//     this.stack2 = [];
//   }

//   push(x) {
//     this.stack1.push(x);
//   }

//   pop() {
//     if (this.stack2.length === 0) {
//       while (this.stack1.length > 0) {
//         this.stack2.push(this.stack1.pop());
//       }
//     }
//     return this.stack2.pop();
//   }

//   peek() {
//     if (this.stack2.length === 0) {
//       while (this.stack1.length > 0) {
//         this.stack2.push(this.stack1.pop());
//       }
//     }
//     return this.stack2[this.stack2.length - 1];
//   }

//   empty() {
//     return this.stack1.length === 0 && this.stack2.length === 0;
//   }
// }

class CrazyQueue {
  constructor() {
    this.first = [];
    this.last = [];
  }

  enqueue(value) {
    const length = this.first.length;
    for (let i = 0; i < length; i++) {
      this.last.push(this.first.pop());
    }
    this.last.push(value);
    return this;
  }

  dequeue() {
    const length = this.last.length;
    for (let i = 0; i < length; i++) {
      this.first.push(this.last.pop());
    }
    this.first.pop();
    return this;
  }
  peek() {
    if (this.last.length > 0) {
      return this.last[0];
    }
    return this.first[this.first.length - 1];
  }
  empty() {
    return this.first.length === 0 && this.last.length === 0;
  }
}
