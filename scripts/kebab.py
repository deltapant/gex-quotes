def correctness(bobs_decisions, expert_decisions):
    score = 0
    for i in range(0, len(bobs_decisions)):
        if bobs_decisions[i] == expert_decisions[i]:
            score += 1
        elif bobs_decisions[i] != expert_decisions[i]:
            if bobs_decisions[i] == '?' or expert_decisions[i] == '?':
                score += 0.5
            else:
                score +=0
                
            
    return score
    
    
    
    
print(correctness(('F', 'M', 'F'), ('M', 'F', 'M')))