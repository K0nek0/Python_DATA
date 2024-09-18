from PIL import Image, ImageDraw, ImageFont


def create_card(number, output_image_path):
    img_size = (100, 100)

    card = Image.new('RGB', img_size, color='white')
    font = ImageFont.truetype("arial.ttf", size=50)

    draw = ImageDraw.Draw(card)
    border_color = 'blue'
    border_thickness = 5

    draw.rectangle(
        [border_thickness // 2, border_thickness // 2,
         img_size[0] - border_thickness // 2,
         img_size[1] - border_thickness // 2],
        outline=border_color, width=border_thickness
    )

    text_color = 'red'
    text = str(number)
    text_position = (img_size[0] // 2, img_size[1] // 2)
    draw.text(text_position, text, anchor='mm', fill=text_color, font=font)

    card.save(output_image_path, 'PNG')
    card.show()


for i in range(1, 4):
    create_card(i, f'card_{i}.png')
