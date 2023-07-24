A_list = []
score_list = []
for i in range(8):
    A = int(input())
    new_dict = {i+1 : A}
    A_list.append(new_dict)

print(A_list.keys())
# for key, value in A_list :
#     if key >= 5:
#         A = min(score_list)
#         if value > A :
#             score_list.append(value)
#             score_list.remove(A)
#             print(score_list)
#             print(index)
#     else :
#         score_list.append(index, value)
#         print(index, score_list)
        
        
