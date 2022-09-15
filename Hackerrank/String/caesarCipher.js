function caesarCipher(s, k) {
  // Write your code here
  let clearTextArr = s.split("");
  let original = "abcdefghijklmnopqrstuvwxyz";
  let rotation = k % original.length;
  let roatated = original.slice(rotation) + original.slice(0, rotation);
  clearTextArr.forEach((char, index) => {
    if (original.includes(char.toLowerCase())) {
      let idx = original.indexOf(char.toLowerCase());
      if (/^[A-Z]*$/.test(clearTextArr[index])) {
        clearTextArr[index] = roatated[idx].toUpperCase();
      } else {
        clearTextArr[index] = roatated[idx];
      }
    }
  });
  return clearTextArr.join("");
}
