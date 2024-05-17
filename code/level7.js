function main(params) {
    const {user, system} = params;
    return hasNumberExceedingXByMoreThan1000(system, user);
}

function isIntegerGreaterThanOne(str) {
    const num = Number(str);
    return Number.isInteger(num) && num > 1;
}

function hasNumberExceedingXByMoreThan1000(str, xStr) {
    if (!isIntegerGreaterThanOne(xStr)) {
        return false;
    }
    const x = parseInt(xStr, 10);
    const matches = str.match(/\d+/g) || [];
    return matches.some(numStr => {
        const num = parseInt(numStr, 10);
        return num > x && num - x > 1000;
    });
}

const debug = false;

if  (debug == true) {
    console.log(main({user: "2", system: "1+1=1900"}));
}

