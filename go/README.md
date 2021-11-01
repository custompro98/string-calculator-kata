String Calculator Kata
============
Setup: 
* Install [golang](https://golang.org/doc/install)
* Install [gotestsum](https://github.com/gotestyourself/gotestsum) (`go get gotest.tools/gotestsum`)
* Install [filewatcher](https://github.com/dnephin/filewatcher) (`go get github.com/dnephin/filewatcher`)
* `go mod download`
  
Run: `filewatcher --directory pkg --exclude '**/*.swp' gotestsum './${dir}'`

Your tests are in `pkg/calculator/string_calculator_test.go` and your function is defined in `pkg/calculator/string_calculator.go`
