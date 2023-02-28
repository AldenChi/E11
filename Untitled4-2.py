#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


data1 = pd.read_csv('sensor_data.csv')
data2 = pd.read_csv('sensor_data_outside.csv')


# In[4]:


plt.rcParams.update({'font.size': 12})
fig, axs = plt.subplots(2, 3, figsize=(12, 8))
axs = axs.flatten()


for i, col in enumerate(['Temperature', 'Gas', 'Pressure', 'Altitude', 'Relative Humididty']):
    data = data1[col]
    q25, q75 = np.percentile(data, [25, 75])
    iqr = q75 - q25
    bin_width = 2 * iqr / (len(data) ** (1/3))
    num_bins = int((max(data) - min(data)) / bin_width * 2)
    axs[i].hist(data, bins=num_bins)
    axs[i].set_xlabel(col)
    axs[i].set_ylabel('Frequency')
    axs[i].set_title('Frequency Distribution of ' + col, fontsize=10)

plt.tight_layout()
plt.show()


# In[5]:



from scipy.stats import normaltest

df = pd.read_csv('sensor_data.csv')


def check_normality(data):
    data_mean = np.mean(data)
    data_std = np.std(data)

    p_value = normaltest(data)[1]

    print('Mean:', data_mean)
    print('Standard deviation:', data_std)
    if p_value < 0.05:
        print('The data does not follow a normal distribution (p-value < 0.05)')
    else:
        print('The data appears to follow a normal distribution (p-value >= 0.05)')

check_normality(df['Temperature'])
check_normality(df['Gas'])
check_normality(df['Pressure'])
check_normality(df['Altitude'])


# In[6]:



from scipy.stats import norm


def plot_distribution(data, label):
   
    data_mean = np.mean(data)
    data_std = np.std(data)


    plt.hist(data, density=True, alpha=0.5, label=label)

    x = np.linspace(data_mean - 3 * data_std, data_mean + 3 * data_std, 100)
    y = norm.pdf(x, data_mean, data_std)
    plt.plot(x, y, label='Gaussian')

    plt.xlabel(label)
    plt.ylabel('Frequency')
    plt.title('Frequency Distribution of ' + label)

    plt.legend()
    plt.show()

plot_distribution(df['Temperature'], 'Temperature')
plot_distribution(df['Gas'], 'Gas')
plot_distribution(df['Pressure'], 'Pressure')
plot_distribution(df['Altitude'], 'Altitude')


# In[7]:


plt.rcParams.update({'font.size': 12})
fig, axs = plt.subplots(2, 3, figsize=(12, 8))
axs = axs.flatten()

for i, col in enumerate(['Temperature', 'Gas', 'Pressure', 'Altitude', 'Relative Humididty']):
    data = data2[col]
    q25, q75 = np.percentile(data, [25, 75])
    iqr = q75 - q25
    bin_width = 2 * iqr / (len(data) ** (1/3))
    num_bins = int((max(data) - min(data)) / bin_width * 2)
    axs[i].hist(data, bins=num_bins)
    axs[i].set_xlabel(col)
    axs[i].set_ylabel('Frequency')
    axs[i].set_title('Frequency Distribution of ' + col, fontsize=10)

plt.tight_layout()
plt.show()


# In[8]:


indoor_mean = data1.mean()
indoor_std = data1.std()

outdoor_mean = data2.mean()
outdoor_std = data2.std()

print('Indoor Mean Values:\n', indoor_mean)
print('Indoor Standard Deviation Values:\n', indoor_std)

print('\nOutdoor Mean Values:\n', outdoor_mean)
print('Outdoor Standard Deviation Values:\n', outdoor_std)


# In[9]:


data1 = pd.read_csv('sensor_data.csv')[['Temperature', 'Gas', 'Pressure', 'Altitude', 'Relative Humididty']]
data2 = pd.read_csv('sensor_data_outside.csv')[['Temperature', 'Gas', 'Pressure', 'Altitude', 'Relative Humididty']]

df = pd.concat([data1, data2], ignore_index=True)

std_mean = np.mean(df.std())
print('Mean uncertainty:', std_mean)


# In[10]:


variables = ['Temperature', 'Gas', 'Pressure', 'Altitude', 'Relative Humididty']

for var in variables:

    mean1, std1 = np.mean(data1[var]), np.std(data1[var])
    mean2, std2 = np.mean(data2[var]), np.std(data2[var])
    
    mean_diff = abs(mean1 - mean2)
    
    std_diff = np.sqrt(std1**2 + std2**2)
    
    num_sigma = mean_diff / std_diff
    
    print(f"{var}: {num_sigma:.2f} sigma")


# In[11]:


data3 = pd.read_csv('feb172023insidedata.csv')
data4 = pd.read_csv('feb242023outsidedata.csv')


# In[14]:


plt.rcParams.update({'font.size': 12})
fig, axs = plt.subplots(2, 3, figsize=(12, 8))
axs = axs.flatten()

for i, col in enumerate(['temperature', 'gas', 'pressure', 'humidity', 'altitude']):
    data = data3[col]
    q25, q75 = np.percentile(data, [25, 75])
    iqr = q75 - q25
    bin_width = 2 * iqr / (len(data) ** (1/3))
    num_bins = int((max(data) - min(data)) / bin_width * 2)
    axs[i].hist(data, bins=num_bins)
    axs[i].set_xlabel(col)
    axs[i].set_ylabel('Frequency')
    axs[i].set_title('Frequency Distribution of ' + col, fontsize=10)

