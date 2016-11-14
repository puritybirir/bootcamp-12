def find_max_min(number_list):
  result=[]
  if min(number_list) != max(number_list):
    result.append(min(number_list))
    result.append(max(number_list))
  else:
    result.append(len(number_list))
  return result