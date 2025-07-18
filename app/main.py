# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth,user,wardrobe,style_tip

app = FastAPI(
    title="Smart Fit API",
    version="1.0.0",
    description="Backend for Smart Fit Outfit Suggestion App"
)

# CORS middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (adjust in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)  # Already has prefix="/auth" in the router
app.include_router(user.router)
app.include_router(wardrobe.router)
app.include_router(style_tip.router,prefix="/tips",tags=["Style Tips"])
