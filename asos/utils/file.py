def abs_path_from_project(relative_path: str):
    import asos
    from pathlib import Path

    return (
        Path(asos.__file__)
        .parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )