let a = 1, b = 1;

alert( ++a ); // 2
alert( b++ ); // 1

alert( a ); // 2
alert( b ); // 2

let a = 2;

let x = 1 + (a *= 2); // 5

"" + 1 + 0 = "10" // (1)
"" - 1 + 0 = -1 // (2)
true + false = 1
6 / "3" = 2
"2" * "3" = 6
4 + 5 + "px" = "9px"
"$" + 4 + 5 = "$45"
"4" - 2 = 2
"4px" - 2 = NaN
"  -9  " + 5 = "  -9  5" // (3)
"  -9  " - 5 = -14 // (4)
null + 1 = 1 // (5)
undefined + 1 = NaN // (6)
" \t \n" - 2 = -2 // (7)

let a = prompt("First number?", 1);
let b = prompt("Second number?", 2);

alert(+a + +b); // 3S