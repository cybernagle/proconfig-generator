function main(params) {
    const { user, system } = params;
    return judge(user, system);
}

function judge(user, system) {
    const forbiddenWords = ['dog', '狗'];

    const regexChinese = /[\u4E00-\u9FA5]/g;
    const regexEnglish = /\b[a-zA-Z]+\b/g;

    const uwc = user.match(regexChinese) || [];
    const uwe = user.match(regexEnglish) || [];
    const userWords = [...uwc ,  ...uwe];
    const swc = system.match(regexChinese) || [];
    const swe = system.match(regexEnglish) || [];
    const systemWords = [...swc ,  ...swe];

    const containsForbiddenWords = forbiddenWords.some(word => user.includes(word));

    const userWordCount = userWords.length;
    const systemContainsRequiredWords = forbiddenWords.some(word => system.includes(word));

    const wordCount = forbiddenWords.reduce((count, word) => count + (system.match(new RegExp(word, 'g')) || []).length, 0);

    return !containsForbiddenWords &&
        userWordCount <= 10 &&
        systemContainsRequiredWords &&
        wordCount >= userWordCount * 2;
}

// 测试代码
const debug = false;
if (debug) {
  const testCases = [
    { params: { user: "hello world", system: "dog dog dog dog" }, expected: true },
    { params: { user: "你好 世界的", system: "狗 狗 狗 狗" }, expected: false },
    { params: { user: "hello world", system: "dog dog dog" }, expected: false },
    { params: { user: "你好 世界", system: "狗 狗 狗" }, expected: false },
    { params: { user: "hello world 你好 世界", system: "dog dog dog dog 狗 狗 狗 狗" }, expected: false },
    { params: { user: "hello world 你好 世界", system: "狗 狗 狗 狗 狗 狗 狗 狗" }, expected: false },
    { params: { user: "hello world 你好 世界 你好", system: "狗 狗 狗 狗 狗 狗 狗 狗 狗 狗 狗 狗 dog dog dog dog dog " }, expected: true },
    { params: { user: "dog world", system: "dog dog dog dog" }, expected: false },
    { params: { user: "hello", system: "dog dog dog dog dog dog dog dog dog dog" }, expected: true },
    { params: { user: "你好", system: "狗 狗 狗 狗 狗 狗 dog dog dog 狗 狗" }, expected: true },
  ];

  testCases.forEach((testCase, index) => {
    const result = main(testCase.params);
    console.log(`Test Case ${index + 1}: ${result === testCase.expected ? "Passed" : "Failed"}\n`);
  });
}
