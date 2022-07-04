function countDevelopers(list) {
    // your awesome code here :)
    let count = 0;
    list.forEach(element => {
        if(element.continent === 'Europe' && element.language === 'JavaScript'){
            count++
        }
    });
    return count
}

const list2 = [
    { firstName: 'Oliver', lastName: 'Q.', country: 'Australia', continent: 'Oceania', age: 19, language: 'HTML' },
    { firstName: 'Lukas', lastName: 'R.', country: 'Austria', continent: 'Europe', age: 89, language: 'HTML' }
  ]

console.log(countDevelopers(list2))