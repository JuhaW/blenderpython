# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    'name': 'Emulate Numpad',
    'author': 'chromoly',
    'version': (0, 2, 1),
    'blender': (2, 78, 0),
    'location': 'Screen > Space',
    'description': 'Space + any key -> Numpad key',
    'warning': '',
    'wiki_url': '',
    'tracker_url': '',
    'category': 'User Interface',
}

"""
単独動作不可。listvalidkeysに依存する。
Spaceキーの分はTABキーとの組み合わせで実行できる。(初期設定)
"""


import importlib
import traceback
import ctypes as ct

import bpy

try:
    importlib.reload(listvalidkeys)
    importlib.reload(addongroup)
    importlib.reload(registerinfo)
    importlib.reload(st)
except NameError:
    from .. import listvalidkeys
    from ..utils import addongroup
    from ..utils import registerinfo
    from ..utils import structures as st


keypad = {
    'TYPE1': [
        ('kp0', 'V', 'NUMPAD_0', '0'),
        ('kp1', 'Z', 'NUMPAD_1', '1'),
        ('kp2', 'X', 'NUMPAD_2', '2'),
        ('kp3', 'C', 'NUMPAD_3', '3'),
        ('kp4', 'A', 'NUMPAD_4', '4'),
        ('kp5', 'S', 'NUMPAD_5', '5'),
        ('kp6', 'D', 'NUMPAD_6', '6'),
        ('kp7', 'Q', 'NUMPAD_7', '7'),
        ('kp8', 'W', 'NUMPAD_8', '8'),
        ('kp9', 'E', 'NUMPAD_9', '9'),
        ('kpdl', 'B', 'NUMPAD_PERIOD', '.'),
        ('kpad', 'F', 'NUMPAD_PLUS', '+'),
        ('kpsu', 'R', 'NUMPAD_MINUS', '-'),
        ('kpmu', 'G', 'NUMPAD_ASTERIX', '*'),
        ('kpdv', 'T', 'NUMPAD_SLASH', '/'),
        ('kpen', 'N', 'NUMPAD_ENTER', 'Enter'),
        ('space', 'TAB', 'SPACE', 'Space'),
    ],
    'TYPE2': [
        ('kp0', 'Z', 'NUMPAD_0', '0'),
        ('kp1', 'A', 'NUMPAD_1', '1'),
        ('kp2', 'S', 'NUMPAD_2', '2'),
        ('kp3', 'D', 'NUMPAD_3', '3'),
        ('kp4', 'Q', 'NUMPAD_4', '4'),
        ('kp5', 'W', 'NUMPAD_5', '5'),
        ('kp6', 'E', 'NUMPAD_6', '6'),
        ('kp7', 'ONE', 'NUMPAD_7', '7'),
        ('kp8', 'TWO', 'NUMPAD_8', '8'),
        ('kp9', 'THREE', 'NUMPAD_9', '9'),
        ('kpdl', 'C', 'NUMPAD_PERIOD', '.'),
        ('kpad', 'V', 'NUMPAD_PLUS', '+'),
        ('kpsu', 'F', 'NUMPAD_MINUS', '-'),
        ('kpmu', 'R', 'NUMPAD_ASTERIX', '*'),
        ('kpdv', 'FOUR', 'NUMPAD_SLASH', '/'),
        ('kpen', 'B', 'NUMPAD_ENTER', 'Enter'),
        ('space', 'TAB', 'SPACE', 'Space'),
    ],
    'TYPE3': [
        ('kp0', 'Z', 'NUMPAD_0', '0'),
        ('kp1', 'X', 'NUMPAD_1', '1'),
        ('kp2', 'C', 'NUMPAD_2', '2'),
        ('kp3', 'V', 'NUMPAD_3', '3'),
        ('kp4', 'S', 'NUMPAD_4', '4'),
        ('kp5', 'D', 'NUMPAD_5', '5'),
        ('kp6', 'F', 'NUMPAD_6', '6'),
        ('kp7', 'W', 'NUMPAD_7', '7'),
        ('kp8', 'E', 'NUMPAD_8', '8'),
        ('kp9', 'R', 'NUMPAD_9', '9'),
        ('kpdl', 'A', 'NUMPAD_PERIOD', '.'),
        ('kpad', 'G', 'NUMPAD_PLUS', '+'),
        ('kpsu', 'T', 'NUMPAD_MINUS', '-'),
        ('kpmu', 'FOUR', 'NUMPAD_ASTERIX', '*'),
        ('kpdv', 'THREE', 'NUMPAD_SLASH', '/'),
        ('kpen', 'B', 'NUMPAD_ENTER', 'Enter'),
        ('space', 'TAB', 'SPACE', 'Space'),
    ]
}

