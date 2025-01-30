times =['1:27.95', '1:21.07', '1:30.96', '1:23.22']
# Start with the string
first = times[0]

# Extract the comment parts: start with the minutes value
minutes, rest = first.split(":")
# Extract the component parts: grab the seconds ande hundredths values
seconds, hundredths = rest.split(".")

# Convert the strings to numbers with the help of another BIF called 
# "int", then perform the calculation
converted_time = (int(minutes) * 60 * 100) + (int(seconds) * 100) + int(hundredths)
print("test")
# Display the result
print(converted_time)