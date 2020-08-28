'''

If a runner runs 10 miles in 30 minutes and 30 seconds,
What is his/her average speed in kilometers per hour? (Tip: 1 mile = 1.6 km)

'''

# how many km in 30 min 30 sec
distance = 10 * 1.6
print("In 30 min and 30 sec he will run ", distance)
# how many km per 30 sec
timing = 30 * 2 + 1
print(timing)

# how many km per min
distance_per_half_min = distance / timing
print(distance_per_half_min)
distance_per_min = distance_per_half_min * 2
print(distance_per_min)
# how many km per hour
print("Average speed is ", distance_per_min * 60)
