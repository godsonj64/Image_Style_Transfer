# Image_Style_Transfer
The Image Style Transfer extracts features from a reference image and applies its style to a target image using histogram matching.  
It also provides functionality to enhance the processed image by adjusting brightness, contrast, and color. The results, including the reference image, original image, and processed image with their features, are visualized using comprehensive plots.

Features

Feature Extraction: Extracts various features such as brightness, contrast, hue, saturation, vibrance, color moments, and color coherence vector (CCV) from the images.

Style Transfer: Applies the style of the reference image to the target image using histogram matching.

Image Enhancement: Enhances the processed image by adjusting brightness, contrast, and color.
Visualization: Plots the reference image, original target image, and processed target image along with their respective features.
![result4](https://github.com/user-attachments/assets/0e020632-f4d6-4abf-9d1e-d9addab57eed)
![reslut2](https://github.com/user-attachments/assets/e81435cd-294b-44d4-8ab2-9b29b329081b)


Requirements

Python 3.x
OpenCV
scikit-image
matplotlib
Pillow
Installation

Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/image-style-transfer.git
cd image-style-transfer
Create a Virtual Environment:

bash
Copy code
python -m venv venv
Activate the Virtual Environment:

On Windows:

bash
Copy code
venv\Scripts\activate
On macOS and Linux:

bash
Copy code
source venv/bin/activate
Install the Dependencies:

bash
Copy code
pip install -r requirements.txt
Usage

Set the Paths for the Reference and Target Images:

Update the reference_image_path and target_image_path variables in the main function with the paths to your reference and target images.

python
Copy code
reference_image_path = 'path/to/your/reference_image.jpg'
target_image_path = 'path/to/your/target_image.jpg'
Run the Script:

bash
Copy code
python image_style_transfer.py
View the Results:

The script will display the reference image, original target image, and processed target image along with their respective features in a comprehensive plot.


Detailed Explanation of the Code

ImageStyleTransfer Class
This class handles the extraction of image features, applying style from a reference image to a target image, and enhancing the processed image.

__init__(): Initializes the class and sets self.reference_features to None.
extract_features(image_path=None, image_rgb=None): Extracts features from an image given its path or directly from an RGB image array.
save_reference_features(features): Saves the extracted features of the reference image.
apply_style(target_image_path): Applies the style of the reference image to the target image using histogram matching.
enhance_image(image, brightness=1.0, contrast=1.0, color=1.0): Enhances the image by adjusting brightness, contrast, and color.
plot_results(reference_image, reference_features, original_image, original_features, processed_image, processed_features, title): Plots the reference image, original image, and processed image along with their features.
main Function
The main function performs the following tasks:

Sets the paths for the reference and target images.
Initializes the ImageStyleTransfer class.
Extracts and saves features from the reference image.
Extracts features from the original target image.
Applies the style to the target image and enhances it.
Extracts features from the processed image.
Plots the results.
Example

Here's a simple example of how to use the ImageStyleTransfer class:

python
Copy code
reference_image_path = 'path/to/your/reference_image.jpg'
target_image_path = 'path/to/your/target_image.jpg'

image_style_transfer = ImageStyleTransfer()

# Extract features from the reference image and save them
reference_features = image_style_transfer.extract_features(reference_image_path)
image_style_transfer.save_reference_features(reference_features)
reference_image = reference_features['image']

# Extract features from the original target image
original_features = image_style_transfer.extract_features(target_image_path)
original_image = original_features['image']

# Apply the style to the target image and enhance it
styled_image = image_style_transfer.apply_style(target_image_path)
enhanced_image = image_style_transfer.enhance_image(styled_image, brightness=1.1, contrast=1.1, color=1.0)

# Extract features from the processed image
processed_features = image_style_transfer.extract_features(image_rgb=enhanced_image)
processed_features['image'] = enhanced_image

# Plot the results
image_style_transfer.plot_results(reference_image, reference_features, original_image, original_features,
                                  enhanced_image, processed_features, 'Image Style Transfer Results')
Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

