import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_hist_box(data, feature):
    '''
    takes dataframe and a feature name, outputs a plot with boxplot and histogram of the feature
    '''
    fig, axes=plt.subplots(ncols=2)
    fig.set_size_inches(w=10, h=5)
    axes[0].boxplot(data[feature].dropna());
    axes[0].set_xticklabels([feature]);
    axes[1].hist(data[feature]);
    return axes


def plot_hist_default_pct(feature, dataframe, bins):
    '''
    takes a dataframe, a feature name and number of bins. Plots a histogram of the feature such that binning is equal width, and the value is the deafult percentage of that bin.  
    '''
    df=dataframe.copy()
    df['%s_binned'%feature]=pd.qcut(df[feature], q=bins, precision=3, duplicates='drop')
    counts=df['%s_binned'%feature].value_counts()
    default_counts=df.loc[df['TARGET']==1, '%s_binned'%feature].value_counts()
    default_counts=default_counts*100/counts
    default_counts.sort_index(inplace=True)
    ax=plt.axes()
    ax.bar(default_counts.index.astype(str), default_counts.values)
    ax.tick_params(axis='x', rotation=90)
    ax.set_title('Deafulters %% in %s'%feature)
    ax.set_xlabel('Category')
    ax.set_ylabel('Defaulter %')
    print(default_counts)



def calc_iqr(feature, data):
    '''
    takes a dataframe and a feature name, returns the the 1st quartile, 3rd quartile and the inter-quartile range
    '''
    q3=data[feature].quantile(0.75)
    q1=data[feature].quantile(0.25)
    iqr=q3-q1
    return q1, q3, iqr


def plot_kde_vs_target(feature, main_data):
    '''
    takes a dataframe and a feature name, plots two kernel density plots, one for deafulter customers and other of non-deafulter customers. plots nothing of the variance of the feature is zero. 
    '''
    paid=main_data[main_data['TARGET']==0][feature]
    defaulted=main_data[main_data['TARGET']==1][feature]
    sns.kdeplot(paid, label='Paid', color='b')
    sns.kdeplot(defaulted, label='Defaulted', color='r')
    plt.legend()


def plot_all_numeric_kde(main_data, numerical_features):
    '''
    takes a dataframe and an index of feature names, plots the kernel density plots of all features present in numerical_features   
    '''
    fig, axes=plt.subplots(numerical_features.shape[0])
    fig.set_size_inches(10, 4*numerical_features.shape[0])
    for i, feature in enumerate(numerical_features):
        q1, q3, iqr=calc_iqr(feature, main_data)
        plot_data=main_data.loc[(main_data[feature]>=q1-1.5*iqr) & (main_data[feature]<=q3+1.5*iqr), :]
        paid=plot_data[plot_data['TARGET']==0][feature]
        defaulted=plot_data[plot_data['TARGET']==1][feature]
        sns.kdeplot(paid, label='Paid', color='b', ax=axes[i])
        sns.kdeplot(defaulted, label='Defaulted', color='r', ax=axes[i])
        axes[i].legend()


def plot_pie_target(target_series, ax=None):
    if ax is None:
        ax=plt.axes()
    plot_data=target_series.value_counts()
    plot_data.rename(index={0: "Paid", 1: "Defaulted"}, inplace=True)
    ax.pie(x=plot_data.values, labels=plot_data.index, autopct='%1.1f%%')
    return ax


def median_vs_target(feature, data):
    '''
    takes a feature name and a dataframe. prints two values, one is median of non-defaulters while other is median of deafulters
    '''
    print('Median of %s with target=0 : %f'%(feature, data.loc[data['TARGET']==0, feature].median()))
    print('Median of %s with target=1 : %f'%(feature, data.loc[data['TARGET']==1, feature].median()))