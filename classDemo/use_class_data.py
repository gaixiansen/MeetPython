# encoding:utf-8

import json
from classDemo import class_data
from classDemo import test


jack = class_data.Student()
jack.set_age(12)
jack.set_name("jack")
print(jack)
data = {}
ls = []
data["id"] = 1
ls.append(jack.__str__()) # 重写__str__ 将类的所有属性以字典字符串的形式返回
data["学生"] = ls
js = json.dumps(data)
# 将json格式的字符串写成json文件
js_file = json.dump(data, fp=open("1.json", "w", encoding="utf-8"), ensure_ascii=False, sort_keys=True, indent=4)
print(type(js))
print(js)
py_obj = json.loads(js)
print(type(py_obj))







