def minion_game(string):
    stuart = 0
    kevin  = 0
    stuart = score_it(string,'BCDFGHJKLMNPQRSTVWXYZ')
    kevin  = score_it(string,'AEIOU')
    if stuart > kevin:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")
    
def score_it(s,starts='LETTERS'):
    score = 0
    for i, c in enumerate(list(s)):
        if c in starts:
            score += len(s) - i
    return score    
    

if __name__ == '__main__':
    s = input()
    minion_game(s)