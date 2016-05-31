function fizzbuzz(n) {
	console.log(i%3 === 0 && i%5 == 0 ? "FizzBuzz": i%3 === 0 ? "Fizz" : i%5 === 0 ? "Buzz" : i);
}

function betterFizzbuzz(n) {
	var result = "";
	if (n % 3 === 0)
		result += "Fizz";
	if (n % 5 === 0)
		result += "Buzz";
	console.log(result || n);
}

for(var i = 0; i < 100; i++){
	fizzbuzz(i);
}

console.log();

for(var i = 0; i < 100; i++){
	betterFizzbuzz(i);
}
