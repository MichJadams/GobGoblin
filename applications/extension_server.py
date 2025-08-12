import threading

from fastapi import FastAPI, APIRouter
import uvicorn
from typing import Dict, Any

from applications.database import Database

api = FastAPI()

class ExtensionServer(threading.Thread):
    def __init__(self, database: Database):
        super().__init__()

        self.router = APIRouter()
        self.router.add_api_route("/", self.post_application, methods=["POST"])
        self.config = uvicorn.Config(api, host="127.0.0.1", port=8000, log_level="info")
        self.server = uvicorn.Server(config=self.config)
        api.include_router(self.router)

        self.daemon = True
        self.should_stop = False
        self.database = database

    def is_running(self):
        return self.server.started

    def run(self):
        # Server is blocking, so we run it here
        print("server running?")
        self.server.run()

    def stop(self):
        self.server.should_exit = True  # Triggers server shutdown

    def post_application(self, payload: Dict[Any, Any]):
        # print(payload)
        self.database.add_application(
            title=payload.get("title", ""),
            company=payload.get("company", ""),
            requirements=payload.get("requirements", ""),
            url=payload.get("url", "")
        )
        return {"message": "Hello from FastAPI!"}
