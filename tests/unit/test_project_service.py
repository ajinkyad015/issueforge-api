import pytest


from app.schemas.project import ProjectCreate
from app.services.project import ProjectService
from app.exceptions.project import ProjectSlugAlreadyExistsError

@pytest.mark.asyncio
async def test_create_project_success(service: ProjectService):
    # Arrange
    project = ProjectCreate(
        name="IssueForge",
        slug="issueforge",
        description="Issue tracking platform",
    )

    # Act
    created = await service.create_project(project)
    projects = await service.list_projects()

    # Assert repository state
    assert len(projects) == 1
    assert projects[0].slug == "issueforge"

    # Assert returned object
    assert created.id is not None
    assert created.name == "IssueForge"
    assert created.slug == "issueforge"
    assert created.description == "Issue tracking platform"



@pytest.mark.asyncio
async def test_create_project_duplicate_slug(service: ProjectService):
    project = ProjectCreate(
        name="IssueForge",
        slug="issueforge",
        description="First project",
    )

    await service.create_project(project)

    duplicate = ProjectCreate(
        name="Another Project",
        slug="issueforge",
        description="Duplicate slug",
    )

    with pytest.raises(ProjectSlugAlreadyExistsError) as exc_info:
        await service.create_project(duplicate)

    assert "issueforge" in str(exc_info.value)