name_space = \
    {attr: bpy.props.StringProperty(
        name=name, description=type_, default=default)
     for attr, default, type_, name in keypad['TYPE1']}


def keybind_update(self, context):
    for attr, rcv, snd, name in keypad[self.keybind_preset]:
        setattr(self, attr, rcv)


name_space['keybind_preset'] = bpy.props.EnumProperty(
    name='Keybind',
    items=(('TYPE1', 'Type1', ''),
           ('TYPE2', 'Type2', ''),
           ('TYPE3', 'Type3', '')),
    update=keybind_update,
)
KeyPad = type('KeyPad', (), name_space)


class EmulateNumpadPreferences(
        addongroup.AddonGroupPreferences,
        registerinfo.AddonRegisterInfo,
        KeyPad,
        bpy.types.PropertyGroup if '.' in __name__ else
        bpy.types.AddonPreferences):
    bl_idname = __name__

    def draw(self, context):
        layout = self.layout

        sp = layout.split(0.3)
        row = sp.row()
        row.prop(self, 'keybind_preset', text='Preset')
        row = sp.row()
        row.alignment = 'RIGHT'
        op = row.operator('wm.url_open', text='Valid Strings', icon='URL')
        op.url = 'https://www.blender.org/api/' \
                 'blender_python_api_2_78a_release/bpy.types.Event.html' \
                 '#bpy.types.Event.type'

        def draw_column(layout, attrs):
            column = layout.column()
            for attr in attrs:
                prop_row = column.row()
                if attr:
                    s = prop_row.split(0.3)
                    sub_row = s.row()
                    sub_row.label(self.bl_rna.properties[attr].name)
                    sub_row = s.row()
                    sub_row.prop(self, attr, text='')
                else:
                    prop_row.label()

        row = layout.box().row()
        draw_column(row.column(), [None, 'kp7', 'kp4', 'kp1', 'kp0'])
        draw_column(row.column(), ['kpdv', 'kp8', 'kp5', 'kp2', None])
        draw_column(row.column(), ['kpmu', 'kp9', 'kp6', 'kp3', 'kpdl'])
        draw_column(row.column(), [None, 'kpsu', 'kpad', 'kpen', 'space'])

        self.layout.separator()
        super().draw(context)


def find_event_keymap_items(context, event_attrs, keymaps):
    keymap_items = []

    event_attrs = {
        'type': 'NONE',
        'value': 'ANY',
        'any': False,
        'shift': False,
        'ctrl': False,
        'alt': False,
        'oskey': False,
        'key_modifier': 'NONE',
        **event_attrs
    }

    for km in keymaps:
        for kmi in km.keymap_items:
            if not kmi.active:
                # if (km, kmi) not in disabled_keymap_items:
                continue
            if kmi.idname == SCREEN_OT_emulate_numpad.bl_idname:
                continue

            select_mouse = context.user_preferences.inputs.select_mouse
            if select_mouse == 'RIGHT':
                action_select = {'ACTIONMOUSE': 'LEFTMOUSE',
                     'SELECTMOUSE': 'RIGHTMOUSE',
                     'EVT_TWEAK_A': 'EVT_TWEAK_L',
                     'EVT_TWEAK_S': 'EVT_TWEAK_R',
                     }
            else:
                action_select = {'ACTIONMOUSE': 'RIGHTMOUSE',
                     'SELECTMOUSE': 'LEFTMOUSE',
                     'EVT_TWEAK_A': 'EVT_TWEAK_R',
                     'EVT_TWEAK_S': 'EVT_TWEAK_L',
                     }
            if (kmi.type == event_attrs['type'] or
                    kmi.type in action_select and
                    action_select[kmi.type] == event_attrs['type']):
                if kmi.value == event_attrs['value'] or kmi.value == 'ANY':
                    if kmi.any:
                        match = True
                    else:
                        mods = ['shift', 'ctrl', 'alt', 'oskey']
                        match = all([getattr(kmi, m) == event_attrs[m]
                                     for m in mods])
                    if kmi.key_modifier != 'NONE':
                        if kmi.key_modifier != event_attrs['key_modifier']:
                            match = False
                    if match:
                        keymap_items.append(kmi)
    return keymap_items


