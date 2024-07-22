function findFirstDuplicate(arr) {
  const eleCount = {};

  // for (let i = 0; i < arr.length; i++) {
  for (const i in arr) {
    if (!eleCount[arr[i]]) {
      eleCount[arr[i]] = 1;
    } else if (eleCount[arr[i]]) {
      eleCount[arr[i]] += 1;
      return arr[i];
    }
  };
  return -1
};

// console.log(findFirstDuplicate([0, 0, 1, 2, 3, 4, 4]))
// console.log(findFirstDuplicate([1, 2, 3, 4]))
// console.log(findFirstDuplicate([2, 1, 3, 3, 2]))

if (require.main === module) {
  // add your own tests in here
  console.log("Expecting: 3");
  console.log("=>", findFirstDuplicate([2, 1, 3, 3, 2]));

  console.log("");

  console.log("Expecting: -1");
  console.log("=>", findFirstDuplicate([1, 2, 3, 4]));
}

module.exports = findFirstDuplicate;

// pseudo function findFirstDuplicate
// declare and initialize object to keep track of dupes

// iterate over the array given as an arg
// check if array element is present and if not add with element as key and 1 as value
// else if element is present, increment by one and exit
