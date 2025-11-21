package main

import "fmt"

func main() {
	p := 34
	q := 20

	// Addition
	result1 := p + q
	fmt.Printf("Result of p + q = %d", result1)

	// Subtraction
	result2 := p - q
	fmt.Printf("\nResult of p - q = %d", result2)

	// Multiplication
	result3 := p * q
	fmt.Printf("\nResult of p * q = %d", result3)

	// Division
	result4 := p / q
	fmt.Printf("\nResult of p / q = %d", result4)

	// Modulus
	result5 := p % q
	fmt.Printf("\nResult of p %% q = %d", result5)

	// ‘=='(Equal To)
	result6 := p == q
	fmt.Println(result6)

	// ‘!='(Not Equal To)
	result7 := p != q
	fmt.Println(result7)

	// ‘<‘(Less Than)
	result8 := p < q
	fmt.Println(result8)

	// ‘>'(Greater Than)
	result9 := p > q
	fmt.Println(result9)

	// ‘>='(Greater Than Equal To)
	result10 := p >= q
	fmt.Println(result10)

	// ‘<='(Less Than Equal To)
	result11 := p <= q
	fmt.Println(result11)

	// logical operations
	if p != q && p <= q {
		fmt.Println("True")
	}

	if p != q || p <= q {
		fmt.Println("True")
	}

	if !(p == q) {
		fmt.Println("True")
	}

	// & (bitwise AND)
	result12 := p & q
	fmt.Printf("Result of p & q = %d", result12)

	// | (bitwise OR)
	result13 := p | q
	fmt.Printf("\nResult of p | q = %d", result13)

	// ^ (bitwise XOR)
	result14 := p ^ q
	fmt.Printf("\nResult of p ^ q = %d", result14)

	// << (left shift)
	result15 := p << 1
	fmt.Printf("\nResult of p << 1 = %d", result15)

	// >> (right shift)
	result16 := p >> 1
	fmt.Printf("\nResult of p >> 1 = %d", result16)

	// &^ (AND NOT)
	result17 := p &^ q
	fmt.Printf("\nResult of p &^ q = %d", result17)

	// “=”(Simple Assignment)
	p = q
	fmt.Println(p)

	// “+=”(Add Assignment)
	p += q
	fmt.Println(p)

	//“-=”(Subtract Assignment)
	p -= q
	fmt.Println(p)

	// “*=”(Multiply Assignment)
	p *= q
	fmt.Println(p)

	// “/=”(Division Assignment)
	p /= q
	fmt.Println(p)

	// “%=”(Modulus Assignment)
	p %= q
	fmt.Println(p)

	// Using address of operator(&) and pointer indirection(*) operator
	a := 4
	b := &a
	fmt.Println(*b)
	*b = 7
	fmt.Println(a)
}
