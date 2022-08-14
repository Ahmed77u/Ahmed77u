import requests,telebot,os
from telebot import types

status__new = "✅"
status__ch = "✅"
ch_sta = True
new_member = True
channel = "ahmejdjdhd" # channel username without @  /  @ يوزر القناة بدون 
token = "5487383560:AAEqk8ZJQx1J0wwpFww1yk2iEPaYqI4u5m0"
admin_first = "5183888056"
with open("admin.txt","w") as k :
    k.write(admin_first+"\n")
k.close()
bot = telebot.TeleBot(token)
us = bot.get_me().username
@bot.message_handler(commands=['start'])
def send_tool(message):
        k = open("admin.txt","r").read()
        ch_admin1 = open("admins.txt","r").read()
        new_mem_ch = open("users.txt","r").read()
        m = bot.get_chat_member(f"@{channel}",message.from_user.id).status
        if ch_sta == True:
                if str(message.chat.id) in str(k) or str(m) == str("creator") or str(m) == str("administrator") or str(message.chat.id) in ch_admin1:
                    bot.send_message(message.chat.id,"HELLO SIR ! send /admin") #رسالة الادمن
                    bot.send_message(message.chat.id,"- أهلا انا بوت تحميل من تيك توك .\n- فقط ارسلي رابط الفيديو لكي احمله لك بدون حقوق .")
                    
                elif bot.get_chat_member(f"@{channel}",message.from_user.id).status == "member" and new_member != True:
                    if str(message.chat.id) in new_mem_ch:
                        bot.send_message(message.chat.id,"- أهلا انا بوت تحميل من تيك توك .\n- فقط ارسلي رابط الفيديو لكي احمله لك بدون حقوق .") # ثاني رسالة للمستخدم
                    else:
                        with open("users.txt","a") as new: new.write(f"{message.chat.id}\n")
                        new.close()
                        bot.send_message(message.chat.id,"- أهلا انا بوت تحميل من تيك توك .\n- فقط ارسلي رابط الفيديو لكي احمله لك بدون حقوق .") # اول رسالة للمستخدم
                elif bot.get_chat_member(f"@{channel}",message.from_user.id).status == "member" and new_member == True:
                    if str(message.chat.id) in new_mem_ch and new_member == True:
                        bot.send_message(message.chat.id,"- أهلا انا بوت تحميل من تيك توك .\n- فقط ارسلي رابط الفيديو لكي احمله لك بدون حقوق .")
                    elif str(message.from_user.id) not in new_mem_ch:
                        with open("users.txt","a") as new: new.write(f"{message.chat.id}\n")
                        new.close()
                        bot.send_message(message.chat.id,"- أهلا انا بوت تحميل من تيك توك .\n- فقط ارسلي رابط الفيديو لكي احمله لك بدون حقوق .") # ثاني رساله للمستخدم
                        try:
                            for x in open("admin.txt","r").readlines():
                                bot.send_message(x,f"new member\n-------------\nname : {message.from_user.first_name}\nid : {message.from_user.id}")#tofe x
                        except: pass
                elif bot.get_chat_member(f"@{channel}",message.from_user.id).status == "left":
                    bot.send_message(message.chat.id,f"channel : @{channel}") # رسالة الاشتراك الاجباري
                else: 
                    bot.send_message(message.chat.id,f"channel : @{channel}") # رسالة الاشتراك الاجباري
        elif ch_sta == False:
                if str(message.chat.id) in str(new_mem_ch):
                    bot.send_message(message.chat.id,"- أهلا انا بوت تحميل من تيك توك .\n- فقط ارسلي رابط الفيديو لكي احمله لك بدون حقوق .") # ثاني رسالة للمستخدم
                elif str(message.chat.id) not in str(new_mem_ch) and new_member == False:
                    with open("users.txt","a") as new: new.write(f"{message.chat.id}\n")
                    new.close()
                    bot.send_message(message.chat.id,"- أهلا انا بوت تحميل من تيك توك .\n- فقط ارسلي رابط الفيديو لكي احمله لك بدون حقوق .") # اول رسالة للمستخدم
                elif str(message.chat.id) not in str(new_mem_ch) and new_member == True:
                    with open("users.txt","a") as new: new.write(f"{message.chat.id}\n")
                    new.close()
                    try:
                        for x in open("admin.txt","r").readlines():
                            bot.send_message(x,f"new member\n-------------\nname : {message.from_user.first_name}\nid : {message.from_user.id}")
                    except: pass
                    bot.send_message(message.chat.id,"- أهلا انا بوت تحميل من تيك توك .\n- فقط ارسلي رابط الفيديو لكي احمله لك بدون حقوق .") # ثاني رسالة للمستخدم
