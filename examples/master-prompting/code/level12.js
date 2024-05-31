function main(params) {
    const {user, system} = params;
    userCount = countText(user);

    if (userCount > 10) {
        return user == system;
    }

    return false;

}

function countText(text) {
    const regexChinese = /[\u4E00-\u9FA5]/g;
    const regexEnglish = /\b[a-zA-Z]+\b/g;

    const chineseCount = (text.match(regexChinese) || []).length;
    const englishCount = (text.match(regexEnglish) || []).length;

    return chineseCount + englishCount;
}


const debug = false;
if (debug) {
    const testCases = [
        {
            params: {user: "hello world hello worldhello worldhello worldhello worldhello worldhello worldhello worldhello worldhello world!", system: "hello world hello worldhello worldhello worldhello worldhello worldhello worldhello worldhello worldhello world!"},
            expected: true
        },
        {
            params: {user: "hello world!hello world!hello world!hello world!hello world!hello world!hello world!hello world!", system: "hello world!hello world!hello world!hello world!hello world!hello world!hello world!hello world"},
            expected: false
        },
        {
            params: {user: "short", system: "short"},
            expected: false
        },
        {
            params: {user: "short", system: "different"},
            expected: false
        },
        {
            params: {user: "你好，hello world!世界,你好世界你好世界", system: "你好，hello world!世界,你好世界你好世界"},
            expected: true
        },
        {
            params: {user: "你好，hello world!", system: "你好，different world!"},
            expected: false
        }
    ];

    testCases.forEach(({params, expected}, index) => {
        const result = main(params);
        console.log(`Test Case ${index + 1}: ${result === expected ? "Passed" : "Failed"}`);
    });

}
