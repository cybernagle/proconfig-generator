function main(params) {
    const { user, system } = params;
    try{
        return judge(user, system);
    } catch (e) {
        return e+'';
    }
}

function judge(user, system) {
    var cUser = countText(user);
    if (cUser < 10) {
        return false;
    }
    return user == system.split(/(\s+)/).map(part => /[\u4e00-\u9fa5]/.test(part) ? part.split('').reverse().join('') : part).reverse().join('');

}

function countText(text) {
    const regexChinese = /[\u4E00-\u9FA5]/g;
    const regexEnglish = /\b[a-zA-Z]+\b/g;

    const chineseCount = (text.match(regexChinese) || []).length;
    const englishCount = (text.match(regexEnglish) || []).length;

    return chineseCount+englishCount;
}

const debug = false;
if (debug) {
    console.log(main({user: '你好 english', system: ''})); // false, because word count is less than 10
    console.log(main({user: '你好 english', system: 'english 好你'})); // false, because it matches the reversed system string
    console.log(main({user: '你好 world', system: ''})); // false, because word count is less than 10
    console.log(main({user: 'one two three four five six seven eight nine ten eleven', system: ''})); // false, because user does not match reversed system string
    console.log(main({user: 'one two three four five six seven eight nine ten eleven', system: 'eleven ten nine eight seven six five four three two one'})); // true, because user matches reversed system string
    console.log(main({user: 'This is a test with more than ten words to check the function correctly', system: 'correctly function the check to words ten than more with test a is This'})); // true, because user matches reversed system string
    console.log(main({user: 'This is a test with less than ten words', system: ''})); // false, because word count is less than 10
}

