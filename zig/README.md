String Calculator Kata
============
Setup:
* Install [zig](https://ziglang.org/download/)
* Install [filewatcher](https://github.com/dnephin/filewatcher) (`go install github.com/dnephin/filewatcher`)

Run: `zig test src/string_calculator.zig`
Run: `filewatcher --directory src --exclude '**/*.swp' zig test src/string_calculator.zig`

Your tests are in `src/string_calculator.zig` and your function is defined in `src/string_calculator.zig`