@bot.message_handler(commands=['admin'])
def send_tool(message):
    num = str(len(open('users.txt', 'r').read().splitlines()))
    global ch_sta,new_member,status__bott
    keyo = types.InlineKeyboardMarkup(row_width=2)
    keyo1 = types.InlineKeyboardMarkup(row_width=2)
    itembtn1 = types.InlineKeyboardButton('تفعيل الاشتراك الاجباري', callback_data="start_ch")
    itembtn2 = types.InlineKeyboardButton('تعطيل الاشتراك الاجباري',callback_data="stop_ch")
    itembtn3 = types.InlineKeyboardButton('تفعيل تنبيه الدخول',callback_data="start_m")
    itembtn4 = types.InlineKeyboardButton('تعطيل تنبيه الدخول',callback_data="stop_m")
    status_new = types.InlineKeyboardButton(f'حالة تنبيه الدخول : {status__new}',callback_data="a123fsac")
    status_ch = types.InlineKeyboardButton(f'حالة الاشتراك الاجباري {status__ch}',callback_data="ae1e")
    itembtn5 = types.InlineKeyboardButton('أرسال نسخة احتياطية',callback_data="send_users")
    itembtn6 = types.InlineKeyboardButton('اذاعة',callback_data="send_all")#tofe x
    itembtn7 = types.InlineKeyboardButton(f'تغيير القناة : {channel}',callback_data="change_channel")
    itembtn8 = types.InlineKeyboardButton(f'اضافة ادمن',callback_data="add_admin")
    itembtn9 = types.InlineKeyboardButton(f'حذف ادمن',callback_data="delete_admin")
    itembtn11 = types.InlineKeyboardButton(f'ارسال لستة الادمنية',callback_data="sendd_admin")
    itembtn10 = types.InlineKeyboardButton(f'عدد مستخدمين البوت : {num}',callback_data="d243n")
    itembtn100 = types.InlineKeyboardButton(f'',callback_data="c14dq")
    keyo.add(itembtn1,itembtn2,status_ch,itembtn100,itembtn3,itembtn4,status_new,itembtn100,itembtn5,itembtn6,itembtn7,itembtn100,itembtn8,itembtn9,itembtn11,itembtn100,itembtn10,itembtn100)#(py_iq)
    keyo1.add(itembtn3,itembtn4,status_new,itembtn100,itembtn6,itembtn100,itembtn10)
    ch_admin = open("admin.txt","r").read()
    ch_admin1 = open("admins.txt","r").read()
    if str(message.from_user.id) in ch_admin: 
         bot.send_message(message.chat.id, "- admin 💳 " , reply_markup = keyo)
    elif str(message.from_user.id) in ch_admin1:
        bot.send_message(message.chat.id, "- admin 💳 " , reply_markup = keyo1)
