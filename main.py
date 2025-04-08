import matplotlib.pyplot as plot
# set up your lists
numlist = [2, 10, 4, 3]
namelist = ['RED', 'GREEN', 'PINK', 'YELLOW']
colorlist = ['red', 'green', 'pink', 'yellow' ]
explodelist = [0.1, 0.0, 0.0, 0.0]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.2f%%', colors=colorlist,
    	explode = explodelist, startangle = 90)
plot.axis('equal')
plot.savefig('piechart.png')

