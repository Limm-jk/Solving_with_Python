# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-06-14 02:42:54
#  * @modify date 2020-06-14 02:42:54
#  * @desc [description]
#  */

def solution(skill, skill_trees):
    answer = len(skill_trees)
    for i in skill_trees:
        skill_arr = list(skill)
        tree_arr = list(i)
        skill_cnt = skill_arr.pop(0)
        for i in range(len(tree_arr)):
            if tree_arr[i] not in skill_arr:
                if tree_arr == skill_cnt:
                    if(len(skill_arr) != 0):
                        skill_cnt = skill_arr.pop(0)
            else:
                answer-=1
                break
    return answer

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))