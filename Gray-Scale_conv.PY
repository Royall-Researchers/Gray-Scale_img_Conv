from PIL import Image

# Royall-Researchers

print("Gray-Scale Image Converter By")
print( '''  
 ____                   _ _ 
|  _ \ ___  _   _  __ _| | |
| |_) / _ \| | | |/ _` | | |
|  _ < (_) | |_| | (_| | | |
|_| \_\___/ \__, |\__,_|_|_|
            |___/           
 ____                               _                   
|  _ \ ___  ___  ___  __ _ _ __ ___| |__   ___ _ __ ___ 
| |_) / _ \/ __|/ _ \/ _` | '__/ __| '_ \ / _ \ '__/ __|
|  _ <  __/\__ \  __/ (_| | | | (__| | | |  __/ |  \__ \ 
|_| \_\___||___/\___|\__,_|_|  \___|_| |_|\___|_|  |___/
 
''')


print('''	[+]This Tool is Created by Royall Researchers 
	[+]This Tool is only for Educational Purpose 
        [+]no support for illegal or Un Ethical Activities 
        [+]You can Learn More From me 
        [+]Follow More InstaGram : https://instagram.com/royallresearchers 
        [+]Blog : https://royallresearchers.blogspot.com 
        [+]Medium : https://medium.com/@royallresearchers 
        [+]Quora : https://royallresearchers.quora.com 
''')
def convert_to_black_and_white(input_image_path, output_image_path):
    # Open the image file
    img = Image.open(input_image_path)
    
    # Convert the image to grayscale
    bw_img = img.convert("L")
    
    # Save the black and white image
    bw_img.save(output_image_path)

# Example usage
input_image_path = input("Enter Image Path (incl file name) : ") ##enter your Input Image Path
out_img = input("Enter Where The Image want to save (with name of the output image) : ") ##specify where the Output will shown
output_image_path = (out_img )
convert_to_black_and_white(input_image_path, output_image_path)
print("The Given Color Image is Successfully Converted to Gray Scale Image(Black & White) \n")
print("                                  Thank You !             /")

