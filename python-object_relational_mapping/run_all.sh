#!/bin/bash

# 1. إعطاء صلاحيات التنفيذ لجميع ملفات البايثون
chmod +x *.py

# 2. تشغيل الملفات التي تتطلب اتصل مباشر بقاعدة البيانات (MySQLdb)
# ملاحظة: استبدل root root test_0 ببياناتك (المستخدم، الكلمة، قاعدة البيانات)
echo "--- Running Basic SQL Scripts ---"
./0-select_states.py root root test_0
./1-filter_states.py root root test_0
./2-my_filter_states.py root root test_0
./3-my_safe_filter_states.py root root test_0
./4-cities_by_state.py root root test_0
./5-filter_cities.py root root test_0

# 3. تشغيل الملفات التي تستخدم SQLAlchemy
echo "--- Running SQLAlchemy Scripts ---"
./7-model_state_fetch_all.py root root test_0
./8-model_state_fetch_first.py root root test_0
./10-model_state_my_get.py root root test_0 "Texas"
./11-model_state_insert.py root root test_0
./12-model_state_update_id_2.py root root test_0
./13-model_state_delete_a.py root root test_0
./14-model_city_fetch_by_state.py root root test_0
