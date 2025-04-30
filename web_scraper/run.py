# run.py
import asyncio
import uvicorn

if asyncio.get_event_loop_policy().__class__.__name__ != "WindowsProactorEventLoopPolicy":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)