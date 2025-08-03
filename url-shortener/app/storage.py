import threading
from datetime import datetime, timezone
from typing import Dict, Any, Optional

class URLStore:
    """
    A thread-safe in-memory storage for URL mappings.
    """
    def __init__(self):
        # The main data store.
        # Format: { "short_code": { "original_url": str, "created_at": datetime, "clicks": int } }
        self._urls: Dict[str, Dict[str, Any]] = {}
        # A lock to ensure atomic operations on the dictionary
        self._lock = threading.Lock()

    def save_url(self, short_code: str, original_url: str) -> bool:
        """
        Saves a new URL mapping. Returns False if the short_code already exists.
        """
        with self._lock:
            if short_code in self._urls:
                return False
            self._urls[short_code] = {
                "original_url": original_url,
                "created_at": datetime.now(timezone.utc),
                "clicks": 0
            }
            return True

    def get_url(self, short_code: str) -> Optional[str]:
        """
        Retrieves the original URL for a short code, returning None if not found.
        """
        with self._lock:
            return self._urls.get(short_code, {}).get("original_url")

    def increment_click_count(self, short_code: str):
        """
        Increments the click count for a short code.
        """
        with self._lock:
            if short_code in self._urls:
                self._urls[short_code]["clicks"] += 1

    def get_stats(self, short_code: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves the statistics for a short code.
        """
        with self._lock:
            # Return a copy to prevent external modification of the stored data
            return self._urls.get(short_code, None)