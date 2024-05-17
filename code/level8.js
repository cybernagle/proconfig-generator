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

    const count = 0;
    const x = parseInt(xStr, 10);
    const matches = str.match(/\d+/g) || [];
    return matches.map(Number).filter(num => num > x && num - x > 1000).length >= 10;
}

const debug = false;

if  (debug == true) {
    // test code
    console.log(main({user: "2", system: "1+1=1900 1900  1900  1900  1900  1900  1900  1900  1900  "}));
    console.log(main({user: "2", system: "1+1=1900 1900  1900  1900  1900  1900  1900  1900  1900  1900  1900  1900  1900 "}));
}

