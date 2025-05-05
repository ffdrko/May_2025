user_name = "Fahim"
print(len(user_name))
print(user_name.upper())
print(user_name.lower())

name = "!!!Faisal!!!"
print(name.rstrip('!'))
print(name.lstrip('!'))
print(name.strip('!'))
print(name.replace('Faisal', 'Deepto'))

name_lst = "Fahim Faisal Deepto"
print(name_lst.split(" "))

blog_text = "introduction to js"
print(blog_text.capitalize())
print(blog_text.title())
print(len(blog_text))
print(blog_text.center(50))
print(blog_text.count("to"))
print(blog_text.startswith("intro"))
print(blog_text.endswith("js"))

print(blog_text.find('to'))
print(blog_text.index('to'))

print(user_name.isalnum())
print(user_name.isalpha())