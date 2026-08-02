class Media:
    def __init__(self, title, media_type, status, rating, notes):
        self.title = title
        self.media_type = media_type
        self.status = status
        self.rating = rating
        self.notes =notes
    def __str__(self):
        return f"{self.title} ({self.media_type}) - {self.status}"