function main(params) {
    const { user, system } = params;
    try{
        return judge(user, system);
    } catch (e) {
        return e+'';
    }
}


function isPositiveIntegerGreaterThanOne(number) {
    const x = parseInt(number, 10);
    return x > 1;
}

function findNumbersInString(str) {
    return str.match(/\d+/g) ? str.match(/\d+/g).map(Number) : [];
}

function judge(x, str) {
    if (!isPositiveIntegerGreaterThanOne(x)) {
        return false;
    }

    const numbers = findNumbersInString(str);
    return numbers.some(y => Math.abs(y - x) === 1);
}

const debug = true;
if (debug) {
    // test code
    const testCases = [
        { params: { user: "5", system: "1 2 3 4 6 7 8" }, expected: true },
        { params: { user: "3", system: "1 2 4 5 6" }, expected: true },
        { params: { user: "1", system: "1 2 3 4 5" }, expected: false },
        { params: { user: "0", system: "1 2 3 4 5" }, expected: false },
        { params: { user: "2", system: "3 4 5 6" }, expected: true },
        { params: { user: "10", system: "9 11 12 13" }, expected: true },
        { params: { user: "15", system: "14 16 17 18" }, expected: true },
        { params: { user: "4", system: "5 6 7 8" }, expected: true },
        { params: { user: "abc", system: "1 2 3 4 5" }, expected: false },
        { params: { user: "5", system: "a b c d e" }, expected: false }
    ];
    testCases.forEach((testCase, index) => {
        const result = main(testCase.params);
        console.log(`Test Case ${index + 1}: ${result === testCase.expected ? "Passed" : "Failed"}\n`);
    });
}


