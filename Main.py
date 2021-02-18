import matplotlib.pyplot as plt
   
a = ['JavaScript','Python','HTML/CSS','SQL','Java']
b = [67.8, 41.7, 63.5, 54.4, 41.1]

plt.bar(a, b, color = ['crimson', 'aqua','deeppink','yellow', 'springgreen'])
plt.title('Popularity of Programming Language')
plt.xlabel('Name of Programming Language')
plt.ylabel('Popularity')
plt.show()