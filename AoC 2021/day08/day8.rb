file = File.open('day08/a.in')
data = file.read.chomp
file.close

def part1 data
  data.scan(/\|.*/).sum do |line|
    line
    .scan(/\w+/)
    .count { |x| [2, 3, 4, 7].include? x.length }
  end
end

def convert perm, str
  h = {
    'abcefg' => 0,
    'cf' => 1,
    'acdeg' => 2,
    'acdfg' => 3,
    'bcdf' => 4,
    'abdfg' => 5,
    'abdefg' => 6,
    'acf' => 7,
    'abcdefg' => 8,
    'abcdfg' => 9
  }
  strTranslated = str.tr(perm, 'abcdefg').chars.sort.join
  h[strTranslated] || -1
end

def getKey digits
    digits = digits.split(' ')
    ('a'..'g').to_a.permutation.find do |perm|
      perm = perm.join
      digits.sum { |w| convert perm, w } == 45
    end
    .join
end

def part2 data
  data.split("\n").sum do |line|
    front, back = line.split(" | ")
    key = getKey front
    back.split(' ').map { |w| convert key, w } .join.to_i
  end
end

p part1 data
p part2 data
# part2 takes around 5 seconds
