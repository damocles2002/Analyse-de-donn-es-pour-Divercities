import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pyodbc

plt.figure(figsize=(10, 6))
plt.plot(data_transformed['column_name'])
plt.title('Visualisation des données')
plt.xlabel('Temps')
plt.ylabel('Valeur')
plt.show()

data_transformed.to_csv('transformed_data.csv', index=False)
