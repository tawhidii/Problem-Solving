function doSum(arry) {
  let total = 0;
  arry.forEach((item) => {
    total += item;
  });
  return total;
}

function hourglassSum(arr) {
  // Write your code here
  let max = -999;
  for (let i = 0; i < arr.length - 2; i++) {
    for (let j = 0; j < arr.length - 2; j++) {
      let top = doSum(arr[i].slice(j, j + 3));
      let mid = arr[i + 1][j + 1];
      let bottom = doSum(arr[i + 2].slice(j, j + 3));
      let sss = top + mid + bottom;
      max = Math.max(sss, max);
    }
  }
  return max;
}
