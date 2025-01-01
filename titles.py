# Titles for chatGPT bot
# So i store texts and titles here to avoid mess in main code.

# We have 4 type of welcome messages
# First 2 is normal and second 2 is for deep-linking
# User is new (/start):
welcome_1: str = (
    "مرحبا {}\n\n"
    "مرحبا بك في بوت جان جي بي تي!\n"
)
# User already have account (/start):
welcome_2: str = (
    "مرحبا بك مرة اخرى {}\n"
    "لنبدأ محادثتنا!"
)
# User is new (/start=create):
welcome_3: str = (
    "مرحبا {}\n"
    "تم عمل حسابك استمتع"
)
# User already have account (/start?create):
welcome_4: str = (
    "مرحبا {}\n"
    "انت لديك حساب."
)

# No account prompt for users with no accounts:
no_account_warn: str = (
    "عزيزي {}\n\n"
    "تحتاج لبدأ البوت قبل استخدامه! "
    "تحتاج لصنع حساب لنفسك بالبداية:\n\n"
    "t.me/{}?start=create"
)

# History cleared prompt:
history_cleared: str = (
    "عزيزي {}\n\n"
    "تم حذف دردشاتك بنجاح."
)

# Dan mode prompts for /danmode command
# Dan mode enabled:
dan_mode_enabled: str = (
    "مود الدي اي ان تفعل لكن احذر اصداره قديم\n"
    "Status: *مفعل*"
)
# Dan mode disabled:
dan_mode_disabled: str = (
    "DAN mode _version 10.0!_\n"
    "Status: *Disabled*\n\n"
    "Note: History file also reset!"
)

# Help prompt for (/help) command:
help_message: str = (
    "*List of global commands*:\n"
    "1. /start: Start bot\n"
    "2. /ping: Ping the Providers\n\n"
    "*List of chat related commands*:\n"
    "1. /reset: Reset chat history\n"
    "2. /history: Get chat history\n"
    "3. /chat: Chat in groups\n"
    "4. /tts: Voice response\n"
    "4. /settings: Providers settings\n"
    "4. /danmode: Use DAN mode in GPT\n\n"
    "*Other commands*:\n"
    "1. /features: See feature changes\n\n"
    "*Inline usage* (copy):\n"
    "`@{} roles`\n"
    "this will show all available roles.\n"
)

# Features prompt for (/features) command
features: str = (
    "*Main features*:\n"
    "1. يشمل الذاكرة طويلة المدى\n"
    "2. يتضمن الأدوار ووضع DAN\n"
    "3. يدعم المجموعات و المحادثات\n"
    "4. يدعم خاصية اعادة التوليد\n"
    "5. استجابة صوتية اصدار (بيتا)\n\n"
    "*Other features*:\n"
    "1. MarkdownV2 escaper\n"
    "2. مدقق التاريخ والمثبت\n\n"
    "*الميزات القادمة*:\n"
    "1. خيار الرد الذكي\n"
    "2. مولد اكواد برمجية\n"
    "3. مولد الصور\n"
    "5. لغات متعددة\n\n"
    "يرجى ارسال اي خطأ ممكن يحدث في البوت لحسابي:\n"
    "@x8_9n\n\n"
    "*التغييرات الاخيرة*:\n"
    "# تمت إضافة المزيد من مقدمي الخدمات.\n"
    "# تم اضافة ذكاء اصطناعي مدموج."
)

# Usage help for (/chat) command:
chat_help: str = (
    "Hi {}\n"
    "يرجى كتابة سؤالك بعد امر /chat\n\n"
    "*مثال*: /chat مرحبا"
)

# Usage for (/tts) command:
tts_help: str = (
    "مرحبا {}\n"
    "يرجى ارسال سؤالك بعد /tts\n\n"
    "*مثال*: /tts hi"
)

# Response prompt:
response_prompt: str = (
    "جارٍ إنشاء الاستجابة... الرجاء الانتظار"
)

# Response prompt:
tts_response_prompt: str = (
    "جارٍ إنشاء استجابة صوتية... الرجاء الانتظار. (قد يستغرق الأمر ما يصل إلى دقيقة!)"
)

# GPT response error:
response_error: str = (
    "خطأ!\n"
    "ChatGPT لا يتم الاتصال به حاليا!"
)

# Settings prompt
settings_prompt: str = (
    "مقدمي الخدمة الخاصين بك:\n"
    "يمكنك تمكينها/تعطيلها من خلال النقر عليها."
)