def get_operator_from_keymap_item(kmi):
    kwargs = {}
    try:
        m, f = kmi.idname.split('.')
        type_name = m.upper() + '_OT_' + f
        if not hasattr(bpy.types, type_name):
            return None, kwargs

        op = getattr(getattr(bpy.ops, m), f)
        for attr in kmi.properties.keys():
            if kmi.properties.is_property_set(attr):
                # NOTE: enumの場合、kmi.properties[attr]とすると
                #       intが返ってくる
                kwargs[attr] = getattr(kmi.properties, attr)
        return op, kwargs
    except:
        traceback.print_exc()
        return None, kwargs


def operator_call(context, event_attrs, keymaps):
    """イベントに一致するオペレーターを実行する。"""
    called = False
    pass_through = False
    running_modal = False
    interface = False

    for kmi in find_event_keymap_items(context, event_attrs, keymaps):
        op, kwargs = get_operator_from_keymap_item(kmi)
        if not op:
            continue

        if op.poll():
            called = True
            try:
                r = op('INVOKE_DEFAULT', **kwargs)
            except:
                traceback.print_exc()
                return called, running_modal, False
            pass_through = 'PASS_THROUGH' in r
            if 'RUNNING_MODAL' in r:
                running_modal = True
            if 'INTERFACE' in r:
                interface = True
            if not pass_through:
                return called, running_modal, pass_through, interface

    return called, running_modal, pass_through, interface


def get_active_area_region(context, event):
    """マウスカーソル位置のAreaとRegionを取得する。
    :type context: bpy.types.Context
    :type event: bpy.types.Event
    :rtype: (bpy.types.Area, bpy.types.Region)
    """
    x, y = event.mouse_x, event.mouse_y
    for area in context.screen.areas:
        if area.x <= x < area.x + area.width:
            if area.y <= y < area.y + area.height:
                for region in area.regions:
                    if region.x <= x < region.x + region.width:
                        if region.y <= y < region.y + region.height:
                            return area, region
    return None, None


def find_window_form_region(region):
    for wm in bpy.data.window_managers:
        for window in wm.windows:
            for area in window.screen.areas:
                for region_ in area.regions:
                    if region_ == region:
                        return window


def set_active_area_region(context, area, region):
    """ContextのAreaとRegionを設定する。py_contextを無効化した状態で処理をする。
    返り値は変更前のAreaとRegion。これは bContext.wm.area,
    bContext.wm.region に当たるもの。
    :type context: bpy.types.Context
    :type area: bpy.types.Area
    :type region: bpy.types.Region
    :rtype: (bpy.types.Area, bpy.types.Region)
    """
    py_dict_bak = st.context_py_dict_set(context, None)
    area_bak = context.area  # bContext.wm.area
    region_bak = context.region  # bContext.wm.region

    ctx_p = ct.cast(context.as_pointer(), ct.POINTER(st.bContext))
    ctx = ctx_p.contents
    if area:
        # CTX_wm_area_set()
        ctx.wm.area = ct.cast(area.as_pointer(), ct.POINTER(st.ScrArea))
        # ctx.wm.region = None
    else:
        ctx.wm.area = None
    if region:
        # CTX_wm_region_set()
        ctx.wm.region = ct.cast(region.as_pointer(), ct.POINTER(st.ARegion))
    else:
        ctx.wm.region = None

    if region:
        window = find_window_form_region(region)
        if window:
            win_p = ct.cast(window.as_pointer(), ct.POINTER(st.wmWindow))
        else:
            win_p = ctx.wm.window  # context.window
        if win_p:
            win = win_p.contents
            event = win.eventstate.contents
            event.mval[0] = event.x - region.x
            event.mval[1] = event.y - region.y

    st.context_py_dict_set(context, py_dict_bak)
    return area_bak, region_bak


