def eval_env_as_bool(value: str):
    return str(value).lower() in ("true", "t", "yes", "y", "1")
