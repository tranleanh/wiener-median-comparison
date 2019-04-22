import os
import matplotlib.pyplot as plt
from Median_Filter import median_filter, add_gaussian_noise, rgb2gray
from Wiener_Filter import blur, gaussian_kernel, wiener_filter

if __name__ == '__main__':
	# Load image and convert it to gray scale
	file_name = os.path.join('lena1000p.jpg')
	img = rgb2gray(plt.imread(file_name))

	# Blur image
	blurred_img = blur(img, kernel_size = 9)

	# Add Gaussian noise
	noisy_img = add_gaussian_noise(blurred_img, 20)

	# Apply Median Filter
	median_filter = median_filter(noisy_img, 9)

	# Apply Wiener Filter
	wiener_filter = wiener_filter(noisy_img, gaussian_kernel(9), K = 0.5)

	# Display results
	fig = plt.figure(figsize = (12, 10))

	display = [img, noisy_img, median_filter, wiener_filter]
	title = ['Original image', 'Blurred + Gaussian Noise Added', 
			 'Median Filter', 'Wiener Filter']

	for i in range(len(display)):
		fig.add_subplot(2, 2, i+1)
		plt.imshow(display[i], cmap = 'gray')
		plt.title(title[i])
	
	plt.show()