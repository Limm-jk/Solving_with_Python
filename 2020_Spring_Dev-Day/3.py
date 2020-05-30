def solution(rule, A, B):
    answer = ''
    # arr = [[0 for i in range(100)] for j in range(55)]
    # print(arr[50][50])
    rules = list(rule)
    N = len(rules)
    A_arr = list(A)
    A_sub = []
    B_arr = list(B)
    B_sub = []
    totlen = len(A_arr)
    ans = [0 for _ in range(totlen)]
    ans_rule = []
    for i in range(totlen):
        A_sub.append(rules.index(A_arr[i]))
    for i in range(len(B_arr)):
        B_sub.append(rules.index(B_arr[i]))
    B_and = [0 for i in range(totlen-len(B_arr))]
    for p in range(len(B_sub)):
        B_and.append(B_sub.pop(0))
    # print(B_and)

    for cnt in range(totlen):
        if A_sub[cnt]-B_and[cnt] < 0:
            ans[cnt-1] -= 1
            A_sub[cnt] += N
        ans[cnt] = A_sub[cnt]-B_and[cnt]
    for j in range(totlen):
        if ans[0] == 0:
            if len(ans) == 1:
                break
            ans.pop(0)
        else:
            break;
    for k in range(len(ans)):
        ans_rule.append(rules[ans[k]])
    answer = "".join(ans_rule)
    return answer