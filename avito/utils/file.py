def abs_path_from_project(relative_path: str):
    import avito
    from pathlib import Path

    return (
        Path(avito.__file__)
        .parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )