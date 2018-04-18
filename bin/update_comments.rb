#!/usr/bin/env ruby

# Script to convert "rerun" Ruby gem syntax to Python "rerun" package syntax

=begin
# Example rerun command:
#	rerun -p '*.py' -cx -- ./test_pig_latin.py -v
=end

re = %r(^#\s*Example rerun command:\n#\s+rerun -p.+(python\s+)((\.\/)?test_[\w_]+\.py) -v\n)
str = ARGF.read

m = str.match(re)
if m
  fname = m[2]
  replacement = <<EOF
# This driver is executable from the command line.  Use the Python
# "rerun" package to re-run the driver whenever files in this
# directory (and its recursive children) are changed or added.
#
#   rerun -v #{fname}
EOF
  puts str.sub(re, replacement)
else
  # puts str
end

