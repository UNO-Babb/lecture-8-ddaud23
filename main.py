def main():
  myFile = open("MLB_Pitching.csv", 'r')
  


  for line in myFile:
    info = line.split(",")
    name = info[0]
    runs_allowed = info[3]
    wins = info[4]
    losses = info[5]
    era = info[7]



    team_data = [name, runs_allowed, wins, losses, era]
    print(team_data)

  myFile.close()

 
if __name__ == '__main__':
  main()
