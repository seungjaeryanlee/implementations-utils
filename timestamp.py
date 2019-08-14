"""Timestamp-related functions for discerning runs."""
from datetime import datetime


def get_timestamp(timestamp_format="%Y%m%d_%H%M%S"):
    """Return timestamp with the given format."""
    return datetime.now().strftime(timestamp_format)
