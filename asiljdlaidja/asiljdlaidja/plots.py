import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("clash_royale_cards2.csv")



print("Here is what the dataset looks like:")
print(df.head())
print("\n")



plt.figure(figsize=(8, 5))
plt.scatter(df["elixirCost"],df["rarity"],s=None,c=None,marker='o',cmap='viridis',norm=None,vmin=0,vmax=10,alpha=0.8,linewidths=1.2,edgecolors='black',)


plt.title("Clash Royale Rarity Elixir Cost")
plt.xlabel("Elixir Cost")
plt.ylabel("Rarity")

plt.grid(False)  # I did this to make it easier to read
plt.tight_layout()
plt.savefig("elixircost.png")


#New Graph

plt.figure(figsize=(8, 5))
plt.bar(df["rarity"], df["Win Rate"], alpha=0.7,)




plt.title("Clash Royale Rarity Elixir Cost")
plt.xlabel("Win Rate")
plt.ylabel("Rarity")

plt.grid(False)  # I did this to make it easier to read
plt.tight_layout()
plt.savefig("winelixir.png")
plt.show()


plt.figure(figsize=(8, 5))

# Two bars for each month: one for NYC, one for LA
