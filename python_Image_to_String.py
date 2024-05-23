from PIL import Image
import pytesseract

# 图片转文字
Image = Image.open("one.jpg")
text = pytesseract.image_to_string(Image)
output_file=open("output_text.txt",mode="w")
output_file.write(text)
print(text)
output_file.close()