function pangrams(s) {
  // Write your code here
  const ss = new Set(s.toLowerCase(s)).size;
  if (ss > 26) {
    return "pangram";
  } else {
    return "not pangram";
  }
}
