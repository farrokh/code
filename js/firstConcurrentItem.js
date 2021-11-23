function findFirsDuplicated(bucket) {
  let hashTable = {};
  for (let i = 0; i < bucket.length; i++) {
    if (hashTable[bucket[i]]) {
      //   console.log(bucket[i]);
      return bucket[i];
    }
    hashTable[bucket[i]] = true;
  }
  return undefined;
}
//Google Question
//Given an array = [2,5,1,2,3,5,1,2,4]:
console.log(findFirsDuplicated([2, 5, 5, 2, 3, 5, 1, 2, 4]));
//It should return 2

//Given an array = [2,1,1,2,3,5,1,2,4]:
//It should return 1

//Given an array = [2,3,4,5]:
//It should return undefined

//Bonus... What if we had this:
// [2,5,5,2,3,5,1,2,4]
// return 5 because the pairs are before 2,2
