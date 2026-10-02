package main

import "fmt"
import "os"

func main() {
	// fmt.Println("Hello world!")
	files, _ := os.ReadDir(".")

	for _, file := range files {
		content, err := os.ReadFile(file.Name())
		if err != nil {
			fmt.Println(err)
		}

		fmt.Println(file.Name() + ": \n")
		fmt.Println(string(content))
	}
}