user_language = {}
LANGUAGES = {
    'en': {
        'start': "Register Gmail accounts and get paid.",
        'keyboard': [['➕ New Gmail'], ['💰 Withdraw']],
        'gmail_info': "First: {first}\nEmail: {email}\nPassword: {password}\nRecovery: {recovery}"
    },
    'bn': {
        'start': "জিমেইল খুলুন এবং টাকা আয় করুন।",
        'keyboard': [['➕ নতুন জিমেইল'], ['💰 উইথড্র করুন']],
        'gmail_info': "নাম: {first}\nইমেইল: {email}\nপাসওয়ার্ড: {password}\nরিকভারি: {recovery}"
    }
}

def get_text(user_id, key):
    lang = user_language.get(user_id, 'en')
    return LANGUAGES.get(lang, LANGUAGES['en']).get(key, '')