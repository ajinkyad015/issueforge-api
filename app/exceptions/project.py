class ProjectSlugAlreadyExistsError(Exception):
    def __init__(self, slug: str) -> None:
        self.slug = slug
        super().__init__(f"Project with slug '{slug}' already exists")