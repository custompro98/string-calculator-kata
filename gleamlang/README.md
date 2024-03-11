String Calculator Kata
============
Setup: 
* Install [gleam](https://gleam.run/getting-started/installing/#installing-gleam)
* Install [erlang](https://gleam.run/getting-started/installing/#installing-erlang)
* Install [rebar3](https://rebar3.org/docs/getting-started/)
* Install [filewatcher](https://github.com/dnephin/filewatcher) (`go install github.com/dnephin/filewatcher`)
  
Run: `gleam test`
Run: `filewatcher --directory src --directory test --exclude '**/*.swp' gleam test`

Your tests are in `test/string_calculator_test.gleam` and your function is defined in `src/string_calculator.gleam`
