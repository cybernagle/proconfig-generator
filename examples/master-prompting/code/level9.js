function main(params) {
    const { user, system } = params;
    try{
        return judge(user, system);
    } catch(e) {
        return e+'';
    }
}

function judge(user, system) {
  const forbiddenDigits = ['1', '4', '5'];
  const containsForbiddenDigits = forbiddenDigits.some(digit => user.includes(digit));
  const isSystemMatch = system === "114514";
  return !containsForbiddenDigits && isSystemMatch;
}

// test code
const debug = false;
if (debug) {
  const testCases = [
    { params: { user: "236789", system: "114514" }, expected: true },
    { params: { user: "123456", system: "114514" }, expected: false },
    { params: { user: "236789", system: "123456" }, expected: false },
    { params: { user: "6789", system: "114514" }, expected: true },
    { params: { user: "6781", system: "114514" }, expected: false },
    { params: { user: "6789", system: "114515" }, expected: false },
  ];

  testCases.forEach((testCase, index) => {
    const result = main(testCase.params);
    console.log(`Test Case ${index + 1}: ${result === testCase.expected ? "Passed" : "Failed"}`);
  });
}