@bot.callback_query_handler(func=lambda call: True )
def answer(call):
    global ch_sta,new_member,status__ch,status__new,status__bott
    ch_admin = ch_admin = open("admin.txt","r").read()
    ch_admin1 = open("admins.txt","r").read()
    num = str(len(open('users.txt', 'r').read().splitlines()))
    try: 
        if call.data == 'stop_ch' and str(call.message.chat.id) in ch_admin:
            ch_sta = False
            status__ch = "❌"
            keyoo = types.InlineKeyboardMarkup(row_width=2)
            itembtn1 = types.InlineKeyboardButton('تفعيل الاشتراك الاجباري', callback_data="start_ch")
            itembtn2 = types.InlineKeyboardButton('تعطيل الاشتراك الاجباري',callback_data="stop_ch")
            itembtn3 = types.InlineKeyboardButton('تفعيل تنبيه الدخول',callback_data="start_m")
            itembtn4 = types.InlineKeyboardButton('تعطيل تنبيه الدخول',callback_data="stop_m")
            status_new = types.InlineKeyboardButton(f'حالة تنبيه الدخول : {status__new}',callback_data="adasd2134dc")
            status_ch = types.InlineKeyboardButton(f'حالة الاشتراك الاجباري {status__ch}',callback_data="aqwe12ed")
            itembtn3 = types.InlineKeyboardButton('تفعيل تنبيه الدخول',callback_data="start_m")
            itembtn5 = types.InlineKeyboardButton('أرسال نسخة احتياطية',callback_data="send_users")
            itembtn6 = types.InlineKeyboardButton('اذاعة',callback_data="send_all")
            itembtn7 = types.InlineKeyboardButton(f'تغيير القناة : {channel}',callback_data="change_channel")
            itembtn8 = types.InlineKeyboardButton(f'اضافة ادمن',callback_data="add_admin")
            itembtn9 = types.InlineKeyboardButton(f'حذف ادمن',callback_data="delete_admin")
            itembtn11 = types.InlineKeyboardButton(f'ارسال لستة الادمنية',callback_data="sendd_admin")
            itembtn10 = types.InlineKeyboardButton(f'عدد مستخدمين البوت : {num}',callback_data="d243n")
            itembtn100 = types.InlineKeyboardButton(f'',callback_data="c234s12")
            keyoo.add(itembtn1,itembtn2,status_ch,itembtn100,itembtn3,itembtn4,status_new,itembtn100,itembtn5,itembtn6,itembtn7,itembtn100,itembtn8,itembtn9,itembtn11,itembtn100,itembtn10,itembtn100)
            bot.edit_message_text(chat_id=call.message.chat.id,text="- admin 💳 ",message_id=call.message.message_id,reply_markup=keyoo)
    except:
        pass
    try :
        if call.data == 'start_ch' and str(call.message.chat.id) in ch_admin:
            ch_sta = True
            status__ch = "✅"
            keyooo = types.InlineKeyboardMarkup(row_width=2 )
            itembtn1 = types.InlineKeyboardButton('تفعيل الاشتراك الاجباري', callback_data="start_ch")
            itembtn2 = types.InlineKeyboardButton('تعطيل الاشتراك الاجباري',callback_data="stop_ch")
            itembtn3 = types.InlineKeyboardButton('تفعيل تنبيه الدخول',callback_data="start_m")
            itembtn4 = types.InlineKeyboardButton('تعطيل تنبيه الدخول',callback_data="stop_m")
            status_new = types.InlineKeyboardButton(f'حالة تنبيه الدخول : {status__new}',callback_data="mu1st3af4a")
            status_ch = types.InlineKeyboardButton(f'حالة الاشتراك الاجباري {status__ch}',callback_data="asasdofeq213")
            itembtn3 = types.InlineKeyboardButton('تفعيل تنبيه الدخول',callback_data="start_m")
            itembtn5 = types.InlineKeyboardButton('أرسال نسخة احتياطية',callback_data="send_users")
            itembtn6 = types.InlineKeyboardButton('اذاعة',callback_data="send_all")
            itembtn7 = types.InlineKeyboardButton(f'تغيير القناة : {channel}',callback_data="change_channel")
            itembtn8 = types.InlineKeyboardButton(f'اضافة ادمن',callback_data="add_admin")
            itembtn9 = types.InlineKeyboardButton(f'حذف ادمن',callback_data="delete_admin")
            itembtn11 = types.InlineKeyboardButton(f'ارسال لستة الادمنية',callback_data="sendd_admin")
            itembtn10 = types.InlineKeyboardButton(f'عدد مستخدمين البوت : {num}',callback_data="d243n")
            itembtn100 = types.InlineKeyboardButton(f'',callback_data="c234")
            keyooo.add(itembtn1,itembtn2,status_ch,itembtn100,itembtn3,itembtn4,status_new,itembtn100,itembtn5,itembtn6,itembtn7,itembtn100,itembtn8,itembtn9,itembtn11,itembtn100,itembtn10,itembtn100)
            bot.edit_message_text(chat_id=call.message.chat.id,text="- admin 💳 ",message_id=call.message.message_id,reply_markup=keyooo)
    except : pass
    try:
        if call.data == 'start_m' and str(call.message.chat.id) in ch_admin:
            new_member = True
            status__new = "✅"
            keyooo = types.InlineKeyboardMarkup(row_width=2 )
            key11 = types.InlineKeyboardMarkup(row_width=2 )
            itembtn1 = types.InlineKeyboardButton('تفعيل الاشتراك الاجباري', callback_data="start_ch")
            itembtn2 = types.InlineKeyboardButton('تعطيل الاشتراك الاجباري',callback_data="stop_ch")
            itembtn3 = types.InlineKeyboardButton('تفعيل تنبيه الدخول',callback_data="start_m")
            itembtn4 = types.InlineKeyboardButton('تعطيل تنبيه الدخول',callback_data="stop_m")
            status_new = types.InlineKeyboardButton(f'حالة تنبيه الدخول : {status__new}',callback_data="aasd543")
            status_ch = types.InlineKeyboardButton(f'حالة الاشتراك الاجباري {status__ch}',callback_data="amc9d")
            itembtn3 = types.InlineKeyboardButton('تفعيل تنبيه الدخول',callback_data="start_m")
            itembtn5 = types.InlineKeyboardButton('أرسال نسخة احتياطية',callback_data="send_users")
            itembtn6 = types.InlineKeyboardButton('اذاعة',callback_data="send_all")
            itembtn7 = types.InlineKeyboardButton(f'تغيير القناة : {channel}',callback_data="change_channel")
            itembtn8 = types.InlineKeyboardButton(f'اضافة ادمن',callback_data="add_admin")
            itembtn9 = types.InlineKeyboardButton(f'حذف ادمن',callback_data="delete_admin")
            itembtn11 = types.InlineKeyboardButton(f'ارسال لستة الادمنية',callback_data="sendd_admin")
            itembtn10 = types.InlineKeyboardButton(f'عدد مستخدمين البوت : {num}',callback_data="d243n")
            itembtn100 = types.InlineKeyboardButton(f'',callback_data="c1234")
            keyooo.add(itembtn1,itembtn2,status_ch,itembtn100,itembtn3,itembtn4,status_new,itembtn100,itembtn5,itembtn6,itembtn7,itembtn100,itembtn8,itembtn9,itembtn11,itembtn100,itembtn10,itembtn100)
            bot.edit_message_text(chat_id=call.message.chat.id,text="- admin 💳 ",message_id=call.message.message_id,reply_markup=keyooo)
        if call.data == "start_m" and str(call.message.chat.id) in ch_admin1:
            new_member = True
            status__new = "✅"
            key11 = types.InlineKeyboardMarkup(row_width=2 )
            itembtn3 = types.InlineKeyboardButton('تفعيل تنبيه الدخول',callback_data="start_m")
            itembtn4 = types.InlineKeyboardButton('تعطيل تنبيه الدخول',callback_data="stop_m")
            status_new = types.InlineKeyboardButton(f'حالة تنبيه الدخول : {status__new}',callback_data="aqwed22")
            itembtn6 = types.InlineKeyboardButton('اذاعة',callback_data="send_all")
            itembtn10 = types.InlineKeyboardButton(f'عدد مستخدمين البوت : {num}',callback_data="d243n")
            itembtn100 = types.InlineKeyboardButton(f'',callback_data="c1324141")
            key11.add(itembtn3,itembtn4,status_new,itembtn100,itembtn6,itembtn100,itembtn10)
            bot.edit_message_text(chat_id=call.message.chat.id,text="- admin 💳 ",message_id=call.message.message_id,reply_markup=key11)
    except: pass
    try:
        if call.data == 'stop_m' and str(call.message.chat.id) in ch_admin:
            new_member = False
            status__new = "❌"
            keyooo11 = types.InlineKeyboardMarkup(row_width=2 )
            keyooo = types.InlineKeyboardMarkup(row_width=2 )
            itembtn1 = types.InlineKeyboardButton('تفعيل الاشتراك الاجباري', callback_data="start_ch")
            itembtn2 = types.InlineKeyboardButton('تعطيل الاشتراك الاجباري',callback_data="stop_ch")
            itembtn3 = types.InlineKeyboardButton('تفعيل تنبيه الدخول',callback_data="start_m")
            itembtn4 = types.InlineKeyboardButton('تعطيل تنبيه الدخول',callback_data="stop_m")
            status_new = types.InlineKeyboardButton(f'حالة تنبيه الدخول : {status__new}',callback_data="aqwed22")
            status_ch = types.InlineKeyboardButton(f'حالة الاشتراك الاجباري {status__ch}',callback_data="a123dq")
            itembtn3 = types.InlineKeyboardButton('تفعيل تنبيه الدخول',callback_data="start_m")
            itembtn5 = types.InlineKeyboardButton('أرسال نسخة احتياطية',callback_data="send_users")
            itembtn6 = types.InlineKeyboardButton('اذاعة',callback_data="send_all")
            itembtn7 = types.InlineKeyboardButton(f'تغيير القناة : {channel}',callback_data="change_channel")
            itembtn8 = types.InlineKeyboardButton(f'اضافة ادمن',callback_data="add_admin")
            itembtn9 = types.InlineKeyboardButton(f'حذف ادمن',callback_data="delete_admin")
            itembtn11 = types.InlineKeyboardButton(f'ارسال لستة الادمنية',callback_data="sendd_admin")
            itembtn10 = types.InlineKeyboardButton(f'عدد مستخدمين البوت : {num}',callback_data="d243n")
            itembtn100 = types.InlineKeyboardButton(f'',callback_data="c1324141")
            keyooo.add(itembtn1,itembtn2,status_ch,itembtn100,itembtn3,itembtn4,status_new,itembtn100,itembtn5,itembtn6,itembtn7,itembtn100,itembtn8,itembtn9,itembtn11,itembtn100,itembtn10,itembtn100)
            bot.edit_message_text(chat_id=call.message.chat.id,text="- admin 💳 ",message_id=call.message.message_id,reply_markup=keyooo)
        if call.data == "stop_m" and str(call.message.chat.id) in ch_admin1:
            new_member = False
            status__new = "❌"
            keyooo11 = types.InlineKeyboardMarkup(row_width=2 )
            itembtn3 = types.InlineKeyboardButton('تفعيل تنبيه الدخول',callback_data="start_m")
            itembtn4 = types.InlineKeyboardButton('تعطيل تنبيه الدخول',callback_data="stop_m")
            status_new = types.InlineKeyboardButton(f'حالة تنبيه الدخول : {status__new}',callback_data="aqwed22")
            itembtn6 = types.InlineKeyboardButton('اذاعة',callback_data="send_all")
            itembtn10 = types.InlineKeyboardButton(f'عدد مستخدمين البوت : {num}',callback_data="d243n")
            itembtn100 = types.InlineKeyboardButton(f'',callback_data="c1324141")
            keyooo11.add(itembtn3,itembtn4,status_new,itembtn100,itembtn6,itembtn100,itembtn10)
            bot.edit_message_text(chat_id=call.message.chat.id,text="- admin 💳 ",message_id=call.message.message_id,reply_markup=keyooo11)
    except: pass
    try:
        if call.data == "send_users" and str(call.message.chat.id) in ch_admin:
            bot.send_document(chat_id=call.message.chat.id,data =open("users.txt","rb"),caption="تم انشاء نسخة احتياطية")
            keyoooo = types.InlineKeyboardMarkup(row_width=2 )
            itembtn1 = types.InlineKeyboardButton('تفعيل الاشتراك الاجباري', callback_data="start_ch")
            itembtn2 = types.InlineKeyboardButton('تعطيل الاشتراك الاجباري',callback_data="stop_ch")
            itembtn3 = types.InlineKeyboardButton('تفعيل تنبيه الدخول',callback_data="start_m")
            itembtn4 = types.InlineKeyboardButton('تعطيل تنبيه الدخول',callback_data="stop_m")
            status_new = types.InlineKeyboardButton(f'حالة تنبيه الدخول : {status__new}',callback_data="aadsf")
            status_ch = types.InlineKeyboardButton(f'حالة الاشتراك الاجباري {status__ch}',callback_data="a3gw")
            itembtn3 = types.InlineKeyboardButton('تفعيل تنبيه الدخول',callback_data="start_m")
            itembtn5 = types.InlineKeyboardButton('أرسال نسخة احتياطية',callback_data="send_users")
            itembtn6 = types.InlineKeyboardButton('اذاعة',callback_data="send_all")
            itembtn7 = types.InlineKeyboardButton(f'تغيير القناة : {channel}',callback_data="change_channel")
            itembtn8 = types.InlineKeyboardButton(f'اضافة ادمن',callback_data="add_admin")
            itembtn9 = types.InlineKeyboardButton(f'حذف ادمن',callback_data="delete_admin")
            itembtn11 = types.InlineKeyboardButton(f'ارسال لستة الادمنية',callback_data="sendd_admin")
            itembtn10 = types.InlineKeyboardButton(f'عدد مستخدمين البوت : {num}',callback_data="d243n")
            itembtn100 = types.InlineKeyboardButton(f'',callback_data="cfqw3")
            keyoooo.add(itembtn1,itembtn2,status_ch,itembtn100,itembtn3,itembtn4,status_new,itembtn100,itembtn5,itembtn6,itembtn7,itembtn100,itembtn8,itembtn9,itembtn11,itembtn100,itembtn10,itembtn100)
            bot.edit_message_text(chat_id=call.message.chat.id,text="- admin 💳 ",message_id=call.message.message_id,reply_markup=keyoooo)
    except: pass
    try:
        if call.data == "send_all" and str(call.message.chat.id) in ch_admin : 
            bot.send_message(chat_id=call.message.chat.id,text="""[الكلمة](الرابط)\n*الكلام حيصير عميق*\n_الخط حيصير مائل_""")
            botbod = bot.send_message(call.message.chat.id,"أرسل الرسالة لأقوم بتوجيهها",parse_mode="MARKDOWN")
            bot.register_next_step_handler(botbod , bodcast)
    except: pass
    try:
        if call.data == "send_all" and str(call.message.chat.id) in ch_admin1 : 
            botbod = bot.send_message(call.message.chat.id,"أرسل الرسالة لأقوم بتوجيهها",parse_mode="MARKDOWN")
            bot.register_next_step_handler(botbod , bodcast)
    except: pass
    try:
        if call.data == "change_channel" and str(call.message.chat.id) in ch_admin:
            new_chan = bot.send_message(call.message.chat.id,"أرسل يوزر القناة بدون @ - ارفع البوت ادمن قبل لا تدز القناة",parse_mode="MARKDOWN")
            bot.register_next_step_handler(new_chan , channel_chch)
    except: pass
    try:
        if call.data == "add_admin" and str(call.message.chat.id) in ch_admin:
            admin_neww = bot.send_message(call.message.chat.id,"أرسل ايدي الادمن الجديد",parse_mode="MARKDOWN")
            bot.register_next_step_handler(admin_neww , adminnnn_new)
    except: pass
    try:
        if call.data == "delete_admin" and str(call.message.chat.id) in ch_admin:
            admin_list = open("admins.txt","r").read()
            bot.send_message(call.message.chat.id,f"\n{admin_list}\n")
            admin_delete = bot.send_message(call.message.chat.id,"أرسل ايدي الادمن الذي تريد أزالته",parse_mode="MARKDOWN")
            bot.register_next_step_handler(admin_delete , admin_deletee)
    except: pass
    try:
        try:
            if call.data == "sendd_admin" and str(call.message.chat.id) in ch_admin : 
                largestring = open("admins.txt","r").read()
                lines = largestring.split("\n")

                non_empty_lines = [line for line in lines if line.strip() != ""]


                string_without_empty_lines = ""

                for line in non_empty_lines:

                    string_without_empty_lines += line + "\n"

                with open("admins.txt","w") as llq:
                    llq.write(string_without_empty_lines)
                bot.send_document(call.message.chat.id,data=open("admins.txt","rb"),caption=f"{str(len(open('admins.txt', 'r').read().splitlines()))}: عدد الادمنبة  ")
        except: bot.send_message(call.message.chat.id,"لا يوجد ادمنية")  
    except:pass
