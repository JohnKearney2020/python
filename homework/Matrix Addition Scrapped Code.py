# multi_list = [[7,8], [12,10]]
# print(multi_list[0][0]) # 7
# print(multi_list[0][1]) # 8
# print(multi_list[1][0]) # 12
# print(multi_list[1][1]) # 10

# twoD_list_1 = [[1, 3], [2, 4]]
# twoD_list_2 = [[5, 2], [1, 0]]
# x = 'placeholder string'
# added_list = [[x, x], [x, x]]

#print(len(added_list))
#print(len(twoD_list))
# for i in range(0, len(twoD_list_1), 1):
#     # added_list[i][i] = twoD_list[i][i] + 
#     # added_list[i][i+1] = twoD_list[i][i+1]
#     list_1_val = twoD_list_1[i][i]
#     list_2_val = twoD_list_2[i][i]
#     added_list[i][i] = list_1_val + list_2_val

#     for ii in range(1, len(twoD_list_2), 1):
#         #added_list[i][ii] = twoD_list[ii][i]
#         list_1_val = twoD_list_1[i][ii]
#         list_2_val = twoD_list_2[i][ii]
#         added_list[i][ii] = list_1_val + list_2_val

twoD_list_1 = [[1, 3], [2, 4]]
twoD_list_2 = [[5, 2], [1, 0]]
x = 'placeholder string'
#added_list = [[x, x], [x, x]]
added_list = []
m_1_values = []
m_2_values = []
for i in range(0, len(twoD_list_1) - 1, 1):
    #value_1_m_1 = twoD_list_1[i][i]
    m_1_values.append(twoD_list_1[i][i])
    for ii in range(0, len(twoD_list_1) - 1, 1):
        #value_2_m_1 = twoD_list_1[i][i+1]
        m_1_values.append(twoD_list_1[i][i+1])
        #value_3_m_1 = twoD_list_1[i+1][i]
        m_1_values.append(twoD_list_1[i+1][i])
        for iii in range(0, len(twoD_list_1) - 1, 1):
            #value_4_m_1 = twoD_list_1[i+1][i+1]
            m_1_values.append(twoD_list_1[i+1][i+1])

for i in range(0, len(twoD_list_2) - 1, 1):
    #value_1_m_1 = twoD_list_1[i][i]
    m_2_values.append(twoD_list_2[i][i])
    for ii in range(0, len(twoD_list_2) - 1, 1):
        #value_2_m_1 = twoD_list_1[i][i+1]
        m_2_values.append(twoD_list_2[i][i+1])
        #value_3_m_1 = twoD_list_1[i+1][i]
        m_2_values.append(twoD_list_2[i+1][i])
        for iii in range(0, len(twoD_list_2) - 1, 1):
            #value_4_m_1 = twoD_list_1[i+1][i+1]
            m_2_values.append(twoD_list_2[i+1][i+1])


for i in range(0, len(m_1_values),1):
    added_list.append(m_1_values[i] + m_2_values[i])

print(added_list)
#arr = [[0 for i in range(cols)] for j in range(rows)] 
final_list = [[0 for i in range(len(twoD_list_1))], [0 for i in range(len(twoD_list_1))]]
print(final_list)
