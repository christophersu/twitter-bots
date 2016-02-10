import json

bots = None
with open('twitter_bots.json') as f:    
    bots = json.load(f)["bots"]

if __name__ == '__main__':
  print bots