def channel_chch(message):
    global channel,new_chan
    cid = message.chat.id
    msg_chchchch= message.text
    try:
        check_channel = bot.get_chat(f"@{msg_chchchch}")
        if check_channel.type == "channel" and str(check_channel.invite_link) != str("None") and "@" not in message.text :
            channel = str(msg_chchchch)
            bot.send_message(message.chat.id,"تم اضافة القناة بنجاح")
        elif check_channel.type != "channel":
            bot.send_message(message.chat.id,"أرسل يوزر قناة صحيح")
        elif str(check_channel.invite_link) == str("None"):
            bot.send_message(message.chat.id,"تأكد من رفع البوت ادمن")
        else:
            bot.send_message(message.chat.id,"أرسل يوزر صحيح")
    except: bot.send_message(message.chat.id,"أرسل يوزر صحيح")

def bodcast(message):
    global botbod
    cid = message.chat.id
    msg_bod= message.text
    for x in open("users.txt","r").readlines():
        try:
            bot.send_message(x,msg_bod,parse_mode="MARKDOWN")
        except:
            pass
    bot.send_message(message.chat.id,"تمت سيدي")
def adminnnn_new(message):
    global admin_new
    cid = message.chat.id
    admin_new= message.text
    with open("admins.txt","a") as kl :
        kl.write(admin_new+"\n")
    bot.send_message(message.chat.id,"تمت اضافته")
def admin_deletee(message):
    global admin_delete
    cid = message.chat.id
    admin_dede= message.text
    dd = open("admins.txt","r").read()
    if str(admin_dede) in str(dd):
        d = dd.replace(admin_dede,"")
        with open("admins.txt","w") as kl :
            kl.write(d+"\n")
        bot.send_message(message.chat.id,"تمت أزالته")


@bot.message_handler(regexp=r"(.*)tiktok(.*)")
def t(message):
    m = message.text
    idd = message.from_user.id
    mc = message.chat.id
    url = "https://www.tikwm.com/api/?url={}".format(m)
    res = requests.get(url).json()
    video = res['data']['play']
    title = res['data']['title']
    time1=res["processed_time"]
    share = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="- مشاركه .",url='https://t.me/share/url?url={}'.format(m))
    share.row_width = 2
    share.add(button)
    bot.send_video(mc,video,caption=f'- @{us} .\n𖡋 𝐓𝐈𝐌 : {time1} ',reply_markup=share,reply_to_message_id=message.message_id)
    
bot.polling(none_stop=True)