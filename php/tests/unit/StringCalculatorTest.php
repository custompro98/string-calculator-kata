<?php

namespace Kata\Tests\Unit;

use \PHPUnit\Framework\TestCase;
use \Kata\StringCalculator;

class StringCalculatorTest extends TestCase
{
    /** @var StringCalculator $subject */
    private $subject;

    public function setUp(): void
    {
        $this->subject = new StringCalculator;
    }

    public function testFailing()
    {
        $this->assertEquals(true, false);
    }
}
