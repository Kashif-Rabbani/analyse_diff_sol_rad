import pandas as pd
import matplotlib.pyplot as plt

num_measurements = 24

# read data from file r20210601-20210630-UTC.csv
data = pd.read_csv('../data/diffuse_sol_rad/r20210601-20210630-UTC.csv', nrows=num_measurements)
diff_sol_rad = data['Diffuse radiation (W/m2)']

# compute statistics
mean = sum(diff_sol_rad)/num_measurements

# plot results
plt.plot(diff_sol_rad, 'r-')
plt.axhline(y=mean, color='b', linestyle='--')
plt.savefig('../processed_data/2021-06-01.png')
plt.clf()