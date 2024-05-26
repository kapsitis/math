import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from collections import defaultdict

# Input data
data_str = """
LV.VOL.2024.9.1,"ProveDisprove","ProveDisprove"
LV.VOL.2024.9.2,"FindAll","FindExample"
LV.VOL.2024.9.3,"Prove","Prove"
LV.VOL.2024.9.4,"Algorithm","Prove"
LV.VOL.2024.9.5,"ProveDisprove","ProveDisprove"
LV.VOL.2024.10.1,"ProveDisprove","ProveDisprove"
LV.VOL.2024.10.2,"Prove","Prove"
LV.VOL.2024.10.3,"FindAll","FindAll"
LV.VOL.2024.10.4,"FindCount","FindCount"
LV.VOL.2024.10.5,"FindOptimal","FindOptimal"
LV.VOL.2024.11.1,"FindAll","FindAll"
LV.VOL.2024.11.2,"FindAll","FindAll"
LV.VOL.2024.11.3,"Prove","Prove"
LV.VOL.2024.11.4,"FindAll","FindAll"
LV.VOL.2024.11.5,"Prove","Prove"
LV.VOL.2024.12.1,"FindAll","FindAll"
LV.VOL.2024.12.2,"Prove","Prove"
LV.VOL.2024.12.3,"Algorithm,Algorithm","Algorithm"
LV.VOL.2024.12.4,"ProveDisprove","ProveDisprove"
LV.VOL.2024.12.5,"FindOptimal","FindOptimal"
LV.NOL.2024.5.1,"FindExample","FindExample"
LV.NOL.2024.5.2,"FindOptimal","FindOptimal"
LV.NOL.2024.5.3,"FindExample","FindExample"
LV.NOL.2024.5.4,"FindExample","FindExample"
LV.NOL.2024.5.5,"ProveDisprove","ProveDisprove"
LV.NOL.2024.6.1,"FindExample","FindExample"
LV.NOL.2024.6.2,"FindOptimal","FindOptimal"
LV.NOL.2024.6.3,"FindExample","FindExample"
LV.NOL.2024.6.4,"FindExample","FindExample"
LV.NOL.2024.6.5,"ProveDisprove","ProveDisprove"
LV.NOL.2024.7.1,"FindExample","FindExample"
LV.NOL.2024.7.2,"FindOptimal","FindOptimal"
LV.NOL.2024.7.3,"FindAll","FindExample"
LV.NOL.2024.7.4,"FindExample","FindExample"
LV.NOL.2024.7.5,"Prove","Prove"
LV.NOL.2024.8.1,"ProveDisprove","ProveDisprove"
LV.NOL.2024.8.2,"FindExample","FindExample"
LV.NOL.2024.8.3,"FindOptimal","FindOptimal"
LV.NOL.2024.8.4,"Prove","Prove"
LV.NOL.2024.8.5,"ProveDisprove","FindExample"
LV.NOL.2024.9.1,"Prove","Prove"
LV.NOL.2024.9.2,"Prove","Prove"
LV.NOL.2024.9.3,"Prove","Prove"
LV.NOL.2024.9.4,"ProveDisprove","ProveDisprove"
LV.NOL.2024.9.5,"Prove","Prove"
LV.NOL.2024.10.1,"Prove","Prove"
LV.NOL.2024.10.2,"Prove","Prove"
LV.NOL.2024.10.3,"Prove","Prove"
LV.NOL.2024.10.4,"FindAll","FindAll"
LV.NOL.2024.10.5,"ProveDisprove","ProveDisprove"
LV.NOL.2024.11.2,"Prove","Prove"
LV.NOL.2024.11.3,"FindExample","FindExample"
LV.NOL.2024.11.4,"Prove","Prove"
LV.NOL.2024.11.5,"ProveDisprove","ProveDisprove"
LV.NOL.2024.12.1,"Prove","Prove"
LV.NOL.2024.12.2,"Prove","Prove"
LV.NOL.2024.12.4,"Algorithm,Algorithm","Algorithm"
LV.NOL.2024.12.5,"FindAll","FindAll"
LV.AMO.2000.7.1,"Prove","Prove"
LV.AMO.2000.7.2,"FindOptimal","FindOptimal"
LV.AMO.2000.7.4,"ProveDisprove","ProveDisprove"
LV.AMO.2000.8.3,"ProveDisprove","ProveDisprove"
LV.AMO.2001.7.2,"Prove,ProveDisprove","ProveDisprove"
LV.AMO.2001.8.3,"FindAll","FindExample"
LV.AMO.2002.7.4,"Algorithm","Algorithm"
LV.AMO.2002.7.5,"FindOptimal","FindOptimal"
LV.AMO.2002.8.2,"FindAll","FindExample"
LV.AMO.2002.8.3,"ProveDisprove","ProveDisprove"
LV.AMO.2003.7.3,"Algorithm","Algorithm"
LV.AMO.2003.7.5,"Algorithm","Algorithm"
LV.AMO.2003.8.3,"FindCount","FindOptimal"
LV.AMO.2003.8.5,"ProveDisprove","ProveDisprove"
LV.AMO.2004.7.3,"FindOptimal","FindOptimal"
LV.AMO.2004.8.3,"Prove","Prove"
LV.AMO.2004.8.5,"FindAll","Algorithm"
LV.AMO.2005.7.4,"FindOptimal","FindOptimal"
LV.AMO.2005.8.3,"FindExample","FindExample"
LV.AMO.2006.7.1,"FindAll","FindExample"
LV.AMO.2006.8.3,"FindExample,ProveDisprove,ProveDisprove","FindExample"
LV.AMO.2007.7.1,"FindOptimal","FindOptimal"
LV.AMO.2007.7.3,"Algorithm,Prove","Prove"
LV.AMO.2007.8.3,"FindAll","FindExample"
LV.AMO.2008.7.2,"ProveDisprove","ProveDisprove"
LV.AMO.2008.8.3,"Prove","Prove"
LV.AMO.2009.7.3,"FindOptimal","FindOptimal"
LV.AMO.2009.7.5,"FindAll","FindCount"
LV.AMO.2009.8.4,"FindAll","FindExample"
LV.AMO.2010.7.1,"FindAll","FindAll"
LV.AMO.2010.7.3,"FindExample","FindExample"
LV.AMO.2010.7.4,"FindAll","FindCount"
LV.AMO.2010.8.1,"ProveDisprove","FindExample"
LV.AMO.2010.8.2,"Prove","Prove"
LV.AMO.2010.10.4,"FindCount","FindCount"
LV.AMO.2011.5.1,"FindAll","FindAll"
LV.AMO.2011.5.2,"FindAll","FindExample"
LV.AMO.2011.5.3,"Prove","Prove"
LV.AMO.2011.5.4,"ProveDisprove","ProveDisprove"
LV.AMO.2011.5.5,"Prove","FindExample"
LV.AMO.2011.6.1,"ProveDisprove","FindExample"
LV.AMO.2011.6.2,"FindAll","FindCount"
LV.AMO.2011.6.3,"FindOptimal","FindOptimal"
LV.AMO.2011.6.4,"ProveDisprove","Algorithm"
LV.AMO.2011.6.5,"FindAll","FindExample"
LV.AMO.2011.7.1,"FindAll","FindExample"
LV.AMO.2011.7.3,"FindExample","FindExample"
LV.AMO.2011.8.1,"FindExample","FindExample"
LV.AMO.2011.8.4,"ProveDisprove","ProveDisprove"
LV.AMO.2011.8.5,"Algorithm,Prove","Algorithm"
LV.AMO.2012.5.1,"ProveDisprove","ProveDisprove"
LV.AMO.2012.5.2,"ProveDisprove","Prove"
LV.AMO.2012.5.3,"ProveDisprove","FindOptimal"
LV.AMO.2012.5.4,"ProveDisprove","FindExample"
LV.AMO.2012.5.5,"ProveDisprove","FindExample"
LV.AMO.2012.7.1,"ProveDisprove","FindExample"
LV.AMO.2012.8.1,"FindExample","FindExample"
LV.AMO.2012.8.3,"FindAll","FindCount"
LV.AMO.2012.8.4,"Prove","Prove"
LV.AMO.2012.9.1,"FindExample","FindExample"
LV.AMO.2012.9.2,"Prove","Prove"
LV.AMO.2012.9.3,"FindAll","FindExample"
LV.AMO.2012.9.4,"ProveDisprove","ProveDisprove"
LV.AMO.2012.9.5,"Prove","Prove"
LV.AMO.2012.10.1,"Prove","Prove"
LV.AMO.2013.7.1,"Prove","Prove"
LV.AMO.2013.7.3,"Prove","Prove"
LV.AMO.2013.8.1,"FindAll","FindAll"
LV.AMO.2013.10.4,"Prove","Prove"
LV.AMO.2014.5.1,"FindAll","FindAll"
LV.AMO.2014.5.2,"ProveDisprove","ProveDisprove"
LV.AMO.2014.5.3,"FindAll","FindExample"
LV.AMO.2014.5.4,"FindOptimal","FindOptimal"
LV.AMO.2014.5.5,"FindOptimal,FindOptimal","FindOptimal"
LV.AMO.2014.7.2,"ProveDisprove","FindExample"
LV.AMO.2014.7.4,"FindAll","FindAll"
LV.AMO.2014.8.1,"FindAll","ProveDisprove"
LV.AMO.2014.8.2,"FindAll","FindAll"
LV.AMO.2014.8.5,"ProveDisprove","ProveDisprove"
LV.AMO.2014.10.4,"FindOptimal","FindOptimal"
LV.AMO.2015.7.3,"FindExample,ProveDisprove","FindExample"
LV.AMO.2015.8.1,"FindAll","ProveDisprove"
LV.AMO.2015.8.3,"FindExample","FindExample"
LV.AMO.2015.10.3,"FindAll","FindAll"
LV.AMO.2016.7.2,"FindAll","FindExample"
LV.AMO.2016.8.1,"FindAll","FindExample"
LV.AMO.2016.8.2,"ProveDisprove","FindExample"
LV.AMO.2016.8.3,"FindOptimal","FindOptimal"
LV.AMO.2016.10.2,"ProveDisprove","FindExample"
LV.AMO.2016.10.3,"Prove","Prove"
LV.AMO.2017.7.5,"FindCount","FindCount"
LV.AMO.2017.8.5,"ProveDisprove","ProveDisprove"
LV.AMO.2017.10.5,"Prove","Prove"
LV.AMO.2018.7.4,"FindExample","FindExample"
LV.AMO.2018.8.2,"FindAll","Algorithm"
LV.AMO.2018.10.4,"Prove","Prove"
LV.AMO.2019.7.5,"FindOptimal","FindOptimal"
LV.AMO.2019.8.5,"FindOptimal","FindOptimal"
LV.AMO.2019.10.1,"Prove","Prove"
LV.AMO.2019.10.4,"FindAll","FindAll"
"""# Parse the data
data = [line.split(',') for line in data_str.strip().split('\n')]
question_data = [line.split(',') for line in data_str.strip().split('\n')]

