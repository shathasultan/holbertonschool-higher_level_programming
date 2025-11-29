#!/usr/bin/python3

# هذا الكود لن يعمل إلا عند التشغيل المباشر
if __name__ == "__main__":
    import marshal  # لقراءة الكود من ملفات .pyc

    # افتح الملف الثنائي
    with open("/tmp/hidden_4.pyc", "rb") as f:
        f.read(16)          # تخطي الـ header للملف .pyc
        code = marshal.load(f)  # قراءة الكود المخزن

    # استخرج كل الأسماء المعرفة في الملف
    for name in sorted(code.co_names):  # الترتيب أبجدي
        if not name.startswith("__"):   # تجاهل أسماء النظام
            print(name)                 # اطبع الاسم
