const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

function mergeSort(array) {
  if (array.length === 1) {
    return array;
  }
  // Split Array in into right and left
  let left = array.splice(0, array.length / 2);

  return merge(mergeSort(left), mergeSort(array));
}

function merge(left, right) {
  let merged = [];

  for (let index = 0; index < left.length; index++) {
    let step = 0;
    while ((right.length > 0) & (left[index] > right[step])) {
      merged.push(right[step]);
      right.splice(step, 1);
    }
    merged.push(left[index]);
    if (step === right.length) {
      break;
    }
  }
  merged = merged.concat(right);
  return merged;
}

function mergeSort2(array) {
  if (array.length === 1) {
    return array;
  }
  // Split Array in into right and left
  const length = array.length;
  const middle = Math.floor(length / 2);
  const left = array.slice(0, middle);
  const right = array.slice(middle);
  // console.log('left:', left);
  // console.log('right:', right);

  return merge2(mergeSort(left), mergeSort(right));
}

function merge2(left, right) {
  const result = [];
  let leftIndex = 0;
  let rightIndex = 0;
  while (leftIndex < left.length && rightIndex < right.length) {
    if (left[leftIndex] < right[rightIndex]) {
      result.push(left[leftIndex]);
      leftIndex++;
    } else {
      result.push(right[rightIndex]);
      rightIndex++;
    }
  }
  console.log(left, right);
  return result.concat(left.slice(leftIndex)).concat(right.slice(rightIndex));
}

console.time("method 1");
const answer = mergeSort(numbers);
console.log(answer);
console.timeEnd("method 1");

// console.time("method 2");
// const answer2 = mergeSort2(numbers);
// console.log(answer2);
// console.timeEnd("method 2");
