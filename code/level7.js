function main(params) {
    const {user, system} = params;
    return hasNumberExceedingXByMoreThan1000(system, user)
}

function isInteger(str) {
    return /^-?\d+$/.test(str);
}

function hasNumberExceedingXByMoreThan1000(str, xStr) {
    if (!isInteger(xStr)) {
        return false;
    }
    const x = parseInt(xStr, 10);
    const matches = str.match(/\d+/g) || [];
    return matches.some(numStr => {
        const num = parseInt(numStr, 10);
        return num > x && num - x > 1000;
    });
}

console.log(main({user: "1", system: "1+1=900"}))
