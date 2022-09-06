function reverseArray(a) {
  // Write your code here
  let reversedArr = [];
  for (let i = a.length - 1; i >= 0; i--) {
    reversedArr.push(a[i]);
  }
  return reversedArr;
}

console.log(reverseArray([1, 2, 3]));
