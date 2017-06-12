def new():
    """
    :return: a new preview collection.
    :param : (type: bpy.utils.previews.ImagePreviewCollection)
    :rtype: ImagePreviewCollection
    """


def remove(pcoll):
    """Remove the specified previews collection.
    
    :param pcoll: Preview collection to close.
        (type: bpy.utils.previews.ImagePreviewCollection)
    :type pcoll: ImagePreviewCollection
    """


class ImagePreviewCollection:
    """Dictionary-like class of previews.
    This is a subclass of Python's built-in dict type,
                            used to store multiple image previews.
    <Note> - instance with bpy.utils.previews.new
        - keys must be str type.
        - values will be bpy.types.ImagePreview
    """

    def clear(self):
        """Clear all previews."""

    def close(self):
        """Close the collection and clear all previews."""

    def load(self, name, filepath, filetype, force_reload=False):
        """Generate a new preview from given file path, or return existing one matching name.
        
        :param name: The name (unique id) identifying the preview.
        :type name: str
        :param filepath: The file path to generate the preview from.
        :type filepath: str
        :param filetype: The type of file, needed to generate the preview in ['IMAGE', 'MOVIE', 'BLEND', 'FONT'].
        :type filetype: str
        :param force_reload: If True, force running thumbnail manager even if preview already exists in cache.
        :type force_reload: bool
        :return: The Preview matching given name, or a new empty one.
        :rtype: bpy.types.ImagePreview
        """

    def new(self, name):
        """Generate a new empty preview, or return existing one matching name.
        
        :param name: The name (unique id) identifying the preview.
        :type name: str
        :return: The Preview matching given name, or a new empty one.
        :rtype: bpy.types.ImagePreview
        """
