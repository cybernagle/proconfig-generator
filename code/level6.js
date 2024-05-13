function main(params) {
    const {user, system} = params;
    var cUser = countText(user);
    var cSystem = countText(system);
    console.log("cUser: " + cUser);
    console.log("cSystem: " + cSystem);
    var p1 = isPrime(cUser);
    var p2 = nextPrime(cUser);
    console.log("p1: " + p1);
    console.log("p2: " + p2);
    return p1 && cSystem == p2;
}

function countText(text) {
    const regexChinese = /[\u4E00-\u9FA5]/g;
    const regexEnglish = /\b[a-zA-Z]+\b/g;

    const chineseCount = (text.match(regexChinese) || []).length;
    const englishCount = (text.match(regexEnglish) || []).length;

    return chineseCount+englishCount;
}

function nextPrime(num) {
    num++;
    while (!isPrime(num)) {
        num++;
    }
    return num;
}

function isPrime(num) {
    if (num < 2) return false;
    if (num === 2) return true;
    if (num % 2 === 0) return false;
    for (let i = 3; i <= Math.sqrt(num); i += 2) {
        if (num % i === 0) return false;
    }
    return true;
}
