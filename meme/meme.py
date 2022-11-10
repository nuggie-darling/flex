from PIL import Image, ImageFont, ImageDraw

BackgroundImage = Image.open("deserved.png")
TextType = ImageFont.truetype("impact.ttf", 40)
DrawArea = ImageDraw.Draw(BackgroundImage)
Text = "John Mulaney is \n my father."
DrawArea.multiline_text((1050,450), Text, font=TextType, fill=(0,0,0))

BackgroundImage.show()