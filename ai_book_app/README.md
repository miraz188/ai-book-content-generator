# AI Book Content Generator

এটি একটি AI-পাওয়ারড প্রজেক্ট যা যেকোনো বই বা পিডিএফ (PDF) থেকে ইউটিউব ভিডিও স্ক্রিপ্ট, শর্টস আইডিয়া এবং সারাংশ (Summary) তৈরি করতে পারে।

## টেকনোলজি স্ট্যাক (Tech Stack)
- **Backend:** FastAPI (Python)
- **AI Engine:** Ollama (Local AI)
- **Model Used:** qwen3:0.6b (বা আপনি যেটা ব্যবহার করেছেন)
- **Frontend:** HTML, CSS (Tailwind), JavaScript

## কীভাবে রান করবেন (How to Run)
১. প্রথমে Ollama চালু করুন এবং মডেলটি ডাউনলোড করুন।
২. প্রয়োজনীয় লাইব্রেরি ইনস্টল করুন:
   `pip install fastapi uvicorn requests pypdf python-multipart`
৩. সার্ভার চালু করুন:
   `uvicorn main:app --reload`
৪. `index.html` ফাইলটি ব্রাউজারে ওপেন করুন।

## প্রজেক্ট ফিচার
- পিডিএফ এবং টেক্সট ফাইল আপলোড সাপোর্ট।
- ১০ মিনিটের ইউটিউব স্ক্রিপ্ট জেনারেশন।
- ৫টি ইউটিউব শর্টস আইডিয়া।
- ১০টি পয়েন্টে পুরো বইয়ের সামারি।