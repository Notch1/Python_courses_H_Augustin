text = "X-DSPAM-Confidence:    0.8475";
space = text.find(':')
num = text[space+4:]
# without turning num into a float, it will print 0.8475 but as a string
print(float(num))