class SCREEN_OT_emulate_numpad(bpy.types.Operator):
    bl_idname = 'screen.emulate_numpad'
    bl_label = 'Emulate Numpad'
    bl_options = {'REGISTER'}

    def __init__(self):
        self.event_type = ''
        self.finish = False

    def modal(self, context, event):
        prefs = EmulateNumpadPreferences.get_instance()
        ret = {'RUNNING_MODAL'}

        event_attributes = {
            attr: getattr(event, attr)
            for attr in ['type', 'value', 'shift', 'ctrl', 'alt', 'oskey']}
        # event.key_modifierに当たるものはpythonAPIでは提供されていない
        ev = ct.cast(ct.c_void_p(event.as_pointer()),
                     ct.POINTER(st.wmEvent)).contents
        value = ev.keymodifier
        prop = bpy.types.KeyMapItem.bl_rna.properties['key_modifier']
        for enum_item in prop.enum_items:
            if enum_item.value == value:
                event_attributes['key_modifier'] = enum_item.identifier
                break

        if self.finish:
            ret = {'FINISHED'}

        elif event.type == self.event_type and event.value == 'RELEASE':
            ret = {'FINISHED'}

        elif event.type == 'ESC':
            ret = {'FINISHED'}

        else:
            # area, regionと有効なキーマップの更新
            area, region = get_active_area_region(context, event)
            set_active_area_region(context, area, region)
            self.keymaps = [km for km in listvalidkeys.context_keymaps(context)
                            if listvalidkeys.keymap_poll(context, km)]

            match = False
            if event.value == 'PRESS':
                for attr, _, kmi_type, _ in keypad['TYPE1']:
                    if event.type == getattr(prefs, attr):
                        match = True
                        break
            if match:
                event_attrs = {
                    **event_attributes, 'type': kmi_type, 'value': 'PRESS'}
                _called, running_modal, _pass_through, is_interface = \
                    operator_call(context, event_attrs, self.keymaps)
                if running_modal:
                    self.finish = True
                if is_interface:
                    ret = {'FINISHED'}

        if 'FINISHED' in ret:
            area = self.get_info_area(context)
            if area:
                area.header_text_set()

        return ret

    def get_info_area(self, context):
        for area in context.screen.areas:
            if area.type == 'INFO':
                return area

    def invoke(self, context, event):
        # CONSOLEとTEXT_EDITORではSpaceキーのみでの呼び出しは無視する。
        if context.area.type in {'CONSOLE', 'TEXT_EDITOR'}:
            if event.type == 'SPACE':
                if (not event.shift and not event.ctrl and not event.alt and
                        not event.oskey):
                    return {'CANCELLED', 'PASS_THROUGH'}

        self.event_type = event.type

        # これはmodal中にも更新する
        self.keymaps = [km for km in listvalidkeys.context_keymaps(context)
                        if listvalidkeys.keymap_poll(context, km)]

        context.window_manager.modal_handler_add(self)

        area = self.get_info_area(context)
        if area:
            area.header_text_set('Emulate Numpad')

        return {'RUNNING_MODAL'}


classes = [
    SCREEN_OT_emulate_numpad,
    EmulateNumpadPreferences,
]


@EmulateNumpadPreferences.register_addon
def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = EmulateNumpadPreferences.get_keymap('Screen Editing')
        kmi = km.keymap_items.new(
            'screen.emulate_numpad', 'SPACE', 'PRESS', head=True)


@EmulateNumpadPreferences.unregister_addon
def unregister():
    for cls in classes[::-1]:
        bpy.utils.unregister_class(cls)


if __name__ == '__main__':
    register()
