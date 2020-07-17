from PIL import Image, ImageEnhance,ImageFilter
#       save
# im1=Image.open('kaaba.png')
# im1.save('kaaba.png')
#       show
# im1.show()

#       size
# max_size=(250,250)
# im1.thumbnail(max_size)
# im1.save('kaaba.png')



#           sharpness
# im1=Image.open('kaaba.png')
# enhncr=ImageEnhance.Sharpness(im1)
# enhncr.enhance(4).show()

# #       color
# im1=Image.open('kaaba.png')
# enhncr=ImageEnhance.Color(im1)
# enhncr.enhance(4).show()


#       brightness
# im1=Image.open('kaaba.png')
# enhncr=ImageEnhance.Brightness(im1)
# enhncr.enhance(4).show()



# #       contrass
# im1=Image.open('kaaba.png')
# enhncr=ImageEnhance.Color(im1)
# enhncr.enhance(4).show()



#       blure
# im1=Image.open('kaaba.png')
# im1.filter(ImageFilter.GaussianBlur(radius=4)).show() 