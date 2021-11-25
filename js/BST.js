class Node {
  constructor(value) {
    this.left = null;
    this.right = null;
    this.value = value;
  }
}

class BinarySearchTree {
  constructor() {
    this.root = null;
  }
  insert(value) {
    const newNode = new Node(value);
    if (this.root === null) {
      this.root = newNode;
    } else {
      let pointer = this.root;
      while (pointer !== null) {
        if (value > pointer.value) {
          if (pointer.right) {
            pointer = pointer.right;
          } else {
            pointer.right = newNode;
            break;
          }
        } else {
          if (pointer.left) {
            pointer = pointer.left;
          } else {
            pointer.left = newNode;
            break;
          }
        }
      }
      pointer = newNode;
    }
  }
  lookup(value) {
    if (this.root === null) {
      return null;
    }
    let pointer = this.root;
    while (pointer) {
      if (value === pointer.value) {
        return pointer;
      }

      if (value > pointer.value) {
        pointer = pointer.right;
      } else {
        pointer = pointer.left;
      }
    }
    return null;
  }

  // remove(value) {
  //   if (this.root === null) {
  //     return null;
  //   }
  //   let pointer = this.root;
  //   let parent = null;
  //   while (pointer) {
  //     if (value === pointer.value) {
  //       break;
  //     }
  //     parent = pointer;
  //     if (value > pointer.value) {
  //       pointer = pointer.right;
  //     } else {
  //       pointer = pointer.left;
  //     }
  //   }
  //   if (pointer === null) {
  //     return null;
  //   }
  //   if (pointer.left === null && pointer.right === null) {
  //     if (parent.left === pointer) {
  //       parent.left = null;
  //     } else {
  //       parent.right = null;
  //     }
  //   } else if (pointer.left === null) {
  //     if (parent.left === pointer) {
  //       parent.left = pointer.right;
  //     } else {
  //       parent.right = pointer.right;
  //     }
  //   } else if (pointer.right === null) {
  //     if (parent.left === pointer) {
  //       parent.left = pointer.left;
  //     } else {
  //       parent.right = pointer.left;
  //     }
  //   } else {
  //     let temp = pointer.right;
  //     while (temp.left !== null) {
  //       temp = temp.left;
  //     }
  //     pointer.value = temp.value;
  //     this.remove(temp.value);
  //   }
  // }

  // traverse(callback) {
  //   const traverse = (node) => {
  //     if (node !== null) {
  //       traverse(node.left);
  //       callback(node.value);
  //       traverse(node.right);
  //     }
  //   };
  //   traverse(this.root);
  // }
  remove(value) {
    if (!this.root) {
      return false;
    }
    let currentNode = this.root;
    let parentNode = null;
    while (currentNode) {
      if (value < currentNode.value) {
        parentNode = currentNode;
        currentNode = currentNode.left;
      } else if (value > currentNode.value) {
        parentNode = currentNode;
        currentNode = currentNode.right;
      } else if (currentNode.value === value) {
        //We have a match, get to work!

        //Option 1: No right child:
        if (currentNode.right === null) {
          if (parentNode === null) {
            this.root = currentNode.left;
          } else {
            //if parent > current value, make current left child a child of parent
            if (currentNode.value < parentNode.value) {
              parentNode.left = currentNode.left;

              //if parent < current value, make left child a right child of parent
            } else if (currentNode.value > parentNode.value) {
              parentNode.right = currentNode.left;
            }
          }

          //Option 2: Right child which doesnt have a left child
        } else if (currentNode.right.left === null) {
          currentNode.right.left = currentNode.left;
          if (parentNode === null) {
            this.root = currentNode.right;
          } else {
            //if parent > current, make right child of the left the parent
            if (currentNode.value < parentNode.value) {
              parentNode.left = currentNode.right;

              //if parent < current, make right child a right child of the parent
            } else if (currentNode.value > parentNode.value) {
              parentNode.right = currentNode.right;
            }
          }

          //Option 3: Right child that has a left child
        } else {
          //find the Right child's left most child
          let leftmost = currentNode.right.left;
          let leftmostParent = currentNode.right;
          while (leftmost.left !== null) {
            leftmostParent = leftmost;
            leftmost = leftmost.left;
          }

          //Parent's left subtree is now leftmost's right subtree
          leftmostParent.left = leftmost.right;
          leftmost.left = currentNode.left;
          leftmost.right = currentNode.right;

          if (parentNode === null) {
            this.root = leftmost;
          } else {
            if (currentNode.value < parentNode.value) {
              parentNode.left = leftmost;
            } else if (currentNode.value > parentNode.value) {
              parentNode.right = leftmost;
            }
          }
        }
        return true;
      }
    }
  }
}

const tree = new BinarySearchTree();
tree.insert(9);
tree.insert(4);
tree.insert(6);
tree.insert(20);
tree.insert(170);
tree.insert(15);
tree.insert(1);
// console.log(tree.print());
// console.log(JSON.stringify(traverse(tree.root)));
// console.log(traverse(tree.root));
// console.log(tree.lookup(20));
// JSON.stringify(traverse(tree.root));
// console.log(
//   tree.traverse((value) => {
//     console.log(value);
//   })
// );

//     9
//  4     20
//1  6  15  170

function traverse(node) {
  const tree = { value: node.value };
  tree.left = node.left || traverse(node.left);
  tree.right = node.right || traverse(node.right);
  return tree;
}
