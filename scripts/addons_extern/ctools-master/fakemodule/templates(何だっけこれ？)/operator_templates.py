import bpy


class AddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__  # or __package__

    def draw(self, context):
        layout = self.layout


class OperatorBase(bpy.types.Operator):
    bl_idname = ''
    bl_label = ''
    bl_description = ''

    # Options for this operator type
    # REGISTER:    Register, Display in the info window and support the redo
    #              toolbar panel.
    # UNDO:        Undo, Push an undo event (needed for operator redo).
    # BLOCKING:    Blocking, Block anything else from using the cursor.
    # MACRO:       Macro, Use to check if an operator is a macro.
    # GRAB_CURSOR: Grab Pointer, Use so the operator grabs the mouse focus,
    #              enables wrapping when continuous grab is enabled.
    # PRESET:      Preset, Display a preset button with the operators settings.
    # INTERNAL:    Internal, Removes the operator from search results.
    bl_options = {'REGISTER', 'UNDO'}

    def __init__(self):
        pass

    def __del__(self):
        pass

    def get_property(self, attr):
        """return operator property
        :type attr: str
        :return: T
        """
        properties = self.rna_type.properties
        return properties[attr] if attr in properties else None

    def draw_property(self, attr, layout, text=None, skip_hidden=True,
                      row=False, **kwargs):
        """Draw operator property
        :type attr: str
        :type layout: bpy.types.UILayout
        :type text: str
        :type skip_hidden: bool
        :type row: bool
        """
        if attr == 'rna_type':
            return None
        prop = self.get_property(attr)

        if skip_hidden and prop.is_hidden:
            return None
        col = layout.column(align=True)
        sub = col.row()
        name = prop.name if text is None else text
        if prop.type == 'BOOLEAN' and prop.array_length == 0:
            sub.prop(self, attr, text=name, **kwargs)
        else:
            if name:
                sub.label(name + ':')
            sub = col.row() if row else col.column()
            if prop.type == 'ENUM' and \
                    (prop.is_enum_flag or 'expand' in kwargs):
                sub.prop(self, attr, **kwargs)  # text='' だとボタン名が消える為
            else:
                sub.prop(self, attr, text='', **kwargs)
        return col

    def draw_all(self):
        """Draw all operator properties
        :rtype: dict
        """
        columns = {}
        for attr in self.properties.rna_type.properties.keys():
            columns[attr] = self.draw_property(attr, self.layout)
        return columns

    def as_keywords(self, ignore=()):
        """Return a copy of the properties as a dictionary.

        Use collections.OrderedDict instead of dict.
        (original: blender/release/scripts/modules/bpy_types.py:600)

        :type ignore: abc.Iterable
        :rtype: OrderedDict
        """
        from collections import OrderedDict
        ignore = tuple(ignore) + ('rna_type',)
        return OrderedDict(
            [(attr, getattr(self, attr))
             for attr in self.properties.rna_type.properties.keys()
             if attr not in ignore])


def draw_callback_px(self, context):
    pass


class ModalOperator(OperatorBase, bpy.types.Operator):
    """Modal operator example"""
    bl_idname = 'view3d.modal_operator'
    bl_label = 'Simple Modal Operator'

    def draw_handler_add(self, context):
        self._handle = bpy.types.SpaceView3D.draw_handler_add(
                draw_callback_px, (self, context), 'WINDOW', 'POST_PIXEL')

    def draw_handler_remove(self):
        bpy.types.SpaceView3D.draw_handler_remove(self._handle, 'WINDOW')

    def redraw(self, context):
        context.area.tag_redraw()

    def __init__(self):
        self._handle = None

    @classmethod
    def poll(cls, context):
        return True

    def check(self, context):
        return False

    def execute(self, context):
        user_preferences = context.user_preferences
        addon_prefs = user_preferences.addons[__name__].preferences

        return {'FINISHED'}

    def modal(self, context, event):
        if event.type == 'INBETWEEN_MOUSEMOVE':
            return {'PASS_THROUGH'}

        elif event.type == 'MOUSEMOVE':
            # commit 53a3850a8a05249942a0c4a16060e9491456af02
            # source/blender/editors/interface/interface_handlers.c:9200
            # let's make sure we are really not hovering a button by adding
            # a mousemove!
            # XXX some WM_event_add_mousemove calls may become unnecessary
            # with this and can be removed
            #
            # パネル上のボタン類が無い所にマウスを置くと絶えず'MOUSEMOVE'
            # イベントが発生し続ける。
            if (event.mouse_x == event.mouse_prev_x and
                    event.mouse_y == event.mouse_prev_y):
                return {'PASS_THROUGH'}

        if event.type in {'LEFTMOUSE', 'SPACE', 'RET', 'NUMPAD_ENTER'}:
            self.draw_handler_remove()
            self.redraw(context)
            return {'FINISHED'}

        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            self.draw_handler_remove()
            self.redraw(context)
            return {'CANCELLED'}

        self.execute(context)

        self.redraw(context)

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        if context.area.type == 'VIEW_3D':
            self.options.use_cursor_region = True  # context.regionのみ更新
            self.draw_handler_add(context)
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'WARNING'}, "View3D not found, cannot run operator")
            return {'CANCELLED'}

    def cancel(self, context):
        pass

    def draw(self, context):
        pass


def register():
    bpy.utils.register_class(ModalOperator)


def unregister():
    bpy.utils.unregister_class(ModalOperator)


if __name__ == "__main__":
    register()
