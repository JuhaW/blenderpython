bl_info = {
    "name": "Menu Base",
    "description": "Test",
    "category": "User Interface"
}


from types import MethodType

import bpy


items = [{"label": "Item " + str(i)} for i in range(8)]
item = items[0]
# item["label"] = "AAAAA"
# item["description"] = "Delete"
# item["icon"] = 'BLENDER'
# item["execute"] = "print('HOOOOOOO')"
# item = items[1]
# item["label"] = "Translate"
# item["execute"] = "transform.translate"


items[0]["icon"] = "BLENDER"
items[0]["description"] = "テスト"
items[0]["execute"] = "print('Blender')"
for i, item in enumerate(items):
    item["shortcut"] = chr(ord("A") + i)

shift_items = [{"label": "Shift " + str(i)} for i in range(8)]
p = "/home/sui/.config/blender/2.78/scripts/addons/ctools/piemenu/{}.jpg"
for i, item in enumerate(shift_items):
    item["icon"] = p.format(i + 1)


class TempMenu:
    keymap_items = [["3D View", {"type": 'ONE', "value": 'PRESS', "alt": True}]]

    idname = "hoge"
    label = "(　ﾟ∀ﾟ)o彡ﾟ"
    items = items
    shift_items = shift_items
    draw_type = "box"
    icon_scale = 1
    icon_expand = 0.0
    radius = 40
    center_type = "last"  # "last", "fixed"
    center_index = 5  # for "fixed"
    quick_action = False


##########################################
def get_enum_items(obj, prop_name):
    prop = obj.bl_rna.properties[prop_name]
    return list(prop.enum_items)


class Empty:
    pass


pie_menus = [
    TempMenu,
]


keymap_items = []


def register(addon_preferences):
    for menu in pie_menus:
        if hasattr(menu, "keymap_items"):
            for km_name, kwargs in menu.keymap_items:
                km = addon_preferences.get_keymap(km_name)
                if km:
                    kmi = km.keymap_items.new("wm.pie_menu", **kwargs)
                    kmi.properties.menu = menu.idname
                    keymap_items.append((km, kmi))
    return pie_menus


def unregister(addon_preferences):
    for km, kmi in keymap_items:
        km.keymap_items.remove(kmi)
    keymap_items.clear()
    return pie_menus
