# filename: happy_birthday.py
"""A basic (single function) API written using hug"""
import hug
from hug import types
from jinja2 import FileSystemLoader, Environment

template_engine = Environment(loader=FileSystemLoader("templates"))

def get_template(name):
    return template_engine.get_template(name)


@hug.get('/api/ads')
def list(limit:types.number=10):
    ad = {
        'title': '年底冲量！江淮、解放、东风、福田等贷款提车',
        'desc': '上海旭坤常年出售​‌‌新货车销售业务3.2米双排座 ‌‌ 3.8米带卧铺 4.2‌‌米单排 5.2米有单排有带卧铺 6.2米以上车型都是带卧铺的 6.8米 7.7米 8.6米 9.6米 前四后四 前四后六 前四后八 厢式车 栏板车 栅栏车 冷藏车 危险品车 江淮：帅铃 、康铃、 骏铃、新款骏铃V6 格尔发K3 格尔发A5 格尔发K5 格尔发K6 K5L K3L K3X K5X K3W K5W 解放 ：一汽菱源国五 J6F 、J6L 、J6M 、J6P、青岛解放、虎V、悍V 、龙V 、途V、天V 。东风：多利卡、东风天锦、东风天龙、东风锐铃、东风凯普特。',
        'image': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1517315972999&di=14e221127e70ac22054342d0ddc125bb&imgtype=0&src=http%3A%2F%2Fa1.att.hudong.com%2F38%2F84%2F19300533963554135544845328746.jpg'
    }
    return [ad for i in range(limit)]


@hug.static('/csr')
def my_static_dirs():
    return('../csr',)


@hug.get(output=hug.output_format.html)
def ssr():
    return get_template("list.html").render({'ads': list() + list()})
