String Calculator Kata
============
Setup: 
* Install [filewatcher](https://github.com/dnephin/filewatcher) (`go install github.com/dnephin/filewatcher`)
* Done. It's Perl, dude.

Setup to avoid system Perl:
* Install [plenv](https://github.com/tokuhirom/plenv)
* Install [plenv-contrib](https://github.com/miyagawa/plenv-contrib) (using the bootstrap method)
* Install [cpanm](https://metacpan.org/pod/App::cpanminus#Installing-to-local-perl-(perlbrew,-plenv-etc.)) (using quickstart)
  * Executable after `plenv use ...`
  * `cpanm local::lib`
  * `cpanm --installdeps .`
* Manage dependencies with [cpanfile](https://metacpan.org/dist/Module-CPANfile/view/lib/cpanfile.pod)
  
Run: `perl bin/StringCalculator.pl`
Run: `filewatcher --directory lib --directory bin --exclude '**/*.swp' perl bin/StringCalculatorTest.pl`

Run (with plenv):
```
plenv lib create string-calculator-kata
plenv use 5.38.2@string-calculator-kata
cpanm local::lib

filewatcher --directory lib --directory bin --exclude '**/*.swp' perl bin/StringCalculatorTest.pl
```

Your tests are in `bin/StringCalculatorTest.pl` and your function is defined in `lib/StringCalculator.pm`
