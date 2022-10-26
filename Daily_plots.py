import matplotlib
import matplotlib.pyplot as plt
from Initial_stock_interaction import Loading_data

time_series, open_values, lookup_date = time_series_fun()

plt.plot(sorted(time_series), open_values, color='red')#, marker='o')
plt.title(f"{lookup_date} stock prices", fontsize=14)
plt.xlabel('Hour', fontsize=14)
plt.ylabel('Price', fontsize=14)
plt.grid(True)
plt.yticks(np.arange(min(open_values), max(open_values)+1, 1))
plt.xticks(np.arange(min(time_series), max(time_series)+1, 1))

plt.show()





