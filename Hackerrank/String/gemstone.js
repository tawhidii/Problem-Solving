function gemstones(arr) {
  let str = [...new Set(...arr)];
  let count = 0;
  for (let s of str) {
    if (arr.every((v) => v.includes(s))) {
      count++;
    }
  }
  return count;
}
