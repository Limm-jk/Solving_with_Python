def convert(s: str, numRows: int) -> str:
        str_list = list(s)
        flag = 1 #0이면 감소 1이면 증가
        row = [[] for i in range(numRows+1)]
        index = 1
        
        for i in str_list:
            row[index].append(i)
            if numRows != 1:
                if flag:
                    if index == numRows:
                        flag = 0
                else:
                    if index == 1:
                        flag = 1
                            
                if flag:
                    index += 1
                else:
                    index -= 1
                
        answer_list = []
        for i in row:
            answer_list.extend(i)
        
        
        answer = ''.join(answer_list)
        return answer

print(convert("AB", 1))