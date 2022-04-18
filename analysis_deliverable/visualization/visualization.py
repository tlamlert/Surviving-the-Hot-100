import seaborn as sb
import matplotlib.pyplot as plt
import matplotlib.cm as cm



def correlation_heatmap(songs_df):
    C_mat = songs_df.corr()
    fig = plt.figure(figsize=(15,15))

    sb.heatmap(C_mat, vmax=0.8, square=True, center=0, cmap='seismic')
    plt.show()