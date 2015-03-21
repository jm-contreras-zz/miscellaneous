# Import module
from datetime import datetime as dt

def main(then):
    
    # Declare now and then
    now = dt.now()
    then = dt.strptime(then, '%b %d %Y %I:%M%p')
    
    # Compute delta
    dlt = then - now
    
    # Determine time values
    v = [dlt.days, dlt.seconds // 3600, dlt.seconds // 60 % 60, dlt.seconds % 60]
    
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

if __name__ == '__main__':
    
    main(str(raw_input('When will you see your sweetheart next? ')))
