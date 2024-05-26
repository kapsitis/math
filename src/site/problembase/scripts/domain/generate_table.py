import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from collections import defaultdict

# Input data
data = """
LV.AMO.2022B.5.1,"NT","Skaitļu teorija"
LV.AMO.2022B.5.2,"Geom","Ģeometrija"
LV.AMO.2022B.5.3,"NT","Kombinatorika"
LV.AMO.2022B.5.4,"Alg","Ģeometrija"
LV.AMO.2022B.5.5,"Comb","loģika"
LV.AMO.2022B.6.1,"NT","Skaitļu teorija"
LV.AMO.2022B.6.2,"Geom","Ģeometrija"
LV.AMO.2022B.6.3,"NT","Skaitļu teorija"
LV.AMO.2022B.6.4,"Alg","ģeometrija"
LV.AMO.2022B.6.5,"Comb","kombinatorika"
LV.AMO.2022B.7.1,"NT","Skaitļu teorija"
LV.AMO.2022B.7.2,"Alg","Skaitļu teorija"
LV.AMO.2022B.7.3,"Geom","Ģeometrija"
LV.AMO.2022B.7.4,"NT","kombinatorika"
LV.AMO.2022B.7.5,"Comb","kombinatorika"
LV.AMO.2022B.8.1,"NT","Skaitļu teorija"
LV.AMO.2022B.8.2,"Alg","algebra"
LV.AMO.2022B.8.3,"Geom","Ģeometrija"
LV.AMO.2022B.8.4,"NT","skaitļu teorija"
LV.AMO.2022B.8.5,"Comb","kombinatorika"
LV.AMO.2022B.9.1,"NT","Skaitļu teorija"
LV.AMO.2022B.9.2,"Alg","Algebra"
LV.AMO.2022B.9.3,"Geom","Ģeometrija"
LV.AMO.2022B.9.4,"NT","skaitļu teorija"
LV.AMO.2022B.9.5,"Comb","kombinatorika"
LV.AMO.2022B.10.1,"NT","skaitļu teorija"
LV.AMO.2022B.10.2,"NT","Skaitļu teorija"
LV.AMO.2022B.10.3,"Geom","Ģeometrija"
LV.AMO.2022B.10.4,"Alg","algebra"
LV.AMO.2022B.10.5,"Comb","kombinatorika"
LV.AMO.2022B.11.1,"NT","Skaitļu teorija"
LV.AMO.2022B.11.2,"Alg","Algebra"
LV.AMO.2022B.11.3,"Geom","Ģeometrija"
LV.AMO.2022B.11.4,"NT","Algebra"
LV.AMO.2022B.11.5,"Comb","Kombinatorika"
LV.AMO.2022B.12.1,"NT","Skaitļu teorija"
LV.AMO.2022B.12.2,"Alg","Algebra"
LV.AMO.2022B.12.3,"Geom","Ģeometrija"
LV.AMO.2022B.12.4,"Alg","Algebra"
LV.AMO.2022B.12.5,"Comb","kombinatorika"
LV.AMO.2023.5.1,"Alg","kombinatorika"
LV.AMO.2023.5.2,"NT","skaitļu teorija"
LV.AMO.2023.5.3,"Geom","Ģeometrija"
LV.AMO.2023.5.4,"Comb","Kombinatorika"
LV.AMO.2023.5.5,"Alg","kombinatorika"
LV.AMO.2023.6.1,"Alg","kombinatorika"
LV.AMO.2023.6.2,"NT","skaitļu teorija"
LV.AMO.2023.6.3,"Geom","Ģeometrija"
LV.AMO.2023.6.4,"Comb","kombinatorika"
LV.AMO.2023.6.5,"Alg","kombinatorika"
LV.AMO.2023.7.1,"Comb","kombinatorika"
LV.AMO.2023.7.2,"NT","skaitļu teorija"
LV.AMO.2023.7.3,"Geom","Ģeometrija"
LV.AMO.2023.7.4,"Alg","kombinatorika"
LV.AMO.2023.7.5,"Comb","kombinatorika"
LV.AMO.2023.8.1,"Alg","skaitļu teorija"
LV.AMO.2023.8.2,"NT","Skaitļu teorija"
LV.AMO.2023.8.3,"Geom","Ģeometrija"
LV.AMO.2023.8.4,"Alg","Skaitļu teorija"
LV.AMO.2023.8.5,"Comb","loģikas problēma"
LV.AMO.2023.9.1,"Alg","Skaitļu teorija"
LV.AMO.2023.9.2,"NT","skaitļu teorija"
LV.AMO.2023.9.3,"Geom","Ģeometrija"
LV.AMO.2023.9.4,"Alg","kombinatorika"
LV.AMO.2023.9.5,"Comb","skaitļu teorija"
LV.AMO.2023.10.1,"Comb","kombinatorika"
LV.AMO.2023.10.2,"Alg","Algebra"
LV.AMO.2023.10.3,"Geom","Ģeometrija"
LV.AMO.2023.10.4,"Alg","kombinatorika"
LV.AMO.2023.10.5,"NT","skaitļu teorija"
LV.AMO.2023.11.1,"Alg","Kombinatorika"
LV.AMO.2023.11.2,"Alg","algebra"
LV.AMO.2023.11.3,"Geom","Ģeometrija"
LV.AMO.2023.11.4,"Comb","Kombinatorika"
LV.AMO.2023.11.5,"NT","Algebra"
LV.AMO.2023.12.1,"Alg","kombinatorika"
LV.AMO.2023.12.2,"Alg","Algebra"
LV.AMO.2023.12.3,"Geom","Ģeometrija"
LV.AMO.2023.12.4,"Comb","Kombinatorika"
LV.AMO.2023.12.5,"NT","skaitļu teorija"
LV.NOL.2024.5.1,"NT","kombinatorika"
LV.NOL.2024.5.2,"Geom","kombinatorika"
LV.NOL.2024.5.3,"Comb","Ģeometrija"
LV.NOL.2024.5.4,"NT","skaitļu teorija"
LV.NOL.2024.5.5,"Alg","kombinatorika"
LV.NOL.2024.6.1,"NT","Kombinatorika"
LV.NOL.2024.6.2,"Geom","Ģeometrija"
LV.NOL.2024.6.3,"Comb","Kombinatorika"
LV.NOL.2024.6.4,"NT","Skaitļu teorija"
LV.NOL.2024.6.5,"Geom","kombinatorika"
LV.NOL.2024.7.1,"Comb","kombinatorika"
LV.NOL.2024.7.2,"NT","Skaitļu teorija"
LV.NOL.2024.7.3,"Geom","Ģeometrija"
LV.NOL.2024.7.4,"Comb","Ģeometrija"
LV.NOL.2024.7.5,"Alg","Kombinatorika"
LV.NOL.2024.8.1,"NT","Skaitļu teorija"
LV.NOL.2024.8.2,"Geom","Ģeometrija"
LV.NOL.2024.8.3,"Comb","Kombinatorika"
LV.NOL.2024.8.4,"Alg","kombinatorika"
LV.NOL.2024.8.5,"Alg","kombinatorika"
LV.NOL.2024.9.1,"Geom","Ģeometrija"
LV.NOL.2024.9.2,"Alg","algebra"
LV.NOL.2024.9.3,"Geom","Ģeometrija"
LV.NOL.2024.9.4,"Comb","kombinatorika"
LV.NOL.2024.9.5,"NT","Skaitļu teorija"
LV.NOL.2024.10.1,"Alg","Algebra"
LV.NOL.2024.10.2,"Geom","kombinatorika"
LV.NOL.2024.10.3,"Geom","ģeometrija"
LV.NOL.2024.10.4,"NT","skaitļu teorija"
LV.NOL.2024.10.5,"Comb","Kombinatorika"
LV.NOL.2024.11.1,"Geom","Ģeometrija"
LV.NOL.2024.11.2,"Alg","Algebra"
LV.NOL.2024.11.3,"Geom","Ģeometrija"
LV.NOL.2024.11.4,"NT","skaitļu teorija"
LV.NOL.2024.11.5,"Comb","kombinatorika"
LV.NOL.2024.12.1,"Geom","Ģeometrija"
LV.NOL.2024.12.2,"Alg","algebra"
LV.NOL.2024.12.3,"Geom","Ģeometrija"
LV.NOL.2024.12.4,"NT","kombinatorika"
LV.NOL.2024.12.5,"NT","Skaitļu teorija"
LV.VOL.2024.9.1,"Alg","Skaitļu teorija"
LV.VOL.2024.9.2,"Geom","Ģeometrija"
LV.VOL.2024.9.3,"Comb","Kombinatorika"
LV.VOL.2024.9.4,"NT","skaitļu teorija"
LV.VOL.2024.9.5,"NT","kombinatorika"
LV.VOL.2024.10.1,"NT","kombinatorika"
LV.VOL.2024.10.2,"Geom","Ģeometrija"
LV.VOL.2024.10.3,"Alg","Algebra"
LV.VOL.2024.10.4,"Alg","skaitļu teorija"
LV.VOL.2024.10.5,"Comb","Kombinatorika"
LV.VOL.2024.11.1,"Alg","Algebra"
LV.VOL.2024.11.2,"Geom","Ģeometrija"
LV.VOL.2024.11.3,"Comb","Kombinatorika"
LV.VOL.2024.11.4,"NT","Skaitļu teorija"
LV.VOL.2024.11.5,"Alg","Algebra"
LV.VOL.2024.12.1,"Alg","Algebra"
LV.VOL.2024.12.2,"Geom","Ģeometrija"
LV.VOL.2024.12.3,"Comb","Kombinatorika"
LV.VOL.2024.12.4,"NT","skaitļu teorija"
LV.VOL.2024.12.5,"Alg","algebra"
"""

