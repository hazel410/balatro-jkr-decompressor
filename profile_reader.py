import re

stakeList = ["none", "white", "red", "green", "black", "blue", "purple", "orange", "gold"]
stakeCount = [0,0,0,0,0,0,0,0,0]

# Match stake names to index
def getStakeIndex(stake):
    match stake:
        case "_white":
            return 1
        case "_red":
            return 2
        case "_green":
            return 3
        case "_black":
            return 4
        case "_blue":
            return 5
        case "_purple":
            return 6
        case "_orange":
            return 7
        case "_gold":
            return 8
# get highest completed stake for a joker
def getHighestStake(stakes):
    highest = 0 # no sticker
    for stake in stakes:
        index = getStakeIndex(stake)
        if  index > highest:
            highest = index
    stakeCount[highest] += 1
    return highest

def moreJokers(txt):
    x = re.search("\"j_[a-z0-9]+\"]=", txt) 
    if x != None:
        return True
    return False

def main():
    decompressed_path = 'decompressed/profile_decoded.txt'
    with open(decompressed_path, 'r') as file:
      txt = file.read()  
    
    # Cut off everything before joker usage
    joker_usage = re.search("\"joker_usage\"]={", txt)
    txt = txt[joker_usage.end():]
    # End at next usage statistics (maybe hand_usage)
    next_usage = re.search("_usage\"]={", txt)
    txt = txt[:next_usage.start()]
    joker_list = list()
    # Loop over each joker
    while (moreJokers(txt)):
        # get name of joker
        joker = re.search("\"j_[a-z0-9_]+\"", txt).group()
        
        # parse through joker stake wins
        wins = re.search("wins_by_key\"]={", txt)
        txt = txt[wins.end():]
        end = re.search("}", txt).start()
        # temp string with containing only stake wins for current joker
        temp = txt[:end]
        stakes = re.findall("_[a-z]+", temp)
        highest = getHighestStake(stakes)
        joker_stake = str(joker + " = " + stakeList[highest])
        joker_list.append(joker_stake)
    print(joker_list)
    print(stakeCount)
    
main()

  


  
  
  










