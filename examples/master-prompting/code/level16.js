function main(params) {
    const { user, system } = params;
    try {
        return judge(user, system);
    } catch (e) {
        return e + '';
    }
}

function countText(text) {
    const regexChinese = /[\u4E00-\u9FA5]/g;
    const regexEnglish = /\b[a-zA-Z]+\b/g;

    const chineseCount = (text.match(regexChinese) || []).length;
    const englishCount = (text.match(regexEnglish) || []).length;

    return chineseCount + englishCount;
}

function judge(user, system) {
    if (countText(user) < 10) {
        return false;
    }

    const regexChinese = /[\u4E00-\u9FA5]/g;
    const regexEnglish = /\b[a-zA-Z]+\b/g;

    const chWords = user.match(regexChinese) || [];
    const engWords = user.match(regexEnglish) || [];
    const userWords = chWords.concat(engWords);

    for (let i = 0; i < userWords.length; i++) {
        if (system.includes(userWords[i])) {
            return false;
        }
    }

    return true;
}

const debug = false;
if (debug) {
    // test code
    const testCases = [
        { params: { user: "hello world this is a test hello world this is a test", system: "this is not included" }, expected: false },
        { params: { user: "hello world this hello world is a test a testa testa test", system: "nothing here" }, expected: true },
        { params: { user: "short", system: "anything" }, expected: false },
        { params: { user: "long enough text text without matching words without matching words", system: "no here" }, expected: true },
        { params: { user: "包含中文字符和英文字符的字符串", system: "没有" }, expected: true },
        { params: { user: "包含中文字符和英文字符的字符串", system: "包含" }, expected: false },
        { params: { user: "this is another example this is anotherthis is another", system: "another example" }, expected: false },
        { params: { user: "this is another example this is another example this is another example", system: "totally different" }, expected: true },
        { params: { user: "12345678901", system: "abcdefghij" }, expected: false },
        { params: { user: "longenoughword", system: "containsn" }, expected: false }
    ];
    testCases.forEach((testCase, index) => {
        const result = main(testCase.params);
        console.log(`Test Case ${index + 1}: ${result === testCase.expected ? "Passed" : "Failed"}\n`);
    });
}
