file = File.open('day09/a.in')
data = file.read.chomp
file.close

data = data.split("\n").map do |line|
  line.chars.map(&:to_i)
end

class PartOne
  def initialize data
    @data = data
    @m = @data.length
    @n = @data[0].length
  end

  def get_height r, c
    (r < 0 || r >= @m || c < 0 || c >= @n) ? nil : @data[r][c]
  end

  def low_point? r, c
    point = get_height r, c
    top = get_height r - 1, c
    bot = get_height r + 1, c
    left = get_height r, c - 1
    right = get_height r, c + 1
    (top.nil? || point < top) && (bot.nil? || point < bot) && (left.nil? || point < left) && (right.nil? || point < right)
  end

  def solve
    result = 0
    @m.times do |r|
      @n.times do |c|
        result += get_height(r, c) + 1 if low_point?(r, c)
      end
    end
    result
  end
end

class PartTwo
  def initialize data
    @data = data
    @m = @data.length
    @n = @data[0].length
    @basins = []
    @visited = Array.new(@m) { Array.new(@n, false) }
  end

  def visit_basin r, c
    if r < 0 || r >= @m || c < 0 || c >= @n || @visited[r][c]
      return
    end
    @visited[r][c] = true
    if @data[r][c] != 9
      @basins[-1] += 1
      visit_basin r + 1, c
      visit_basin r - 1, c
      visit_basin r, c + 1
      visit_basin r, c - 1
    end
  end

  def solve
    @m.times do |r|
      @n.times do |c|
        if @data[r][c] != 9 && !@visited[r][c]
          @basins << 0
          visit_basin r, c
        end
      end
    end
    sorted = @basins.sort
    sorted[-1] * sorted[-2] * sorted[-3]
  end
end

p PartOne.new(data).solve
p PartTwo.new(data).solve
