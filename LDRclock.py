# Import module
from datetime import datetime as dt

# Declare now and then
now = dt.now()
then = dt.strptime('Apr 2 2015 10:59PM', '%b %d %Y %I:%M%p')

# Compute delta
delta = then - now

# Determine time values
v = [delta.days, delta.seconds // 3600, delta.seconds // 60 % 60, delta.seconds % 60]

# Determine time units
u = ['days', 'hours', 'minutes', 'seconds']

# Drop 's' from time units, if necessary
for i, this_u in enumerate(u):
    if v[i] == 1:
        u[i] = this_u[:-1]

# Write report
report = 'You will see your sweetheart in {} {}, {} {}, {} {}, and {} {}.'

# Print it
print report.format(v[0], u[0], v[1], u[1], v[2], u[2], v[3], u[3])
