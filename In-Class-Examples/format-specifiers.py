# format specifier for type
print("{0:d}".format(42))           # integer
print("{0:f}".format(3.45))         # float
print("{0:s}".format("books"))      # string
print("{0:%}".format(0.13))         # percentage

# minimum width specifier
print('{0:8d}'.format(123))          # min width set at 8; output: '     123'

# alignment specifier
print("{0:^14s}".format("ha"))       # string, alocated width 14, centered; output: '      ha      '

# padding character specifier
print("{0:*^14s}".format("ha"))     # string, alocated width 14, centered; filler: *; output: '******ha******'

# grouping separator specifier
print("{0:,d}".format(1234567))     # adding a comma as a thousand-separator; output: '1,234,567'

# different format specifiers combined, in the correct order  [fill][align][width][group][.prec][type]
print("{0:-^20,.2f}".format(1231231.99))
# a float value displayed with 2 decimal places, using , as thousand separator.
# Minimum width of the output set to 20; if shorter, center it, and padd with '-'