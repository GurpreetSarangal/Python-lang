# Convert given time in seconds to time in Hours-Minutes-Seconds
seconds = int(input("Input seconds: "))
hours = int(seconds/3600)
seconds = seconds%3600
minutes = int(seconds/60)
seconds = seconds%60

print(hours,"hr/",minutes,"m/",seconds,"s")