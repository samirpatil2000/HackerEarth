import enum

class URLS(str, enum.Enum):
    IMAGE_LIST = "images"
    IMAGE_DETAILS = "image-details"
    NEW_IMAGE = "image-new"
    UPDATE_IMAGE = "image-update"
    DELETE_IMAGE = "image-delete"