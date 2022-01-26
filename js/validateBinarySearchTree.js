// Given the root of a binary tree, determine if it is a valid binary search tree (BST).

// A valid BST is defined as follows:

//     The left subtree of a node contains only nodes with keys less than the node's key.
//     The right subtree of a node contains only nodes with keys greater than the node's key.
//     Both the left and right subtrees must also be binary search trees.
// Example 1:

// Input: root = [2,1,3]
// Output: true

function isValidBST(root) {
  return isValidBSTHelper(root);
}
function isValidBSTHelper(queue) {
  if (queue.length === 0) {
    return true;
  }
  let root = queue.shift();
  let left = queue.shift();
  let right = queue.shift();
  if (root === null) {
    return true;
  }
  if (left && left > root) {
    return false;
  }
  if (right && right < root) {
    return false;
  }
  return isValidBSTHelper(queue);
}

console.log(isValidBST([2, 1, 3]));
