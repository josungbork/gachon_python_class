x = int(raw_input())
try:
    print 10 / x
except ZeroDivisionError:
        print 'Unable to caluate - divide by zero'
else:
    print 'The result is ', str(10 / x)
