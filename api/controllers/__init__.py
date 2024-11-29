import importlib
import pkgutil
from fastapi import FastAPI

def register_controllers(app: FastAPI):
    package = __package__
    for _, module_name, _ in pkgutil.iter_modules(__path__):
        module = importlib.import_module(f"{package}.{module_name}")
        if hasattr(module, "router"):
            app.include_router(module.router, prefix="/api")
