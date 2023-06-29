# Plot test result
import matplotlib.pyplot as plt
import pandas as pd
import os

def extract_session_ids(path):
    files = os.listdir(path)
#     print("File Count: " + str(len(files)))
    session_ids = []
    for f in files:
#         print(f)
        temp = f.split('subject_')[1].split('__')[0]
        if temp not in session_ids:
            session_ids.append(temp)
#     print("Session Count: " + str(len(session_ids)))
#     print(session_ids)
    return session_ids

time_folder = "TestData/"
readings_folder = "TestData/x/"
label_folder = "TestLabel/"
sessions = extract_session_ids(readings_folder)
plt_df = pd.DataFrame()
for i in range(0,len(sessions)):
    sid = sessions[i]
    x_path =  readings_folder + "subject_" + sid + "__x.csv"
    y_path = label_folder + "subject_" + sid + "__y_prediction.csv"
    x_time_path = time_folder  + "subject_" + sid + "__x_time.csv"
    
    x = pd.read_csv(x_path,header=None, names=['xa', 'ya','za','xg','yg','zg'])
    x_time = pd.read_csv(x_time_path,header=None, names=['time'])
    y = pd.read_csv(y_path,header=None, names=['label'])
    
    temp = pd.concat([x_time, x, y], axis=1)
    
    plt_df = pd.concat([plt_df, temp], axis=0)
    

# Reading and Terrain------------------------------------------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

color = ['r','b','g','y']

for i in [0,1,2,3]:
    temp = plt_df[plt_df['label'] == i]
    z = temp['zg']
    x = temp['xg']
    y = temp['yg']
    ax.scatter(x, y, z, c=color[i],label=i)
ax.legend()
ax.set_title('Terrain Classes Against Gyroscope Reading')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
