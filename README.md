# Telegram Support Bot / بات پشتیبانی تلگرام

> ⚠️ **Note / توجه:** This is a test/educational project created for university coursework purposes. It is not intended for production use.
> این پروژه صرفاً یک نمونه‌ی آزمایشی و آموزشی است که برای تمرین دانشگاهی نوشته شده و برای استفاده در محیط واقعی (Production) مناسب نیست.

---

## English

### Overview
A simple Telegram bot built with [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) (`telebot`) that provides basic customer-support style interactions in Persian. Users can either:
- Request direct contact information (phone numbers)
- Submit a problem/ticket and receive a randomly generated tracking number.

### Features
- `/start` command shows a custom reply keyboard with two options.
- **"ارتباط مستقیم با ما" (Contact us directly)** — sends support phone numbers.
- **"ثبت مشکل" (Report a problem)** — asks the user to describe their issue, then replies with a randomly generated 5-digit ticket number.

### Requirements
- Python 3.8+
- `pyTelegramBotAPI`

Install dependencies:
```bash
pip install pyTelegramBotAPI
```

### Setup
1. Create a bot via [@BotFather](https://t.me/BotFather) on Telegram and obtain an API token.
2. Set the token as an environment variable:
   ```bash
   export API_TOKEN="your-telegram-bot-token"
   ```
3. Run the bot:
   ```bash
   python main.py
   ```

### Known Limitations (worth mentioning as it's a course project)
- Ticket numbers are generated randomly and **not stored anywhere** — there is no database, so tickets/tracking numbers are lost on restart and can't actually be looked up later.
- No persistence layer for submitted problems (no file/database logging).
- Support phone numbers in the code are placeholders (`0912*******`, `021********`) and should be replaced with real numbers.
- No error handling around missing `API_TOKEN` or network/polling failures.
- Uses `infinity_polling()`, which is fine for learning/demo purposes but not ideal for production (webhook-based deployment would be more robust and scalable).

### License
This is a course/academic exercise; use freely for learning purposes.

---

## فارسی

### معرفی پروژه
این یک بات ساده‌ی تلگرامی است که با کتابخانه‌ی [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) (`telebot`) نوشته شده و نوعی تعامل ساده‌ی پشتیبانی مشتری به زبان فارسی را فراهم می‌کند. کاربر می‌تواند:
- اطلاعات تماس مستقیم (شماره تلفن‌ها) را درخواست کند .
- مشکل خود را ثبت کرده و یک شماره پیگیری تصادفی دریافت کند.

### امکانات
- دستور `/start` یک کیبورد پاسخ سفارشی با دو گزینه نمایش می‌دهد.
- **«ارتباط مستقیم با ما»** — شماره‌های تماس پشتیبانی را ارسال می‌کند.
- **«ثبت مشکل»** — از کاربر می‌خواهد مشکل خود را بنویسد و سپس یک شماره تیکت ۵ رقمی تصادفی برمی‌گرداند.

### پیش‌نیازها
- پایتون نسخه ۳.۸ به بالا
- کتابخانه‌ی `pyTelegramBotAPI`

نصب وابستگی‌ها:
```bash
pip install pyTelegramBotAPI
```

### راه‌اندازی
۱. از طریق [@BotFather](https://t.me/BotFather) در تلگرام یک بات بسازید و توکن API آن را دریافت کنید.
۲. توکن را به‌صورت متغیر محیطی تنظیم کنید:
   ```bash
   export API_TOKEN="توکن-بات-شما"
   ```
۳. بات را اجرا کنید:
   ```bash
   python main.py
   ```

### مجوز
این پروژه یک تمرین درسی/دانشگاهی است و برای اهداف یادگیری آزادانه قابل استفاده است.