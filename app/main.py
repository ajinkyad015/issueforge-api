from fastapi import FastAPI


app = FastAPI(
    title="IssueForge API",
    description="A production-style issue tracking REST API.",
    version="0.1.0",
)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "IssueForge API is running"}