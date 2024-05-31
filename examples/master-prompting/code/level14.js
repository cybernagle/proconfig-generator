function main(params) {
    const { user, system } = params;
    try{
        return judge(user, system);
    } catch (e) {
        return e+'';
    }
}

function judge(user, system) {
    if (user.includes('1') || user.includes('3') ){
        return false;
    }
    return system=="1+1=3";
}

const debug = false;
if (debug) {
    // test code
    const testCases = [
        {params: { user: "撒发生1阿斯顿发", system: "1+1=3"} , expected: false},
        {params: { user: "你好世界456", system: "1+1=3" }, expected: true},
        {params: { user: "123", system: "1+1=2" } , expected: false},
        {params: { user: "456", system: "1+1=2"} , expected: false},
    ];
    testCases.forEach((testCase, index) => {
        const result = main(testCase.params);
        console.log(`Test Case ${index + 1}: ${result === testCase.expected ? "Passed" : "Failed"}\n`);
    });

}
