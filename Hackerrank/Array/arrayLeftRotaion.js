function rotateLeft(d, arr) {
  // Write your code here

  for (let i = 0; i < d; i++) {
    let indexZero = arr[0];
    let indexOne = arr[1];
    arr[0] = indexOne;
    arr.push(indexZero);
    arr.splice(arr.indexOf(indexOne), 1);
  }
  return arr;
}
