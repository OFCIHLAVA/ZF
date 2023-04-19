# The Orientation Challenge solution overview
- My solution is missing automation of first and secod step of the user task (data download and image processing). These needs to be done manually for now.
- After first 2 steps are done, result JSON file containing image pixel data structured as dictionary needs to be coppied into same folder in which the script is.
- The user can run the script and rest of the task will be done automaticly. (calculate the colour pixels percentage, save the data for each image to csv file.)

## Solution Details
- 1. Load data from JSON file to get dictionary with all images data in format:
 image_name_1: {count_red_pixels: x,
                count_green_pixels: y,
                count_blue_pixels: z,
                count_others_pixels: a
            },
 image_name_2: {count_red_pixels: x,
                count_green_pixels: y,
                count_blue_pixels: z,
                count_others_pixels: a
            }
etc.
- 2. Using list comprehension, get count (int) of pixels of different colours for all the images in JSON file.
for example:
green_pixels = [image_1_red_pixels_count, image_2_red_pixels_count, ...]
red pixels ...
etc.
- 3. Using built-in SUM function get sum of all the pixels in image files.
- 4. Calculate percentage of each color pixels in all the image files combined. Round to 4 decimal points so we get percentage with 2 decimal places after result*100 ( 0.5655 = 56.55 % )
- 5. Using CSV module, write headings, all the data lines for all images and total percentage for each colour into CSV file. Save CSV file into same folder as the test_script with name "dataID_analysis:.csv"