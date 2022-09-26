import pandas as pd
import matplotlib.pyplot as plt

num_measurements = 24


def read_data_for_particular_day(year, month, day):
    #
    month_int = int(month)
    first_day = "01"
    last_day = "31"
    if month_int in [9, 4, 6, 11]:
        last_day = "30"

    file_name = f"r{year}{month}{first_day}-{year}{month}{last_day}-UTC.csv"
    file_address = f"../data/diffuse_sol_rad/{file_name}"

    # read data from file r20210601-20210630-UTC.csv
    data_all = pd.read_csv(file_address)

    # filter to the specified day
    data_day = data_all[data_all['d'] == int(day)]
    file_name = f"{year}-{month}-{day}"
    return data_day, file_name


def plot_data(file_name):
    # plot results
    plt.plot(diff_sol_rad, 'r-')
    plt.axhline(y=mean, color='b', linestyle='--')
    plot_file_name = f"../processed_data/{file_name}.png"
    plt.savefig(plot_file_name)
    plt.show()




data, file_name = read_data_for_particular_day("2021", "09", "02")
diff_sol_rad = data['Diffuse radiation (W/m2)']  # extracting the relevant column

# compute statistics
mean = sum(diff_sol_rad) / num_measurements

plot_data(file_name)
