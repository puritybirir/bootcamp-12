def words(string):
  keys=[]
  string_words = string.split()
  [keys.append(word) for word in string_words if word not in keys]
  
  results={}
  
  for key in keys:
    i=0
    count=0
    while i < len(string_words):
      if key == string_words[i]:
        count = count+1
      i = i+1
    results[key]=count
  return results