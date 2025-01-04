import matplotlib.pyplot as plt

def plot_consumption_vs_hour(df):
    plt.figure(figsize=(10, 6))
    plt.scatter(df['hour'], df['consumption'], alpha=0.5)
    plt.title("Consumption vs Hour")
    plt.xlabel("Hour")
    plt.ylabel("Consumption (kW)")
    plt.grid(True)
    plt.show()
    
def plot_consumption_vs_day_of_week(df):
    plt.figure(figsize=(10, 6))
    tage = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']
    plt.scatter(df['day_of_week'].map(dict(enumerate(tage))), df['consumption'], alpha=0.5)
    plt.title("Consumption vs Day of Week")
    plt.xlabel("Day of Week")
    plt.ylabel("Consumption (kW)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
def visualize_energy_consumption(df):	
    plot_consumption_vs_hour(df)
    plot_consumption_vs_day_of_week(df)