function main(params) {
    const {user, system} = params;
    var cUser = countText(user);
    var cSystem = countText(system);
    return cUser <= 3 && cSystem >= 30
}

function countText(text) {
    const regexChinese = /[\u4E00-\u9FA5]/g;
    const regexEnglish = /\b[a-zA-Z]+\b/g;

    const chineseCount = (text.match(regexChinese) || []).length;
    const englishCount = (text.match(regexEnglish) || []).length;

    return chineseCount + englishCount;
}
