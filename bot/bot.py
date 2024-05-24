import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import requests

# إعدادات البوت
TOKEN = 'التوكن الخاص بالبوت'
API_URL = 'https://flask-api.onrender.com/vlan_data'  #رابط السرفر

# إعداد تسجيل الدخول
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# دالة لبدء البوت
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("تسمية الفيلانات", callback_data='name_vlans')],
        [InlineKeyboardButton("تحديد وقت الإرسال", callback_data='set_time')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('اختر الإجراء:', reply_markup=reply_markup)

# دالة لتنفيذ الإجراءات
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    if query.data == 'name_vlans':
        vlans = requests.get(API_URL).json()
        for vlan in vlans:
            query.message.reply_text(f"VLAN: {vlan['name']}")
    elif query.data == 'set_time':
        keyboard = [
            [InlineKeyboardButton("يوميًا", callback_data='daily')],
            [InlineKeyboardButton("أسبوعيًا", callback_data='weekly')],
            [InlineKeyboardButton("شهريًا", callback_data='monthly')],
            [InlineKeyboardButton("تحديد الكل", callback_data='all')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.reply_text('اختر وقت الإرسال:', reply_markup=reply_markup)

def main() -> None:
    # إعداد البوت
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
