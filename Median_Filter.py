import os
import numpy as np
import matplotlib.pyplot as plt

def median_filter(data, kernel_size):
    temp = []
    indexer = kernel_size // 2
    data_final = []
    data_final = np.zeros((len(data),len(data[0])))
    for i in range(len(data)):

        for j in range(len(data[0])):

            for z in range(kernel_size):
                if i + z - indexer < 0 or i + z - indexer > len(data) - 1:
                    for c in range(kernel_size):
                        temp.append(0)
                else:
                    if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
                        temp.append(0)
                    else:
                        for k in range(kernel_size):
                            temp.append(data[i + z - indexer][j + k - indexer])

            temp.sort()
            data_final[i][j] = temp[len(temp) // 2]
            temp = []
    return data_final

def add_gaussian_noise(img, sigma):
    gauss = np.random.normal(0, sigma, np.shape(img))
    noisy_img = img + gauss
    noisy_img[noisy_img < 0] = 0
    noisy_img[noisy_img > 255] = 255
    return noisy_img

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])


if __name__ == '__main__':
    # Load image and convert it to gray scale
    file_name = os.path.join('lena1000p.jpg')
    img = rgb2gray(plt.imread(file_name))

    # Add Gaussian noise
    noisy_img = add_gaussian_noise(img, 30)

    # Apply Median Filter
    removed_noise_3 = median_filter(noisy_img, 3)
    removed_noise_5 = median_filter(noisy_img, 5)

    # Display results
    fig = plt.figure(figsize = (12, 10))
    display = [img, noisy_img, removed_noise_3, removed_noise_5]
    title = ['Original Image', 'Gaussian Noise Added', '3x3 Median Filter', '5x5 Median Filter']

    for i in range(len(display)):
        fig.add_subplot(2, 2, i+1)
        plt.imshow(display[i], cmap = 'gray')
        plt.title(title[i])
    
    plt.show()