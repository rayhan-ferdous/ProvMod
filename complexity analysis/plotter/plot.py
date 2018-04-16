## numpy is used for creating fake data
import numpy as np
import matplotlib as mpl

## agg backend is used to create plot as a .png file
mpl.use('agg')

import matplotlib.pyplot as plt

'''
collection1 = []
collection2 = []

prov = open('prov.csv', 'r')
noprov = open('noprov.csv', 'r')

for line in prov:
    print line
    collection1.append(float(line))

for line in noprov:
    print line
    collection2.append(float(line))

print collection1
print collection2



data_to_plot = [collection1, collection2]

# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))
plt.xlabel('Test Scenario')
plt.ylabel('Execution Time (sec)')
# Create an axes instance
ax = fig.add_subplot(111)

## Custom x-axis labels


# Create the boxplot
bp = ax.boxplot(data_to_plot, labels = ['prov', 'no prov'])


# Save the figure
fig.savefig('boxplot.png', bbox_inches='tight')
'''


# Create data
N = 500
f = open('time vs nodes.csv', 'r')
x = []
y =  []

for line in f:
    d = line.split(',')
    x.append(float(d[0]))
    y.append(int(d[1].strip()))

print x
print y

colors = (0, 0, 1)
area = np.pi*5

# Plot
plt.scatter(y, x, s=area, c=colors, alpha=0.5)

plt.xlabel('Total Nodes in GDB')
plt.ylabel('Workflow Execution Time (sec)')
plt.show()

plt.savefig('scatter.png', bbox_inches='tight')

'''

# Create data
N = 500
f = open('qtime vs nodes.csv', 'r')
x = []
y =  []

for line in f:
    d = line.split(',')
    x.append(float(d[0]))
    y.append(int(d[1].strip()))

print x
print y

colors = (1, 0, 0)
area = np.pi*5

# Plot
plt.scatter(y, x, s=area, c=colors, alpha=0.5)

plt.xlabel('Total Nodes in GDB')
plt.ylabel('Query Time (sec)')
plt.show()

plt.savefig('qscatter.png', bbox_inches='tight')

'''