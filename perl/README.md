String Calculator Kata
============
Setup: 
* Install [filewatcher](https://github.com/dnephin/filewatcher) (`go install github.com/dnephin/filewatcher`)
* Done. It's Perl, dude.
  
Run: `perl bin/StringCalculator.pl`
Run: `filewatcher --directory lib --directory bin --exclude '**/*.swp' perl bin/StringCalculatorTest.pl`

Your tests are in `bin/StringCalculatorTest.pl` and your function is defined in `lib/StringCalculator.pm`
