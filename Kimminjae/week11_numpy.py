import numpy as np

# python list
mid = [10, 20, 30]
final = [90, 70, 80]

# numpy array
mid_scores = np.array(mid)
final_scores = np.array(final)

print(type(mid), type(mid_scores))

total_np = mid_scores + final_scores
print(f"Total : {total_np}")
print(f"Average : {total_np / 2}")

# total = list()
# avg = []
# for i in range(len(mid)):
#     total.append(mid[i] + final[i])
#     avg.append(total[i] / 2)
# print(f"Total : {total}")
# print(f"Average : {avg}")