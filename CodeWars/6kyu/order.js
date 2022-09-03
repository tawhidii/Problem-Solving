function order(words) {
  // ...
  let result = [];
  let filterTheNumbers = [];
  words.split(" ").forEach((item) => {
    item.split("").forEach((item) => {
      let makeItInt = parseInt(item);
      if (Number.isInteger(makeItInt)) {
        filterTheNumbers.push(makeItInt);
      }
    });
  });
  const sortedNumbers = filterTheNumbers.sort((a, b) => a - b);
  sortedNumbers.forEach((num) => {
    words.split(" ").forEach((word) => {
      if (word.includes(num.toString())) {
        result.push(word);
      }
    });
  });
  return result.join(" ");
}
console.log(order("is2 Thi1s T4est 3a"));
