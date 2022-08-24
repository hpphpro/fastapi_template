import os

from .base import Settings

module = os.environ.get('SETTINGS_MODULE')

match module:
    case 'development':
        from .development import Settings as AdditionalSettings
    case 'production':
        from .production import Settings as AdditionalSettings
    case 'test':
        from .test import Settings as AdditionalSettings
    case _:
        raise TypeError('SETTINGS_MODULE is required')
    
settings = Settings(_env_file=AdditionalSettings.Config.env_file, module=AdditionalSettings)