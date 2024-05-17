function main(params) {
    const {user, system} = params;
    return judge(user, system);
}
// 
function judge(user, system) {
    const num = Number(user);
    if (num <= 1 || isNaN(num)) return false;
    const sqrt = Math.sqrt(num);
    return Number.isInteger(sqrt) && system.includes(sqrt.toString());
}

const debug = false;

if (debug == true) {
    const testCases = [
        { params: { user: "4", system: "the square root is 2" }, expected: true },
        { params: { user: "1", system: "the square root is 1" }, expected: false },
        { params: { user: "16", system: "I have 4 apples" }, expected: true },
        { params: { user: "20", system: "I have 4 apples" }, expected: false },
        { params: { user: "0", system: "Zero is not valid" }, expected: false },
        { params: { user: "9", system: "The result is 3" }, expected: true },
        { params: { user: "25", system: "Square root is 5" }, expected: true },
        { params: { user: "36", system: "Six is the root" }, expected: false },
        { params: { user: "49", system: "The answer is 7" }, expected: true },
        { params: { user: "64", system: "Square root equals 8" }, expected: true },
    ];

    testCases.forEach((testCase, index) => {
        const result = main(testCase.params);
        console.log(`Test Case ${index + 1}: ${result === testCase.expected ? "Passed" : "Failed"}`);
    });
}
