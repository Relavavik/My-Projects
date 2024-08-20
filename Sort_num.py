def main():
  prompt= input().strip(" ")
  x = prompt.split(",")
  i = list(map(int, x))
  st = []
  nd = []
  rd = []
  for u in i:
    if 5<=u < 10:
      st.append(u)
    elif 10 <= u < 15:
      nd.append(u)
    else:
      rd.append(u)
  print("Total number of Elements", len(i))
  print("Lowest number :", min(i))
  print("Highest number:", max(i))
  print(f" Frequency of (5-9) = {len(st)}")
  print(f" Frequency of (10-14) = {len(nd)}")
  print(f" Frequency of (15-19) = {len(rd)}")
  print(f"(5-9)   :{st}",f"(10-14) :{nd}",f"(15-19) :{rd}",sep="\n")
main()
