import matplotlib.pylab as plt
from API import transfer_style


if __name__=="__main__":

    # Path of the pre-trained TF model 
    model_path = r"C:\Users\sakkiah\Desktop\Myapp\working\model\Neural-Style-Transfer\model"

    # NOTE : Works only for '.jpg' and '.png' extensions,other formats may give error
    content_image_path = r"C:\Users\sakkiah\Desktop\Myapp\working\model\art1.png"
    style_image_path = r"C:\Users\sakkiah\Desktop\Myapp\working\model\art2.png"

    img = transfer_style(content_image_path,style_image_path,model_path)
    # Saving the generated image
    plt.imsave('stylized_image.jpeg',img)
    plt.imshow(img)
    plt.show()

