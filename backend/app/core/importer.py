import importlib
from typing import List

from fastapi import APIRouter


class ImportUrlError(Exception):
    pass


def importer(import_str: str):
    if not isinstance(import_str, str):
        # return import_str
        raise ImportError(f'can not import {import_str}')
    try:
        module = importlib.import_module(import_str)
    except ImportError as exc:
        if exc.name != import_str:
            raise exc from None
        msg = f'Could not import module "{import_str}".'
        raise ImportUrlError(msg)

    instance = module
    if not hasattr(instance, 'path'):
        msg = f'{import_str} has no attribute path please check it again.'
        raise ImportUrlError(msg)
    return instance


def import_path(app_name: str):
    import_str = app_name + '.urls'
    instance = importer(import_str)
    path = getattr(instance, 'path')
    if not isinstance(path, APIRouter):
        msg = f'{import_str} is not APIRouter class please check it again.'
        raise ImportUrlError(msg)
    return path


def import_models(app_name: str):
    importer(app_name + 'models')
