from .base import *
import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

ENVIRONMENT = "production"

SECRET_KEY = env("SECRET_KEY")

DEBUG = False

ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(" ")

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

# Static files configuration
USE_WHITENOISE = env("USE_WHITENOISE")
if USE_WHITENOISE:
    # Static file management using WhiteNoise in production
    INSTALLED_APPS.insert(5, "whitenoise.runserver_nostatic")
    MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
    STATIC_URL = "/static/"
    STATIC_ROOT = BASE_DIR / "static"
    STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
    # User uploaded content
    MEDIA_URL = "/media/"
    MEDIA_ROOT = BASE_DIR / "mediafiles"
USE_S3 = env("USE_S3")
if USE_S3:
    INSTALLED_APPS.extend(["storages"])
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_CUSTOM_DOMAIN = os.environ.get("AWS_S3_CUSTOM_DOMAIN")
    AWS_LOCATION = os.environ.get("AWS_S3_CUSTOM_DOMAIN")
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    DEFAULT_FILE_STORAGE = "PersonalWebsite.storage_backends.MediaStorage"
    STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]
USE_CLOUDINARY = env("USE_CLOUDINARY")
if USE_CLOUDINARY:
    INSTALLED_APPS.insert(5, "cloudinary_storage")
    INSTALLED_APPS.insert(7, "cloudinary")
    CLOUDINARY_STORAGE = {
        "CLOUD_NAME": env("CLOUDINARY_CLOUD_NAME"),
        "API_KEY": env("CLOUDINARY_API_KEY"),
        "API_SECRET": env("CLOUDINARY_API_SECRET"),
        "SECURE": True,
        "STATIC_IMAGES_EXTENSIONS": [
            "jpg",
            "jpe",
            "jpeg",
            "jpc",
            "jp2",
            "j2k",
            "wdp",
            "jxr",
            "hdp",
            "png",
            "gif",
            "webp",
            "bmp",
            "tif",
            "tiff",
            "ico",
        ],
    }
    CLOUDINARY_URL = env("CLOUDINARY_URL")
    STATICFILES_STORAGE = "cloudinary_storage.storage.StaticHashedCloudinaryStorage"
    DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
    STATIC_URL = "static/"
    MEDIA_URL = "/media/"
    STATIC_ROOT = BASE_DIR / "staticfiles"
    MEDIA_ROOT = BASE_DIR / "mediafiles"


# SSL Settings
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
