import matplotlib.pyplot as plt # Importing the module

a = ['JavaScript','Python','HTML/CSS','SQL','Java'] # Giving it Data to Plot.
b = [67.8, 41.7, 63.5, 54.4, 41.1] # Giving Y-Axis Coordinates to Plot the Graph in Correct Length.

plt.bar(a, b, color = ['crimson', 'aqua','deeppink','yellow', 'springgreen']) # Displaying the graph.
plt.title('Popularity of Programming Language') # Giving the Title to the Graph.
plt.xlabel('Name of Programming Language') # Giving Name to X-Axis.
plt.ylabel('Popularity') # Giving Name to Y-Axis.
plt.show() # Displaying the Graph to the User.