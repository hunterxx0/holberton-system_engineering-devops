#!/usr/bin/env ruby
S =  ARGV[0].scan(/(?<=from:)\S+\b/).join
TO = ARGV[0].scan(/(?<=to:)\S+\b/).join
FL = ARGV[0].scan(/(?<=flags:)\S+\b/).join
puts (S + "," + TO + "," + FL)
