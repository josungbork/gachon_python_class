import my_module

print ("Enter a temperature in Celsius : "),
celsius = float(raw_input())
fahrenheit = my_module.c_to_f(celsius)
print "That's ", fahrenheit, " degrees Fahrenheit"

