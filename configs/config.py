# configs/config.py
import os

class Config:
    STABILITY_HOST = os.environ.get('STABILITY_HOST', 'grpc.stability.ai:443')
    STABILITY_KEY = os.environ.get('STABILITY_KEY', 'key-goes-here')

