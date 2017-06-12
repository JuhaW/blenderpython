locale = None
"""The actual locale currently in use (will always return a void string when Blender is built without internationalization support)."""

locales = None
"""All locales currently known by Blender (i.e. available as translations)."""

contexts_C_to_py = None
"""A readonly dict mapping contexts' C-identifiers to their py-identifiers."""

contexts = None
"""constant value bpy.app.translations.contexts(default_real=None, default='*', operator_default='Operator', ui_events_keymaps='UI_Events_KeyMaps', plural='Plural', id_action='Action', id_armature='Armature', id_brush='Brush', id_camera='Camera', id_cachefile='CacheFile', id_curve='Curve', id_fs_linestyle='FreestyleLineStyle', id_gpencil='GPencil', id_group='Group', id_id='ID', id_image='Image', id_shapekey='Key', id_lamp='Lamp', id_library='Library', id_lattice='Lattice', id_mask='Mask', id_material='Material', ...)"""


def locale_explode(locale):
    """Return all components and their combinations  of the given ISO locale string.
    For non-complete locales, missing elements will be None.
    
    :param locale: The ISO locale string to explode.
    :return: A tuple (language, country, variant, language_country, language@variant).
    """


def pgettext(msgid, msgctxt):
    """Try to translate the given msgid (with optional msgctxt).
    <Note> The (msgid, msgctxt) parameters order has been switched compared to gettext function, to allow
                                    single-parameter calls (context then defaults to BLT_I18NCONTEXT_DEFAULT).
    <Note> You should really rarely need to use this function in regular addon code, as all translation should be
                                    handled by Blender internal code. The only exception are string containing formatting (like "File: %r"),
                                    but you should rather use bpy.app.translations.pgettext_iface/bpy.app.translations.pgettext_tip in those cases!
    <Note> Does nothing when Blender is built without internationalization support (hence always returns msgid).
    
    :param msgid: The string to translate.
    :type msgid: str
    :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
    :type msgctxt: str or None
    :return: The translated string (or msgid if no translation was found).
    """


def pgettext_data(msgid, msgctxt):
    """Try to translate the given msgid (with optional msgctxt), if new data name's translation is enabled.
    <Note> See bpy.app.translations.pgettext notes.
    
    :param msgid: The string to translate.
    :type msgid: str
    :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
    :type msgctxt: str or None
    :return: The translated string (or msgid if no translation was found).
    """


def pgettext_iface(msgid, msgctxt):
    """Try to translate the given msgid (with optional msgctxt), if labels' translation is enabled.
    <Note> See bpy.app.translations.pgettext notes.
    
    :param msgid: The string to translate.
    :type msgid: str
    :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
    :type msgctxt: str or None
    :return: The translated string (or msgid if no translation was found).
    """


def pgettext_tip(msgid, msgctxt):
    """Try to translate the given msgid (with optional msgctxt), if tooltips' translation is enabled.
    <Note> See bpy.app.translations.pgettext notes.
    
    :param msgid: The string to translate.
    :type msgid: str
    :param msgctxt: The translation context (defaults to BLT_I18NCONTEXT_DEFAULT).
    :type msgctxt: str or None
    :return: The translated string (or msgid if no translation was found).
    """


def register(module_name, translations_dict):
    """Registers an addon's UI translations.
    <Note> Does nothing when Blender is built without internationalization support.
    
    :param module_name: The name identifying the addon.
    :type module_name: str
    :param translations_dict: A dictionary built like that:
                                                    {locale: {msg_key: msg_translation, ...}, ...}
    :type translations_dict: dict
    """


def unregister(module_name):
    """Unregisters an addon's UI translations.
    <Note> Does nothing when Blender is built without internationalization support.
    
    :param module_name: The name identifying the addon.
    :type module_name: str
    """
