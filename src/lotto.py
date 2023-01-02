import fire
import itertools as it
import hashlib

def combine(picks, repeat=6):
  pcks = parse(picks)
  combinations = [it.combinations(pick, repeat) for pick in pcks]
  unique_picks = dict()
  duplicated_picks = dict()
  for combination in combinations:
    items = list(combination)
    for item in items:
      ordered = sorted(list(item))
      hash = frozenset(ordered)
      if hash not in unique_picks:
        unique_picks[hash] = ordered
      else:
        duplicated_picks[hash] = ordered
  print(len(unique_picks.values()))
  print(len(duplicated_picks.values()))

def parse(picks):
  with open(picks, 'r') as f:
    int_picks = []
    lines = f.readlines()
    for line in lines:
      # ignore empty and comment lines
      line = line.strip()
      if line == '' or line.startswith("#"): continue
      int_pick = [int(pick) for pick in line.split(',')]
      int_picks.append(int_pick)
    return int_picks

def main():
  fire.Fire({
    'combine': combine
  })

if __name__ == '__main__':
  main()