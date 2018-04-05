#Sublime Limes' Line Graphs
import codecademylib
from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]

plt.figure(figsize=12,8)
ax1=plt.subplot(1,2,1)
x_values=range(len(12)) 
plt.plot(x_values,visits_per_month,marker='*')
plt.title('Amount of visits per months')
plt.xlabel('Months')
plt.ylabel('Visits')
ax.set_xticks(x_values)
ax.set_xticklabels(months)

#ax.set_yticks([0.10, 0.25, 0.5, 0.75])
#ax.set_yticklabels(["10%", "25%", "50%", "75%"])

ax2=plt.subplot(1,2,2)
plt.plot(persian_limes_per_month,months,marker='s')
plt.plot([x_values,
key_limes_per_month,color='orange'],[x_values,persian_limes_per_month,color='blue'],[x_values,blood_limes_per_month,color='purple'])#nose si es asi
plt.xlabel('key limes')
plt.ylabel('persian limes')
plt.zlabel('blood limes')
ax.set_xticks(x_values)
ax.set_xticklabels(months)
plt.title('LIMES')
plt.savefig('plot.png')
plt.show()
