import codecs

string = "68747470733A2F2F66616365626F6F6B"
binary_str = codecs.decode(string, "hex")
print(str(binary_str,'utf-8'))