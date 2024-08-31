from helpers.copier import finish_task
from helpers.git import ensure_git
from helpers.venv import ensure_project_venv

if __name__ == "__main__":
    try:
        ensure_git()
        venv = ensure_project_venv()
    except Exception as err:  # pylint: disable=broad-except
        finish_task(
            f"Failed initializing environment: {err}",
            False,
            extra=(
                "No worries, just follow the manual steps documented here: "
                "https://salt-extensions.github.io/salt-extension-copier/topics/creation.html#first-steps"
            ),
        )
    finish_task("Successfully initialized environment", True)
