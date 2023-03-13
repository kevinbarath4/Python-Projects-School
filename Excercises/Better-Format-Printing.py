companyName = "Anna's coffee shop"

print()
print("{0:.^60s}".format(companyName.upper()))
print()
print("{0:^60s}".format("Our special for today"))
print("{0:_^60s}".format(''))
print()
print("{0:20s}\t{2}\t${1:>10.2f}".format("Anna's soup", 9.99, "Ask us about it..."))
print("{0:20s}\t\t\t\t${1:>10.2f}".format("Dinner for 2", 17.99))
print("{0:20s}\t{2}\t${1:>10,.2f}".format("Dinner for 4", 1001.99, "20 days, every day!"))
print("\n")