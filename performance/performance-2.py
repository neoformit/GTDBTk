color_setup = ['#5a6855','red','color']
setup = color_setup
pool_size_list=[10, 50, 100, 200, 500, 1000, 2000, 5000]
split_list=[x/60 for x in [88, 150, 160, 169, 195, 235, 312, 558]]
nosplit_list=[x/60 for x in [137, 151, 163, 180, 219, 280, 416, 934]]
values = [10,500,1000,1500,2000,2500,3000,3500,4000,4500,5000]

plt.scatter(pool_size_list, split_list, label="GTDB-Tk v2" , marker="s", s=30, color=setup[0])
plt.plot(pool_size_list, split_list,linestyle='dashed', color=setup[0])
plt.scatter(pool_size_list, nosplit_list, label="GTDB-Tk v1",color=setup[1])
plt.plot(pool_size_list, nosplit_list,linestyle=':', color=setup[1])

# naming the x axis

plt.xticks(values)
plt.yticks([1,3,5,7,9,11,13,15])

# naming the axis
plt.ylabel('Runtime (h)')
plt.xlabel('Number of genomes')
# giving a title to my graph
plt.title('Fig.2: GTDB-Tk runtime with 32CPUs')

# show a legend on the plot
plt.legend(loc=2, prop={'size': 12},frameon=False)

# function to show the plot
plt.show()