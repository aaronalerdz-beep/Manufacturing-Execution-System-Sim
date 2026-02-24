import pandas as pd # type: ignore
import matplotlib.pyplot as plt# type: ignore
import numpy as np # type: ignore
import seaborn as sns # type: ignore
from Model import JoinModel as JM


def main():
    res = JM.select_join()
    df = pd.DataFrame(res)
    headers = [
    "cycle_id",
    "recorded_at",
    "finished",
    "parts_per_cycle",
    "config_id",       
    "pressure",
    "grit",
    "cycle_duration",
    "operator_name",
    "config_created_at", 
    "order_num",
    "target_quantity",
    "final_quantity",
    "start_time",
    "part_id_seq",     
    "description",
    "material",
    "sequence",
    "weight"
    ]
    df.columns =headers
    df['recorded_at'] = pd.to_datetime(df['recorded_at'])
    df['finished'] = df['finished'].astype(bool)
    df['pressure'] = pd.to_numeric(df['pressure'])
    df['grit'] = pd.to_numeric(df['grit'])
    df['cycle_duration'] = pd.to_numeric(df['cycle_duration'])
    print(df.groupby('finished')['description'].value_counts())
    print(df['finished'].value_counts())
    print(df.describe())


    fig, (ax1, ax2, ax3) = plt.subplots(1,3, figsize=(14,6))
    fig.suptitle("Process Characteristics Analysis vs. Description and Status", fontsize=16, fontweight='bold')
    sns.histplot(data=df, x='description', hue='finished', ax=ax1)
    ax1.set_title('Diferente Descripcion vs Fished cycles')
    ax1.tick_params(axis='x', rotation=15)
    sns.histplot(data=df, x='pressure', hue='finished', ax=ax2, palette='mako', shrink=5)
    ax2.set_title('We can see Finished cycles vs PRESSURE')
    ax2.set_xlim(35, 65) 
    ax2.set_xticks([40, 60])
    sns.histplot(data=df, x='grit', hue='finished', ax=ax3, palette='mako', shrink=5)
    ax3.set_title('We can see Finished cycles vs GRIT')
    ax3.set_xlim(35, 65) 
    ax3.set_xticks([40, 60])
    plt.tight_layout()
    plt.show()  

    corr = df[['pressure', 'grit', 'cycle_duration', 'weight']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()

    df_sorted = df.sort_values('recorded_at')
    sns.lineplot(data=df_sorted, x='recorded_at', y='parts_per_cycle', hue='finished')
    plt.title('Parts per Cycle over Time')
    plt.show()
    df.to_csv("output/analysis_results.csv", index=False)
    fig.savefig("output/process_analysis.png", dpi=300)

    
    
    

if __name__ == "__main__":
    main()