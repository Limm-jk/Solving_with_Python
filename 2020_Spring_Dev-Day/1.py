def solution(seat):
    answer = 0
    ticket = []
    for i in seat:
        if i not in ticket:
            ticket.append(i)
            answer += 1

    # ticket = [[0 for i in range(50)] for j in range(50)]
    # for p in seat:
    #     a = ticket[p[0]][p[1]]
    #     if a == 0:
    #         answer += 1
    #         ticket[p[0]][p[1]] = -1
    return answer