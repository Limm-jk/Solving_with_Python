def solution(people, limit):
    answer = 0
    people.sort()
    j = len(people)-1
    for i in range(j):
        while(True):
            if j <= i:
                answer+=1
                break

            if people[i] + people[j] > limit:
                j -= 1
                answer+=1
            else:
                j -= 1
                answer+=1
                break


    return answer


arr = [70, 50, 80, 50]
limit = 100

print(solution(arr,limit))

# def solution(heights):
#     answer = []
#     heights.reverse()
#     for i in range(len(heights)):
#         target = heights[i]
#         for j in range(i+1,len(heights)):
#             if heights[j] > target:
#                 answer.append(len(heights)-j)
#                 break
#         else:
#             answer.append(0)
#     answer.reverse()
#     return answer