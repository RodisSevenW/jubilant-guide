from PIL import Image, ImageDraw, ImageFont
import random
from requests import get as gget





def bg():

    url = 'https://api.yimian.xyz/img?type=wallpaper'
    img = gget(url).content
    img2 = gget(url).content
    img3 = gget(url).content
    with open('1.jpg', 'wb') as fp:
        fp.write(img)
    with open('2.jpg', 'wb') as fp:
        fp.write(img2)
    with open('3.jpg', 'wb') as fp:
        fp.write(img3)

def run(i):
    bg()
    hour = random.randint(9, 23)
    minute = random.randint(0, 59)
    time_text = "{:02d}:{:02d}".format(hour, minute)
    n = gget('https://v.api.aa1.cn/api/api-xingming/index.php')
    n2 = gget('https://v.api.aa1.cn/api/api-xingming/index.php')
    data = n.json()
    data2 = n2.json()
    name = data['xingming']
    name2 = data2['xingming']
    print(name)

    wd = 'http://api.txapi.cn/v1/c/love_talk'
    token = {
        "token": "jQOGJzGjz0ZmIM"
    }
    data3 = gget(wd, token)
    data3 = data3.json()
    data3 = data3['data'][:20]
    try:
        data4 = data3['data'][20:-1]
    except Exception as err:
        pass

    # 打开主图像和要覆盖的图像
    main_image = Image.open("./image/bj.png")   # 背景
    rwl_image = Image.open("./image/rwl.png")   # 任务栏
    xj_image = Image.open("./image/xj.png")   # 相机
    t_image = Image.open(("./image/t.png"))
    bottom_image = Image.open("1.jpg")  # 爬取的图片
    bottom_image2 = Image.open("2.jpg")  # 爬取的图片
    bottom_imaget = Image.open("3.jpg")  # 爬取的图片



    # 调整要覆盖的图像的大小和长宽比
    rwl_image = rwl_image.resize((293, 85))
    xj_image = xj_image.resize((100, 70))
    t_image = t_image.resize((1173,124))

    # 裁剪爬取的图片到500x500
    bottom_image = bottom_image.resize((1920,1040))
    bottom_image2 = bottom_image2.resize((210,210))
    bottom_image3 = bottom_image2.resize((128,129))
    bottom_imaget = bottom_imaget.resize((128, 129))

    # 将裁剪后的图片放置在左上角
    main_image.paste(bottom_image, (0, 0))
    main_image.paste(bottom_image2, (925, 895))
    main_image.paste(bottom_image3, (55, 1263))
    main_image.paste(bottom_imaget, (55, 2346))   #下图


    draw = ImageDraw.Draw(main_image)
    font = ImageFont.truetype("arial.ttf", 45)  # 使用合适的字体和字号
    #text_width, text_height = draw.textsize(time_text, font=font)
    text_position = (135, 55)  # 左上角位置
    draw.text(text_position, time_text, font=font, fill=(0, 0, 0))  # 白色文本

    draw = ImageDraw.Draw(main_image)
    #font = ImageFont.truetype(".msyh.ttf", 45)  # 使用合适的字体和字号
    font_path = "simhei.ttf"  # 替换为你的字体文件路径
    font = ImageFont.truetype(font_path, 50)
    #text_width, text_height = draw.textsize(time_text, font=font)
    name_position = (720, 960)  # 左上角位置
    draw.text(name_position, name, font=font, fill=(255, 255, 255))  # 白色文本

    draw = ImageDraw.Draw(main_image)
    font_path = "simhei.ttf"  # 替换为你的字体文件路径
    font = ImageFont.truetype(font_path, 45)
    # text_width, text_height = draw.textsize(time_text, font=font)
    name_position2 = (215, 1260)  # 左上角位置
    draw.text(name_position2, name, font=font, fill=(91, 106, 145))  # 白色文本

    #下
    draw = ImageDraw.Draw(main_image)
    # font = ImageFont.truetype(".msyh.ttf", 45)  # 使用合适的字体和字号
    font_path = "simhei.ttf"  # 替换为你的字体文件路径
    font = ImageFont.truetype(font_path, 45)
    # text_width, text_height = draw.textsize(time_text, font=font)
    name_position3 = (215, 2343)  # 左上角位置
    draw.text(name_position3, name2, font=font, fill=(91, 106, 145))  # 白色文本

    draw = ImageDraw.Draw(main_image)
    # font = ImageFont.truetype(".msyh.ttf", 45)  # 使用合适的字体和字号
    font_path = "simhei.ttf"  # 替换为你的字体文件路径
    font = ImageFont.truetype(font_path, 45)
    # text_width, text_height = draw.textsize(time_text, font=font)
    name_position4 = (217, 2415)  # 左上角位置
    draw.text(name_position4, data3, font=font, fill=(0, 0, 0))

    try:
        draw = ImageDraw.Draw(main_image)
        # font = ImageFont.truetype(".msyh.ttf", 45)  # 使用合适的字体和字号
        font_path = "simhei.ttf"  # 替换为你的字体文件路径
        font = ImageFont.truetype(font_path, 45)
        # text_width, text_height = draw.textsize(time_text, font=font)
        name_position4 = (217, 2453)  # 左上角位置
        draw.text(name_position4, data4, font=font, fill=(0, 0, 0))
    except Exception as err:
        pass

    # 创建一个新的图像，作为结果
    result_image = Image.new("RGB", main_image.size)

    # 将主图像复制到结果图像中
    result_image.paste(main_image, (0, 0))

    # 任务栏位置
    result_image.paste(rwl_image, (821, 35), mask=rwl_image)

    # 相机位置
    result_image.paste(xj_image, (1033, 171), mask=xj_image)

    #结束位置
    result_image.paste(t_image, (0, 2143), mask=t_image)

    # 保存结果图像
    result_image.save(f"./save/result_image{i}.jpg")

for i in range(10):
    try:
        run(i)
    except Exception as err:
        print(err)