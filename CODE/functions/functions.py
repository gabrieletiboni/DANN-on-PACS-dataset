import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

def plotBar(data1, data2, data3, data4, classes, color='#3949AB'):
	# unique, counts = np.unique(data, return_counts=True)
	# print('Mean images per class:', counts.mean())
	# print('Std images per class:', counts.std())

	unique, counts1 = np.unique(data1, return_counts=True)
	unique, counts2 = np.unique(data2, return_counts=True)
	unique, counts3 = np.unique(data3, return_counts=True)
	unique, counts4 = np.unique(data4, return_counts=True)

	fig, ax = plt.subplots(nrows=1, ncols=1)
	ax.set_title('Distribution of classes across domains', pad=20.0, alpha=0.85, fontweight='bold')

	width=0.18

	# plt.bar(unique, counts, width=width, color=color)
	plt.bar(unique-2*(width)+(width/2), counts1, width=width, color='#3949AB70', edgecolor='#3949AB95', linewidth=0.5, label='Photo')
	plt.bar(unique-(width/2), counts2, width=width, color='#f4433670', edgecolor='#f4433695', linewidth=0.5, label='Art paintings')
	plt.bar(unique+(width/2), counts3, width=width, color='#388E3C70', edgecolor='#388E3C95', linewidth=0.5, label='Cartoon')
	plt.bar(unique+2*(width)-(width/2), counts4, width=width, color='#FF8F0070', edgecolor='#FF8F0095', linewidth=0.5, label='Sketch')

	plt.xticks(rotation=45, ha='right', rotation_mode='anchor')

	ax.set_xticks(unique)
	ax.set_xticklabels([(classe[0].upper()+classe[1:]) for classe in classes])

	plt.grid(alpha=0.2, axis='y')

	ax.legend()
	plt.show()


def imgshow(img):
	img = img / 2 + 0.5     # unnormalize
	npimg = img.numpy()
	plt.imshow(np.transpose(npimg, (1, 2, 0)))
	plt.show()

	return