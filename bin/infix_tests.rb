#!/usr/bin/env ruby

# Script to convert test files to sorted test files by infixing test
# method names with a monotonically increasing index so the test run
# in the order they appear in the file. Otherwise, the tests will run
# in alphabetical order.

index = 10
increment = 10
re = %r(^(\s*def\s+test_)(\w.*))

ARGF.each_line {|line|
  m = line.match re
  if m
    puts "#{m[1]}#{"%03d" % index}_#{m[2]}"
    index += increment
  else
    puts line
  end
}
