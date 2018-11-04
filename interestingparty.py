def bestinvitation(first, second):
    # 두개의 취미중 한개가 다른 사람과 겹치는게 있으면 카운트+
    answer = 0
    for i in range(0, len(first)):
        f = 0
        s = 0
        for j in range(0, len(first)):
            if first[i] == first[j]:
                f += 1
            if first[i] == second[j]:
                f += 1
            if second[i] == first[j]:
                s += 1
            if second[i] == second[j]:
                s += 1
        answer = max(answer, f)
        answer = max(answer, s)
    print(answer)
    return answer


bestinvitation(['fishing', 'fishing'], ['test', 'test'])
