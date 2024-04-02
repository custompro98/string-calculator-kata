#!/usr/bin/perl

package StringCalculatorTest;

use strict;
use warnings;

use File::Basename qw(dirname);
use Cwd  qw(abs_path);
use lib dirname(dirname abs_path $0) . '/lib';

use StringCalculator qw(add);
use Test::More;

ok( 1 eq 0, 'true is true' );

done_testing();
