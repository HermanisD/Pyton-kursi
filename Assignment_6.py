text = "X-DSPAM-Confidence:    0.8475"
num=text.find(":")
floating=float(text[num+1:])
print(floating)