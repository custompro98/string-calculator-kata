#!/usr/bin/perl

use strict;
use warnings;

use File::Basename qw(dirname);
use Cwd  qw(abs_path);
use lib dirname(dirname abs_path $0) . '/lib';

use StringCalculator qw(add);
# HINT: update me every time you add a test to avoid
# '# Looks like you planned 1 test but ran n.'
use Test::Simple tests => 1;

ok( 1 eq 0, 'true is true' );
