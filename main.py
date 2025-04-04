import os
import uvicorn
import asyncpg
from fastapi import FastAPI
from datetime import datetime
from fastapi.responses import HTMLResponse



##python -m uvicorn main:app --reload

app = FastAPI()

@app.get(path="/")
async def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HTMLResponse(content=f"""
<body>
<div style="width: 400px; margin: 50 auto;">
    <h1> 천준영님 환영합니다</h1>
    <h2>{current_time}</h2>
</div>
</body>
""")

@app.get("/crawl/result")
async def get_crawl_result():
    conn = await asyncpg.connect(
        user='myuser',
        password='mypassword',
        database='mydatabase',
        host='hc_postgres',
        port=5432
    )
    rows = await conn.fetch("SELECT * FROM crawl_results ORDER BY id DESC LIMIT 10")
    await conn.close()
    return [{"id": r["id"], "message": r["message"]} for r in rows]

if __name__ == "__main__":

    port = int(os.getenv("PORT", 8000))  # Railway가 PORT 주입함. 없으면 기본값 8000
    uvicorn.run("main:app", host="0.0.0.0", port=port)
