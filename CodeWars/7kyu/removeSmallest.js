function removeSmallest(numbers) {
    const minimum = Math.min(...numbers)
    numbers.splice(numbers.indexOf(minimum),1)
    return numbers

}
