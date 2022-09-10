function matchingStrings(strings, queries) {
  // Write your code here
  const countString = {};
  let result = [];
  strings.forEach((str) => {
    countString[str] ? countString[str]++ : (countString[str] = 1);
  });
  queries.forEach((query) => {
    countString.hasOwnProperty(query)
      ? result.push(countString[query])
      : result.push(0);
  });
  return result;
}

matchingStrings(["ab", "ab", "abc"], ["ab", "abc", "bc"]);