# Parse the data
data = [line.split(',') for line in data.strip().split('\n')]

# Mapping of Latvian names to domains
domain_map = {
    'Skaitļu teorija': 'NT',
    'Ģeometrija': 'Geom',
    'Kombinatorika': 'Comb',
    'Algebra': 'Alg',
    'algebra': 'Alg',
    'skaitļu teorija': 'NT',
    'ģeometrija': 'Geom',
    'kombinatorika': 'Comb',
    'loģika': 'Other', # Assuming loģika is not a valid category for this example
    'loģikas problēma': 'Other' # Assuming loģikas problēma is not a valid category for this example
}

# Initialize confusion matrix
domains = ['Alg', 'Geom', 'Comb', 'NT']
confusion_matrix = defaultdict(lambda: defaultdict(int))

# Populate the confusion matrix
for entry in data:
    expected_domain = entry[1].strip('"')
    generated_domain_latvian = entry[2].strip('"')
    generated_domain = domain_map.get(generated_domain_latvian, 'Other')
    
    if expected_domain in domains and generated_domain in domains:
        confusion_matrix[expected_domain][generated_domain] += 1

# Convert confusion matrix to a pandas DataFrame
confusion_df = pd.DataFrame(confusion_matrix).fillna(0).astype(int).T
confusion_df = confusion_df.reindex(index=domains, columns=domains, fill_value=0)

# Calculate percentages
confusion_df_percentage = confusion_df.div(confusion_df.sum(axis=1), axis=0) * 100

# Print confusion matrix with percentages
print(confusion_df_percentage)

# Plot confusion matrix as a heatmap with percentages
plt.figure(figsize=(10, 8))
sns.heatmap(confusion_df_percentage, annot=True, fmt=".2f", cmap="YlGnBu", cbar=False, xticklabels=domains, yticklabels=domains)
plt.xlabel('Predicted Domain')
plt.ylabel('Actual Domain')
plt.title('Confusion Matrix of Domain Classification (Percentage)')
plt.show()