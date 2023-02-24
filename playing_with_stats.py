import statistics

list_of_numbers = (2, 5.6, 89, 4.99835, 34, 76482, 0.00001, 483598435, 5.2, 1.33, 1.2, 0, 1.55)
# print(statistics.median(list_of_numbers))
# print(statistics.mode(list_of_numbers))
# print(statistics.harmonic_mean(list_of_numbers))
# print(statistics.median_low(list_of_numbers))
# print(statistics.mean(list_of_numbers))

a = (statistics.median(list_of_numbers))
b = (statistics.mode(list_of_numbers))
c = (statistics.harmonic_mean(list_of_numbers))
d = (statistics.median_low(list_of_numbers))
e = (statistics.mean(list_of_numbers))

print(d + e)
print(sorted(list_of_numbers, key=float,))
print(sorted(list_of_numbers, key=float, reverse=True))

gay_people = ("connie", "erol", "alex", "kinjal", "drea", "brielle", "sanda")
straights = ("echo", "eiliyah", "akshay", "chloe", "jeremy", "talia","lara", "mark")
those_who_transcend = ("tai", "liam", "alex", "nate")

x = input(" print your person")

if x == gay_people:
    print("this one's a queer")

elif x == straights:
    print("ew a straight bitch, hate those guys")

elif x == those_who_transcend:
    print("wowza, you got a rare one. store it")