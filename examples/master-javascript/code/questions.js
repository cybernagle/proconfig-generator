// ### 简单语法
console.log("Hello World);
// *Bug*: 缺少结束引号。

let x = 10 console.log(x);
// Bug: 缺少分号。

function add(a, b) { return a + b;

// *Bug*: 缺少函数结束大括号。

let arr = [1, 2, 3; console.log(arr);
// Bug: 数组定义中的分号应为逗号。

if (x = 5) { console.log("x is 5"); }

// *Bug*: 应该是比较运算符 `==` 或 `===`。

// ### 中等语法
let x = "5"; let y = 5; if (x === y) console.log("Equal");
// Bug: === 比较会导致不同类型不相等。

for (let i = 0; i < 10; i++) { i++; }

// *Bug*: 循环体内不应再自增 `i`。

let obj = { a: 1, b: 2; console.log(obj);
// Bug: 对象定义中的分号应为逗号。

let str = 'Hello; console.log(str);

// *Bug*: 字符串缺少结束引号。

function greet(name) { return "Hello, " + name; }
console.log(greet());
// Bug: greet 函数调用缺少参数。

// 复杂语法
let x = [1, 2, 3]; x.map(n => { return n * 2 });

// *Bug*: `map` 函数没有存储或输出结果。

let obj = { a: 1, b: 2 }; delete obj.a; console.log(obj.a);
// Bug: obj.a 已被删除，输出应该是 undefined。

let x = 10; function foo() { x = 20; } console.log(x);

// *Bug*: `foo` 函数未被调用。

let x = 10; function foo() { let x = 20; } foo(); console.log(x);
// Bug: foo 内部的 x 是局部变量，不影响外部 x。

let arr = [1, 2, 3]; arr.forEach(n => n * 2); console.log(arr);

// *Bug*: `forEach` 不返回新数组，原数组未改变。

// ### 更复杂语法
let obj = { a: 1, b: 2 }; let { a, b, c } = obj; console.log(c);
// Bug: c 在 obj 中不存在，输出 undefined。

function add(x, y = 10) { return x + y; } console.log(add(5, ));

// *Bug*: `add` 函数调用中多余的逗号。

let x = 10; try { x.toUpperCase(); } catch(e) { console.log(e); }
// Bug: Number 类型没有 toUpperCase 方法。

let x = 10; if (x > 5) { let y = 20; } console.log(y);

// *Bug*: `y` 是块级作用域变量，在块外不可访问。

let arr = [1, 2, 3]; let newArr = arr.push(4); console.log(newArr);
// Bug: push 返回新长度而不是新数组。

