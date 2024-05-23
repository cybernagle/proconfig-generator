function main(params) {
    const {user, system} = params;
    var cUser = containsDogWord(user); // should be false
    var cSystem = countDogWords(system);
    return !cUser && cSystem >= 3
}

function containsDogWord(str) {
    const dogWords = ['狗', 'dog'];
    return dogWords.some(dogWord => new RegExp(dogWord, 'i').test(str));
}

function countDogWords(str) {
    const dogWords = ['狗', 'dog'];
    let count = 0;
    dogWords.forEach(dogWord => {
        const match = str.match(new RegExp(dogWord, 'gi'));
        if (match) {
            count += match.length;
        }
    });
    return count;
}
