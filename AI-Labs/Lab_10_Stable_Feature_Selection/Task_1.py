import pandas as pd
import matplotlib.pyplot as plt

distance = pd.read_csv('distance.csv')

x = distance['Ref'] + distance['Question']
ratio = distance['Ratio']
transitions = distance['Transitions']
black_sizes = distance['Black_Size']
normalization = distance['Normalization']
normalization_sums = distance['Normalization_Sums']
angles = distance['Angles']
centroid = distance['Centroid']

#plt.subplot(1, 2, 1)
plt.scatter(x[:20], centroid[:20])
plt.title('centroid Plot')
plt.xticks(rotation=70)

plt.subplot(1, 2, 2)
plt.scatter(x[:20], angles[:20])
plt.title('angles Plot')
plt.xticks(rotation=70)

plt.show()
