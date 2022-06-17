# Declare a named constant for array size here.
MAX_AVERAGES = 8
x = 0
# Declare array here.
averages = [0,0,0,0,0,0,0,0]
# Write a loop to get batting averages from user and assign to array.
while x < MAX_AVERAGES:
    averageString = input("Enter a batting average: ")
    battingAverage = float(averageString)
    # Assign value to array.
    averages[x] = battingAverage
    x += 1
# Assign the first element in the array to be the minimum and the maximum.
minAverage = averages[0]
maxAverage = averages[0]
# Start out your total with the value of the first element in the array.
total = averages[0]
# Write a loop here to access array values starting with averages[1]
for y in range(1,8):
    # Within the loop test for minimum and maximum batting averages.
    if averages[y] < minAverage:
      minAverage = averages[y]
    if averages[y] > maxAverage:
      maxAverage = averages[y]
    
    # Also accumulate a total of all batting averages.
    total = total + averages[y]

# Calculate the average of the 8 batting averages.
average = total/8

# Print the batting averages stored in the averages array.
print(averages)

# Print the maximum batting average, minimum batting average, and average batting average.
print("Minimum batting average is " + str(minAverage))
print("Maximum batting average is " + str(maxAverage))
print("Average batting average is " + str(average))