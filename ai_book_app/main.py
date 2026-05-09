import psycopg2
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os
import uuid

# আপনার তৈরি করা অন্য দুই ফাইল থেকে ফাংশন ইমপোর্ট করা হচ্ছে
from parser import extract_text
from ollama_service import ask_ollama

# ১. ডাটাবেজ কানেকশন এবং টেবিল তৈরি
def init_db():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="your password", # আপনার পাসওয়ার্ড নিশ্চিত করুন
            host="localhost"
        )
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS uploads 
                          (id SERIAL PRIMARY KEY, 
                           filename TEXT, 
                           summary TEXT)''')
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Database error: {e}")

init_db()

app = FastAPI()

# ২. CORS কনফিগারেশন
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "Welcome to AI Book Content Generator! Go to /docs to test."}

@app.post("/upload-book/")
async def upload_book(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    file_path = f"{UPLOAD_DIR}/{file_id}_{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text(file_path)
    text = text[:8000]

    # এআই প্রসেসিং
    script_prompt = f"Convert this book into a 10-minute YouTube video script:\n{text}"
    video_script = ask_ollama(script_prompt)

    shorts_prompt = f"Create 5 YouTube Shorts ideas:\n{text}"
    shorts = ask_ollama(shorts_prompt)

    summary_prompt = f"Summarize into 10 bullet points:\n{text}"
    summary = ask_ollama(summary_prompt)

    # ৩. PostgreSQL এ ডেটা সেভ করা (নতুন অংশ)
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="your_password", # আপনার পাসওয়ার্ড দিন
            host="localhost"
        )
        cursor = conn.cursor()
        cursor.execute("INSERT INTO uploads (filename, summary) VALUES (%s, %s)", (file.filename, summary))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Insert error: {e}")

    return {
        "video_script": video_script,
        "shorts_ideas": shorts,
        "summary": summary
    }