# Mapping of Latvian names to question types
question_map = {
    'ProveDisprove': 'ProveDisprove',
    'FindAll': 'FindAll',
    'FindExample': 'FindExample',
    'Prove': 'Prove',
    'Algorithm': 'Algorithm',
    'FindCount': 'FindCount',
    'FindOptimal': 'FindOptimal'
}

# Initialize confusion matrix
question_types = ['ProveDisprove', 'FindAll', 'FindExample', 'Prove', 'Algorithm', 'FindCount', 'FindOptimal']
confusion_matrix = defaultdict(lambda: defaultdict(int))

# Populate the confusion matrix
for entry in question_data:
    expected_question_type = entry[1].strip('"')
    generated_question_type = entry[2].strip('"')
    
    if expected_question_type in question_types and generated_question_type in question_types:
        confusion_matrix[expected_question_type][generated_question_type] += 1

# Convert confusion matrix to a pandas DataFrame
confusion_df = pd.DataFrame(confusion_matrix).fillna(0).astype(int).T
confusion_df = confusion_df.reindex(index=question_types, columns=question_types, fill_value=0)

# Calculate percentages
confusion_df_percentage = confusion_df.div(confusion_df.sum(axis=1), axis=0) * 100

# Print confusion matrix with percentages
print(confusion_df_percentage)

# Plot confusion matrix as a heatmap with percentages
plt.figure(figsize=(10, 8))
sns.heatmap(confusion_df_percentage, annot=True, fmt=".2f", cmap="YlGnBu", cbar=False, xticklabels=question_types, yticklabels=question_types)
plt.xlabel('Predicted Question Type')
plt.ylabel('Actual Question Type')
plt.title('Confusion Matrix of Question Type Classification (Percentage)')
plt.show()