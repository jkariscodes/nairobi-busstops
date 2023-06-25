from .base import *
import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

ENVIRONMENT = "development"

SECRET_KEY = env("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(" ")

# Static files management using WhiteNoise
INSTALLED_APPS.insert(5, "whitenoise.runserver_nostatic")
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

# Database configuration
DATABASES = {
    "default": {
        "ENGINE": env("ENGINE"),
        "NAME": env("GIS_DB_NAME"),
        "USER": env("GIS_DB_USER"),
        "PASSWORD": env("GIS_DB_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
    }
}

# Static and Media files
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
WHITENOISE_USE_FINDERS = True
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "mediafiles"
