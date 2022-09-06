const arraySum = (arra) => {
  let total = 0;
  arra.forEach((element) => {
    total += element;
  });
  return total;
};

function tribonacci(signature, n) {
  //your code here
  for (let i = 0; i < n; i++) {
    signature.push(arraySum(signature.slice(i, signature.length + 1)));
  }
  return signature.slice(0, n);
}

console.log(tribonacci([0, 0, 1], 10));
