days = [1, 2, 8, 9, 10, 11, 12, 15, 18, 22, 24]
cases = [1, 1, 3, 8, 9, 15, 25, 52, 121, 428, 904]

x = days
y = cases

n = x.size

sum_xy = 0

x.each_with_index do |value, index|
  sum_xy += value * y[index]
end

sum_x = x.sum

sum_y = y.sum

sum_squad_x = 0

x.each do |value|
  sum_squad_x += value.round ^ 2
end

sum_x_squad = x.sum.round ^ 2

alfa = ((5 * sum_xy) - (sum_x * sum_y)) / ((5 * sum_squad_x) - sum_x_squad)

beta = y.sum / n - (alfa * x.sum / n)

result = alfa * 50 + beta

p result.abs
