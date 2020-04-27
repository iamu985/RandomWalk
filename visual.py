import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    usr = int(input('Set range: '))
    #filling the plots
    rw = RandomWalk(usr)
    rw.fill_walk()
    points = list(range(rw.numb_points))
    plt.figure(figsize = (10, 6))

    plt.scatter(rw.x_val, rw.y_val, c = points, cmap = plt.cm.Blues, edgecolor = 'none', s = 15)
    #emphasize on starting and ending points
    plt.scatter(0, 0, c = 'green', edgecolor = 'none', s = 100)
    plt.scatter(rw.x_val[-1], rw.y_val[-1], c = 'red', edgecolor = 'none', s = 100)

    #Removing axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    usr_ask = input('Wanna draw again(y/n): ')

    if usr_ask == 'n':
        break