plt.tight_layout()
plt.show()


# In[15]:


plt.rcParams.update({'font.size': 12})
fig, axs = plt.subplots(2, 3, figsize=(12, 8))
axs = axs.flatten()

for i, col in enumerate(['temperature', 'gas', 'pressure', 'humidity', 'altitude']):
    data = data4[col]
    q25, q75 = np.percentile(data, [25, 75])
    iqr = q75 - q25
    bin_width = 2 * iqr / (len(data) ** (1/3))
    num_bins = int((max(data) - min(data)) / bin_width * 2)
    axs[i].hist(data, bins=num_bins)
    axs[i].set_xlabel(col)
    axs[i].set_ylabel('Frequency')
    axs[i].set_title('Frequency Distribution of ' + col, fontsize=10)

plt.tight_layout()
plt.show()


# In[16]:


data3_mapped = data3.rename(columns={'temperature': 'Temperature',
                                     'gas': 'Gas',
                                     'pressure': 'Pressure',
                                     'humidity': 'Relative Humididty',
                                     'altitude': 'Altitude'})


plt.rcParams.update({'font.size': 12})
fig, axs = plt.subplots(2, 3, figsize=(12, 8))
axs = axs.flatten()

for i, col in enumerate(['Temperature', 'Gas', 'Pressure', 'Altitude', 'Relative Humididty']):
    axs[i].hist(data1[col], bins=20, alpha=0.5, label='Data 1')
    axs[i].hist(data3_mapped[col], bins=20, alpha=0.5, label='Data 3')
    axs[i].set_xlabel(col)
    axs[i].set_ylabel('Frequency')
    axs[i].set_title('Frequency Distribution of ' + col, fontsize=10)
    axs[i].legend()

plt.tight_layout()
plt.show()


# In[17]:


data4_mapped = data4.rename(columns={'temperature': 'Temperature',
                                     'gas': 'Gas',
                                     'pressure': 'Pressure',
                                     'humidity': 'Relative Humididty',
                                     'altitude': 'Altitude'})


plt.rcParams.update({'font.size': 12})
fig, axs = plt.subplots(2, 3, figsize=(12, 8))
axs = axs.flatten()

for i, col in enumerate(['Temperature', 'Gas', 'Pressure', 'Altitude', 'Relative Humididty']):
    axs[i].hist(data2[col], bins=20, alpha=0.5, label='Data 2')
    axs[i].hist(data4_mapped[col], bins=20, alpha=0.5, label='Data 4')
    axs[i].set_xlabel(col)
    axs[i].set_ylabel('Frequency')
    axs[i].set_title('Frequency Distribution of ' + col, fontsize=10)
    axs[i].legend()

plt.tight_layout()
plt.show()


# In[22]:


data1_mean = np.mean(data1)
data1_std = np.std(data1)

data3_mean = np.mean(data3)
data3_std = np.std(data3)

print("Data1 mean and standard deviation: ", data1_mean, data1_std)
print("Data3 mean and standard deviation: ", data3_mean, data3_std)


# In[21]:


data2_mean = np.mean(data2)
data2_std = np.std(data2)

data4_mean = np.mean(data4)
data4_std = np.std(data4)

print("Data2 mean and standard deviation: ", data2_mean, data2_std)
print("Data4 mean and standard deviation: ", data4_mean, data4_std)


# In[23]:



mean_uncertainty_data1 = data1.std() / np.sqrt(len(data1))
print("Mean uncertainty of data1:", mean_uncertainty_data1)

mean_uncertainty_data3 = data3.std() / np.sqrt(len(data3))
print("Mean uncertainty of data3:", mean_uncertainty_data3)

mean_uncertainty_data2 = data2.std() / np.sqrt(len(data2))
print("Mean uncertainty of data2:", mean_uncertainty_data2)

mean_uncertainty_data4 = data4.std() / np.sqrt(len(data4))
print("Mean uncertainty of data4:", mean_uncertainty_data4)


# In[33]:


data4_mapped = data4.rename(columns={'temperature': 'Temperature',
                                     'gas': 'Gas',
                                     'pressure': 'Pressure',
                                     'humidity': 'Relative Humididty',
                                     'altitude': 'Altitude'})

data3_mapped = data3.rename(columns={'temperature': 'Temperature',
                                     'gas': 'Gas',
                                     'pressure': 'Pressure',
                                     'humidity': 'Relative Humididty',
                                     'altitude': 'Altitude'})




# In[34]:


variables = ['Temperature', 'Gas', 'Pressure', 'Altitude', 'Relative Humididty']

for var in variables:

    mean1, std1 = np.mean(data1[var]), np.std(data1[var])
    mean3, std3 = np.mean(data3_mapped[var]), np.std(data3_mapped[var])
    
    mean_diff = abs(mean1 - mean3)
    
    std_diff = np.sqrt(std1**2 + std3**2)
    
    num_sigma = mean_diff / std_diff
    
    print(f"{var}: {num_sigma:.2f} sigma")


# In[35]:


variables = ['Temperature', 'Gas', 'Pressure', 'Altitude', 'Relative Humididty']

for var in variables:

    mean2, std2 = np.mean(data2[var]), np.std(data2[var])
    mean4, std4 = np.mean(data4_mapped[var]), np.std(data4_mapped[var])
    
    mean_diff = abs(mean2 - mean4)
    
    std_diff = np.sqrt(std2**2 + std4**2)
    
    num_sigma = mean_diff / std_diff
    
    print(f"{var}: {num_sigma:.2f} sigma")


# In[ ]:




