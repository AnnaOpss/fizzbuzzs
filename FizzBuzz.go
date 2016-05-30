package main

import "fmt"

func FizzBuzz(n int) (ret string) {
	if n%3 == 0 {
		ret += "Fizz"
	}
	if n%5 == 0 {
		ret += "Buzz"
	}
	if ret == "" {
		ret = fmt.Sprintf("%v", n)
	}
	return
}

func main() {

}
