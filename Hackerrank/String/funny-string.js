function funnyString(s) {
  let left = 0;
  let right = s.length - 1;
  while (left <= right) {
    let diffLeft = Math.abs(s[left].charCodeAt(0) - s[left + 1].charCodeAt(0));
    let diffRight = Math.abs(
      s[right].charCodeAt(0) - s[right - 1].charCodeAt(0)
    );

    if (diffLeft !== diffRight) {
      return "Not Funny";
    }
    left++;
    right--;
  }
  return "Funny";
}
