def invert_dict(dictionary):
  i_dict = {}
  for key,value in dictionary.items():
    i_dict = {v:k for k,v in dictionary.items()}
  return i_dict
dictionary = {}
num = int(input("enter no of key value pairs:"))
for i in range(num):
  key = input()
  value = input()
  dictionary[key]=value
print("original dict",dictionary)
print("inverted dict:",invert_dict(dictionary))