import itertools
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CommandHandler, CallbackQueryHandler

possible_combinations = []

def start(update: Update, _: CallbackContext) -> None:
    update.message.reply_text('Welcome to the Telegram Permutation-Combination Bot! Please provide numbers or letters as input. make your input space separated.')

def process_input(update: Update, _: CallbackContext) -> None:
    global possible_combinations
    user_input = update.message.text.split()
    input_list = list(user_input)  # Convert input to a list of characters
    possible_combinations = [''.join(permutation) for permutation in itertools.permutations(input_list)]
    keyboard = [[InlineKeyboardButton("Show Combinations", callback_data='show_combinations')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(f'Total {len(possible_combinations)} possible combinations. Click the button below to see them.', reply_markup=reply_markup)


def button_click_handler(update: Update, _: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    formatted_output = '\n'.join(possible_combinations)
    query.message.reply_text(f'Possible combinations:\n{formatted_output}')


#Developer Section
def developer(update: Update, context: CallbackContext) -> None:
    mail = "eajahmed5110@gmail.com"
    update.message.reply_text(
        f"Hello World! This Bot is Developed by EAJUDDIN AHMED. \n \nEAJUDDIN is a Front-end Web Developer and WordPress Expert. Also he is a great Telegram Bot Developer \nContact Information: \n \nTelegram : @eajahmed \n \nLinkedin: https://www.linkedin.com/in/eajahmed \n \nMail : {mail} \n \nWhatsApp: +8801316032483"
        )

def main() -> None:
    #Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token.
    TOKEN = 'YOUR_BOT_TOKEN' 

    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, process_input))
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button_click_handler, pattern='^show_combinations$'))
    updater.dispatcher.add_handler(CommandHandler("Developer", developer))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
